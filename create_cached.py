#!/bin/env python
import htcondor
import glob
import time
import sys
cached = htcondor.Cached()
cacheName = sys.argv [1]
try:
	cached.createCacheDir(cacheName,int(time.time())+1000)
	print "cacheName=",cacheName
except RuntimeError:
	print "Create cache failed"
	sys.exit(1)
input_glob = glob.glob(sys.argv[2])
print input_glob
try:
	cached.uploadFiles(cacheName,input_glob)
except:
	print "Upload files Fail"
sys.exit(1)
