#!/usr/bin/python

import htcondor
import classad
import datetime
import shutil
import sys
import time

coll = htcondor.Collector()
ads = coll.query(htcondor.AdTypes.Any, "true", ["CachedServer", "MyAddress", "Machine", "Name"])
print ads
