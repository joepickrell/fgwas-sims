#!/usr/bin/python

import sys, os, gzip, random

infile =gzip.open(sys.argv[1])
outfile = gzip.open(sys.argv[2], "w")
causalfile = open(sys.argv[3])
fcausal = float(sys.argv[4])
fnoncausal = float(sys.argv[5])

causals = set()
causal2index = dict()
index = 0
for line in causalfile.xreadlines():
	line = line.strip().split()
	causals.add(line[0])
	causal2index[line[0]] = index
	index = index+1

print causal2index

index = 0
line = infile.readline()
line = line.strip()
print >> outfile, line, "simannot"
line = infile.readline()
while line:
	line = line.strip().split()
	rs = line[0]
	#print line[7]
	if rs in causals and str(causal2index[rs]) == line[7]:
		r = random.random()
		if r < fcausal:
			print >> outfile, " ".join(line), "1"
		else:
			print >> outfile, " ".join(line), "0"
	else:
		r = random.random()
		if r < fnoncausal:
			print >> outfile, " ".join(line), "1"
		else:
			print >> outfile, " ".join(line), "0"
	line = infile.readline()		
