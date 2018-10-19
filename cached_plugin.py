#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print cached.listCacheDirs()


print "Now trying replication..."

#output = cached.requestLocalCache("cached-25511@red-foreman.unl.edu", "/humandatabase")

if len(sys.argv) != 3:
    print "Need 2 arguments to program, originator and database name"

while True:
    print "Now = " + time.strftime("%c")
    try:
        output = cached.requestLocalCache(sys.argv[1], sys.argv[2])
    except RuntimeError:
        print "Failed to reach remote server"
        try:
            cached = htcondor.Cached()
        except:
            pass
        time.sleep(10)
        continue

    print output
    if "CacheState" in output:
        if output["CacheState"] == 3:
            print "Finished replication"
            break
	else:
            print "CacheState=",output["CacheState"]    
    print "Trying request again"
    time.sleep(10)


cached.downloadFiles(sys.argv[2], os.getcwd())


