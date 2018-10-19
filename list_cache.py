#!/usr/bin/python

import htcondor
import time
import os
import sys

cached = htcondor.Cached()

print cached.listCacheDirs(sys.argv[1])

#cached.downloadFiles(sys.argv[1], os.getcwd())
