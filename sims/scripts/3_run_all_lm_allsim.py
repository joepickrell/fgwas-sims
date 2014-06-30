#!/usr/bin/python

import sys, os

for i in range(100):
	cmd = "python run_alll_lm.py ../sim"+str(i)+"/ ../sim"+str(i)+"/sim"+str(i)+".pheno"
	print cmd
	os.system(cmd)
