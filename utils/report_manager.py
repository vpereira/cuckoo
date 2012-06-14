#!/usr/bin/env python
# Copyright (C) 2010-2012 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import sys
import logging
import webbrowser
logging.basicConfig()

sys.path.append(".")
sys.path.append("..")

from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.core.processor import Processor
from lib.cuckoo.core.reporter import Reporter
from lib.cuckoo.common.constants import CUCKOO_ROOT

if CUCKOO_ROOT == "." or not os.path.exists(CUCKOO_ROOT):
    print("ERROR: you need to specify a valid absolute root directory in lib/cuckoo/common/constants.py")
else:
    storage_path = os.path.join(CUCKOO_ROOT,"storage","analyses",sys.argv[1])
    if os.path.exists(storage_path):
    	Reporter(storage_path).run(Processor(storage_path).run())
	report_file = os.path.join(storage_path,"reports","report.html")
	webbrowser.open(report_file)

    else:
        print "Sorry but %s doesnt exist" % storage_path

