#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print "before print"
servers = sys.argv[1]
cacheName = sys.argv[2]
cacheId = sys.argv[3]
files = sys.argv[4]
cached.distributeReplicas(servers, cacheName, cacheId, files)
print "after print"
#cached.downloadFiles(sys.argv[1], os.getcwd())
