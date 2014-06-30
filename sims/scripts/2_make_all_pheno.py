#!/usr/bin/python

import sys, os

for i in range(100):
	cmd = "echo 'python make_pheno.py ../sim"+str(i)+"/ ../sim"+str(i)+"/sim"+str(i)+".pheno ../../subset/causals.txt' | qsub -V -cwd -q res.q -o /dev/null -e "+str(i)+".e"
	print cmd
	os.system(cmd)
