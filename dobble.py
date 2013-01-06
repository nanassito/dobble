"""
	A dobble generator

	It takes a folder as an import and generate a dobble with 
	the pictures contained in the folder.
"""

import argparse
import os
import random
import cairo
import rsvg


def list_symbols(source):
	"""
	List all symbols to use for the game
	"""
	return [ f for f in os.listdir(source) if f[0]!="." ]


def generate_cards(symbols):
	"""
	Generate the list of cards.
	"""
	assert len(symbols)%8 == 0, "We need x*8 symbols."

	if len(symbols) < 20 or len(symbols) > 30:
		print "WARNING : For best result, you need between 20 and 30 different images."

	cards = []
	for j in range(8 * (55/len(symbols))):
		# we shuffle the list and take element from it to be sure
		# that we have the same number of instance of each image.
		random.shuffle(symbols)
		for i in range(0, len(symbols), 8):
			cards.append(symbols[i:i+8])

	return cards


def draw_cards(symbols, target):
	"""
	Render the game as png files.
	"""
	# initialize the cairo renderer
	img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1066, 1066)
	ctx = cairo.Context(img)
	index = 0

	# get the template
	with open("template.svg") as svg_file:
		svg_data = svg_file.read()

		for card in cards:
			card_svg = svg_data % tuple(card)
			handler = rsvg.Handle(None, card_svg)
			handler.render_cairo(ctx)
			img.write_to_png("%s/%s.png" % (target, index))


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

	# assert that both directories exists.
	assert args.source, "missing source directory"
	assert args.output, "missing output directory"
	assert os.path.exists(args.source), \
			"source directory '%s' does not exists" % args.source
	#FIXME: output directory does not need to exists
	assert os.path.exists(args.output), \
			"output directory '%s' does not exists" % args.output

	return args.source, args.output


if __name__ == '__main__':
	source, target = parse_arguments()
	symbols = list_symbols(source)
	cards = generate_cards(symbols)
	draw_cards(cards, target)