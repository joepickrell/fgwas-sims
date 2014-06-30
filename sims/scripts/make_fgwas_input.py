#!/usr/bin/python

import sys, os

stem = sys.argv[1]
outfile = sys.argv[2]

cmd = "head -n 1 "+stem+"0.1.9835.19835.Z | gzip - > "+sys.argv[2]
print cmd
os.system(cmd)
cmd = "cat "+stem+"*.Z | grep -v NA | grep -v SEGNUMBER | sort -k 8n -k3n | gzip - >> "+sys.argv[2]
print cmd
os.system(cmd)
