from IPython.display import HTML

def web(direccion, alto=500):
    """str [, int]
    Muestra una web"""
    code = '<iframe src="' + direccion +  '"  width=100% height=' + str(alto) + '></iframe>'
    return( HTML(code) )

def wiki(art, idioma="en", modo=None, alto=500):
    """str [, str [, str [, int]]]
    Muestra una wiki por defecto en idioma 'en'
    modo por defecto, None (normal). Probar 'mobile' o 'print'
    """
    if modo=="print":
        direc = 'http://' + idioma + '.wikipedia.org/w/index.php?title=' + art + '&printable=yes'
    elif modo=="mobile":
        direc = "http://" + idioma + ".mobile.wikipedia.org/wiki/" + art
    else:
        direc = "http://" + idioma + ".wikipedia.org/wiki/" + art
    return( web(direc, alto=alto) )

if __name__ == "__main__":
  print("Para importar en IPython Notebook")
