#!/usr/bin/python

import sys, os


for i in range(100):
	cmd = "echo 'fgwas -i ../sim"+str(i)+"/sim"+str(i)+".fgwasin.gz -o ../sim"+str(i)+"/sim"+str(i)+"_noannot -fine -print -p 0' | qsub -V -cwd -o /dev/null -e /dev/null -q res.q"
	print cmd
	os.system(cmd)
