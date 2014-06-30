#!/usr/bin/python

import sys, os, gzip

infile = gzip.open(sys.argv[1])
total = 0
annot = 0

line = infile.readline()
line = infile.readline()
while line:
	line = line.strip().split()
	PPA = float(line[9])
	a = line[11]
	total = total+PPA
	if a == "1":
		annot =annot+PPA
	line = infile.readline()
print annot/total
