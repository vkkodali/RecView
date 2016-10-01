#!/usr/bin/python

import sys, csv

# See http://stackoverflow.com/questions/14207708/ioerror-errno-32-broken-pipe-python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

inputfile = sys.argv[1]
csv_f = csv.reader(open(inputfile, "rb"), delimiter = '\t')

csv_f = csv.reader(sys.stdin, delimiter = '\t')
header = next(csv_f)

for row in csv_f:
	i = 1
	j = 0
	while (j < len(row) ):
		print ("{:>30s} [{:3d}]: {}" .format(header[j], i, row[j]))
		i, j = i+1, j+1
	print ("\n")
