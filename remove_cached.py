#!/bin/env python
import htcondor
import glob
import time
import sys
cached = htcondor.Cached()
cacheName = sys.argv [1]
try:
	cached.removeCacheDir(cacheName)
	print "cacheName=",cacheName
except RuntimeError:
	print "Remove cache failed"
	sys.exit(1)
sys.exit(1)
