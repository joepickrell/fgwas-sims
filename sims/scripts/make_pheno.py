#!/usr/bin/python

import sys, os, re, gzip, random

indir = sys.argv[1]
outfile = open(sys.argv[2], "w")
causalfile = open(sys.argv[3])

file2index = dict()

causalcount = list()
for i in range(5000):
	causalcount.append(0)

for line in causalfile.xreadlines():
	print line
	line = line.strip().split()
	file = line[6].split(".")
	file = ".".join(file[:4])
	index = int(line[5])
	file2index[file] = index	

print file2index

ff = os.listdir(indir)
for f in ff:
	if re.search(".controls.haps.gz", f) == None:
		continue
	tmp = f.split(".")
	tmp = ".".join(tmp[:4])
	index2find  = file2index[tmp]
	index = 1
	print f
	file = gzip.open(indir+f)
	line = file.readline()
	while line:
		if index == index2find:
			print f, index,  index2find
			line = line.strip().split()
			for i in range(5000):
				h0 = int(line[2*i])
				h1 = int(line[2*i+1])
				causalcount[i] = causalcount[i]+h0+h1
		index = index+1
		line = file.readline()

for i in range(5000):
	print >> outfile, "ind"+str(i), causalcount[i], 
	p = 0.1*float(causalcount[i])+random.gauss(0, 0.7745967)
	print >> outfile, p

