#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print cached.listCacheDirs()


print "Now trying replication..."

if len(sys.argv) != 3:
    print "Need 2 arguments to program, originator and database name"

print "Now = " + time.strftime("%c")
try:
    output = cached.requestLocalCache2(sys.argv[1], sys.argv[2])
except RuntimeError:
    print "Failed to reach remote server"
