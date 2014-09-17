"""
Modulo ejemplo

>>> ej("2")
'Hola mundo dos'
>>> ej()
'Hola mundo '
"""

def ej(s=""):
	"""Ejemplo

	>>> ej("!")
	'Hola mundo !'
	"""
	return( 'Hola mundo ' + s )

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description='Hola mundo mas algo...')
	parser.add_argument('Text', metavar='T', type=str, nargs=1,
                   help='Texto a imprimir')

	args = parser.parse_args()
	print(ej(args.Text[0]))
