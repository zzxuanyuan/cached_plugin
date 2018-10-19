#!/bin/env python
import htcondor
import glob
import time
import sys
cached = htcondor.Cached()
cacheSource = sys.argv[1]
cacheDestination = sys.argv[2]
cacheName = sys.argv[3]
redundancyPolicy = "Replication"
try:
	cached.createCacheDir2(cacheSource, cacheDestination, cacheName, int(time.time())+1000, redundancyPolicy)
	print "cacheName=",cacheName
except RuntimeError:
	print "Create cache failed"
	sys.exit(1)
input_glob = glob.glob(sys.argv[4])
print input_glob
try:
	cached.uploadFiles2(cacheDestination,cacheName,input_glob)
except:
	print "Upload files Fail"
sys.exit(1)
