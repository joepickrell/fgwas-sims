#!/usr/bin/python

import sys,os, re

ff = os.listdir(".")
for f in ff:
	if re.search(".hap", f) != None:
		tmp = f.split(".")
		tmp = ".".join(tmp[:(len(tmp)-1)])
		cmd = "R --vanilla --args "+tmp+" < getf.R"
		print cmd
		os.system(cmd)
