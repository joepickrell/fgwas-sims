#!/usr/bin/python

import sys, os

fcausal = sys.argv[1]
fnoncausal = sys.argv[2]
for i in range(100):
	cmd = "echo 'python simannot.py ../sim"+str(i)+"/sim"+str(i)+".fgwasin.gz ../sim"+str(i)+"/sim"+str(i)+"_"+fcausal+"_"+fnoncausal+".fgwasin.gz ../../subset/causals.txt "+fcausal+" "+fnoncausal+"' | qsub -V -cwd -q res.q -o /dev/null -e /dev/null"
	print cmd
	os.system(cmd) 
