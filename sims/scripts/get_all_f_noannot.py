#!/usr/bin/python

import sys, os

fannot = sys.argv[1]
fnannot = sys.argv[2]

for i in range(100):
	cmd = "python get_f_noannot.py ../sim"+str(i)+"/sim"+str(i)+"_noannot.bfs.gz ../sim"+str(i)+"/sim"+str(i)+"_"+fannot+"_"+fnannot+".bfs.gz"
	os.system(cmd)
