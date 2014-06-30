#!/usr/bin/python

import sys, os

infile = open("../../subset/causals.txt")
stem = sys.argv[1]
phenofile = sys.argv[2]
index  = 0
for line in infile.xreadlines():
	line = line.strip().split()
	tmp = line[6].split(".")
	tmp = ".".join(tmp[:(len(tmp)-1)])
	cmd = "echo 'R --vanilla --args "+stem+tmp+".hap.controls.haps.gz "+stem+tmp+".hap.legend "+phenofile+" "+stem+tmp+".Z "+str(index)+" < runlm.R' | qsub -V -cwd -q res.q -e /dev/null -o /dev/null"
	print cmd
	os.system(cmd)
	index = index+1
