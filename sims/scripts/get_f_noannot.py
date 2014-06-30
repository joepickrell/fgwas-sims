#!/usr/bin/python

import sys, os, gzip

infile = gzip.open(sys.argv[1])
infile2 = gzip.open(sys.argv[2])
total = 0
annot = 0

inannot = set()

line = infile2.readline()
line = infile2.readline()
while line:
	line = line.strip().split()
	a = line[11]
	if a == "1":
		inannot.add(line[0])
	line = infile2.readline()

infile2.close()
line = infile.readline()
line = infile.readline()
while line:
	line = line.strip().split()
	PPA = float(line[9])
	total = total+PPA
	if line[0] in inannot:
		annot =annot+PPA
	line = infile.readline()
print annot/total
