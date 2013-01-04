"""
	A dobble generator

	It takes a folder as an import and generate a dobble with 
	the pictures contained in the folder.
"""

import argparse


def list_symbols(source):
	"""
	List all symbols to use for the game
	"""
	return 1


def generate_cards(symbols):
	"""
	Generate the list of cards.
	"""
	return 1


def draw_cards(symbols):
	"""
	Render the game as png files.
	"""
	return 1


def parse_arguments():
	"""
	Parse argument to determine where to pick pictures from and 
	where to output the cards.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--source', dest='source', 
	                   help='folder containing the photos')
	parser.add_argument('-o', '--output', dest='output', 
	                   help='destination folder for the cards.')

	args = parser.parse_args()

	assert(args.source)
	assert(args.output)

	return args.source, args.output


if __name__ == '__main__':
	source, target = parse_arguments()
	symbols = list_symbols(source)
	cards = generate_cards(symbols)
	draw_cards(cards)