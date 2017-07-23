#!/usr/bin/python3

import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='''This script displays the
contents of a tsv or csv file, row-by-row with column headers for each
field''')
parser.add_argument('-i', '--input', help='input file, default is stdin')
parser.add_argument('-d', '--delimiter', help='character used for delimiter;'
					'default is tab')

args = parser.parse_args()
infile = args.input

# See http://stackoverflow.com/questions/14207708/ioerror-errno-32-broken-pipe-python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

def recview():
	header = next(tbl)
	l = 0
	for item in header:
		if l < len(item):
			l = len(item)
	for row in tbl:
		i = 1
		j = 0
		while (j < len(row) ):
			print("{:>{}} [{:3d}]: {}" .format(header[j], l, i, row[j]))
			i, j = i+1, j+1
		print('\n')

if args.delimiter:
	delim = args.delimiter
else:
	delim = '\t'

if args.input:
	with open(infile, 'r') as f:
		tbl = csv.reader(f, delimiter = delim)
		recview()
else:
	tbl = csv.reader(sys.stdin, delimiter = delim)
	recview()
