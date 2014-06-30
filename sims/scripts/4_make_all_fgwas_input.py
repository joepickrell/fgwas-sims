#!/usr/bin/python

import sys, os

for i in range(8, 100):
	cmd = "echo 'python make_fgwas_input.py ../sim"+str(i)+"/ ../sim"+str(i)+"/sim"+str(i)+".fgwasin.gz' | qsub -V -cwd -q res.q -e /dev/null -o /dev/null"
	print cmd
	os.system(cmd)
