# coding: utf-8

def identity(seqa, seqb):
    """Retorna la identidad entre dos secuencias de igual longitud"""
    
    l = len(seqa)
    if l != len(seqb):
        raise Exception("Sequences of different lengths")
        
    counter = 0.0
    for i in range(0,l):
        if seqa[i] == seqb[i]:
            counter += 1.0
            
    return(counter/l)

import math
import numpy as np

def dotmatrix(seqa, seqb, window_size=1, threshold=1):
    """Retorna una Dot Matrix (numpy array)
    seqa en las filas, de arriba a abajo
    seqb en las columnas, de izquierda a derecha
    Las secuencias se recorren por ventanas de longitud window_size
    Step size: 1 
    Para cada par de ventanas, se compara la identidad contra un valor threshold. 
    Si la identidad es igual o superior:
    Se coloca un 1 en el centro del cuadrado definido por las ventanas, si la longitud es impar."""
    la = len(seqa)
    lb = len(seqb)
    
    if window_size > la or window_size > lb:
        raise Exception("Window size needs to be less than sequence lengths")
        
    center_window = int( math.ceil(window_size/2.0) ) - 1
    
    mat = np.zeros((la,lb))
    
    for i in range(0, la-window_size+1):
        
        subseqa = seqa[i:i+window_size]
        mati = i + center_window
        
        for j in range(0, lb-window_size+1):
            
            if identity(subseqa, seqb[j:j+window_size]) >= threshold:
                mat[mati, j + center_window ] = 1
                
    return(mat)

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

def dotplot(seqa, seqb, window_size=1, threshold=1):
    """DotPlot usando dotmatrix()
    seqa en x
    seqb en y"""
    cm = dotmatrix(seqb, seqa, window_size, threshold)
    return( plt.pcolormesh( cm , cmap=plt.cm.gray_r ) )

def randseq(k = 5, letters="ACTG"):
    
    rand = np.array([c for c in letters])[np.random.randint(0, len(letters), k)]
    return( "".join(rand) )

from scipy.misc import comb
def prob_binomial(p=0.25, k=5):
    P = [ comb(k,n) * p**n * (1-p)**(k-n) for n in range(0,6) ]
    return( P )

def choose_threshold(alpha=0.05, p=0.25, k=5):
    P = prob_binomial(p,k)
    valid = np.cumsum( np.array( P )[ np.arange(k,-1,-1) ] ) <= alpha
    
    if sum(valid) == 0:
        raise Exception("min p: " + str(min(P)))
    
    return( min( np.arange(k,-1,-1)[ valid ] ) / float(k) )

from Bio import SeqIO
CRK = SeqIO.read("P46108.fasta","fasta").seq
GRB2 = SeqIO.read("P62993.fasta","fasta").seq

def information(pi):
    """float -> float"""
    return( -1 * np.log2( pi ) )
    
def entropy(P):
    """list -> float
    Entropía de Shannon para n simbolos de probabilidad pi en la lista P"""
    suma = 0
    for pi in P:
        suma += pi * information(pi)
    
    return(suma)



from Bio.SubsMat import MatrixInfo

from Bio.SubsMat import SeqMat

def subs_numpy(subsmat, letters=None):
    """dict -> numpy array, str"""
    
    if letters == None:
        letters = "".join( set( [ tup[0] for tup in subsmat.keys() ] ) )
    
    l = len(letters)
    
    mat = np.zeros((l,l))
    
    for key, val in subsmat.items():
        i = letters.find( key[0] )
        j = letters.find( key[1] )
        if j != -1 and i != -1:
            mat[i,j] = val
            mat[j,i] = val
        
    return( mat )


aromaticos = "FYW"
hidrofob_peq = "MILB"
hidrofil_peq = "STPAG"
hidrofil_aminas_acidos = "NDEQ"
basicos = "HRK"
sulf = "C"

letters = aromaticos + hidrofob_peq + hidrofil_peq + hidrofil_aminas_acidos + basicos + sulf

