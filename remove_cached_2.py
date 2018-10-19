#!/bin/env python
import htcondor
import glob
import time
import sys
cached = htcondor.Cached()
cacheDestination = sys.argv[1]
cacheName = sys.argv [2]
try:
	cached.removeCacheDir2(cacheDestination, cacheName)
	print "cacheName=",cacheName
except RuntimeError:
	print "Remove cache failed"
	sys.exit(1)
sys.exit(1)
