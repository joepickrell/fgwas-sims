#!/usr/bin/python

import sys, os

fannot = sys.argv[1]
fnonannot = sys.argv[2]

for i in range(100):
	cmd = "python get_f.py ../sim"+str(i)+"/sim"+str(i)+"_"+fannot+"_"+fnonannot+".bfs.gz"
	print cmd
	os.system(cmd)
