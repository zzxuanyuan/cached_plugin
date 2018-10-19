#!/usr/bin/python

import htcondor
import time
import os
import sys

so = htcondor.StorageOptimizer()

print "before print"
so.listStorageOptimizers()
print "after print"
#cached.downloadFiles(sys.argv[1], os.getcwd())
