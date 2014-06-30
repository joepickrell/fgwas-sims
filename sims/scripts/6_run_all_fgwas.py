#!/usr/bin/python

import sys, os

fcausal = sys.argv[1]
fnoncausal = sys.argv[2]

for i in range(100):
	cmd = "echo 'fgwas -i ../sim"+str(i)+"/sim"+str(i)+"_"+fcausal+"_"+fnoncausal+".fgwasin.gz -o ../sim"+str(i)+"/sim"+str(i)+"_"+fcausal+"_"+fnoncausal+" -fine -print -p 0 -w simannot' | qsub -V -cwd -o /dev/null -e /dev/null -q res.q"
	print cmd
	os.system(cmd)
