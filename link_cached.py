#!/bin/env python
import htcondor
import glob
import time
import sys
cached = htcondor.Cached()
directory = "/home/centos/test"
cacheName = sys.argv [1]
try:
	cached.linkCacheDir(cacheName,int(time.time())+1000,directory)
	print "cacheName=",cacheName
except RuntimeError:
	print "Create cache failed"
	sys.exit(1)
sys.exit(1)
