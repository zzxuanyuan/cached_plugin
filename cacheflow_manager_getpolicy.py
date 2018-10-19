#!/usr/bin/python

import htcondor
import classad
import time
import os
import sys

cacheflow_manager = htcondor.CacheflowManager()

job_ad = classad.ClassAd();
job_ad["CachedServer"] = sys.argv[1]
job_ad["MaxFailureRate"] = 0.1
job_ad["TimeToFailureMinutes"] = 25
job_ad["CacheSize"] = 102400
print cacheflow_manager.getStoragePolicy(job_ad)

#cached.downloadFiles(sys.argv[1], os.getcwd())
