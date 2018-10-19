#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print cached.listCacheDirs()


print "Now trying replication..."

#output = cached.requestLocalCache("cached-25511@red-foreman.unl.edu", "/humandatabase")

if len(sys.argv) != 4:
    print "Need 2 arguments to program, originator and database name"

while True:
    print "Now = " + time.strftime("%c")
    try:
	output = cached.encodeFile(sys.argv[1], sys.argv[2], sys.argv[3])
    except RuntimeError:
        print "Failed to reach remote server"
        try:
            cached = htcondor.Cached()
        except:
            pass
        time.sleep(10)
        continue

    if output is 0:
        print "Succeeded"
	break
    else:
        print "Failed"

    print output
