#!/usr/bin/python3

import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='''This script displays the
contents of a tab-separated file, row-by-row with column headers for each
field''')
parser.add_argument('-i', '--input', help='input file, default is stdin')

args = parser.parse_args()

infile = args.input

# See http://stackoverflow.com/questions/14207708/ioerror-errno-32-broken-pipe-python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

def pivot():
	header = next(tbl)
	l = 0
	for item in header:
		if l < len(item):
			l = len(item)
	for row in tbl:
		i = 1
		j = 0
		while (j < len(row) ):
			# line_new = '{:>30} {:<3} {:<3}'.format(header[j], i, row[j])
			# print(line_new)
			print("{:>{}} [{:3d}]: {}" .format(header[j], l, i, row[j]))
			# print(header[j], '[', i, ']:  ', row[j])
			i, j = i+1, j+1
		print('\n')

# csv_f = csv.reader(open(infile, "rb"), delimiter = '\t')
# header = []
if args.input:
	# tbl = csv.reader(open(infile, "r"), delimiter = '\t')
	with open(infile, 'r') as f:
		tbl = csv.reader(f, delimiter = '\t')
		pivot()
else:
	tbl = csv.reader(sys.stdin, delimiter = '\t')
	pivot()
