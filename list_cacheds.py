#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print "before print"
cached.listCacheDs()
print "after print"
#cached.downloadFiles(sys.argv[1], os.getcwd())
