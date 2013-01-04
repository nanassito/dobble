"""
	A dobble generator

	It takes a folder as an import and generate a dobble with 
	the pictures contained in the folder.
"""

#import random

def list_symbols():
	"""
	List all symbols to use for the game
	"""
	pass


def generate_cards(symbols):
	"""
	Generate the list of cards.
	"""
	pass


def draw_cards(symbols):
	"""
	Render the game as png files.
	"""
	pass


def parse_arguments():
	"""
	Parse argument to determine where to pick pictures from and 
	where to output the cards.
	"""
	pass


if __name__ == '__main__':
	source, target = parse_arguments()
	symbols = list_symbols(source)
	cards = generate_cards(symbols)
	draw_cards()