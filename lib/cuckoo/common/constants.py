# Copyright (C) 2010-2012 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

<<<<<<< HEAD
CUCKOO_ROOT = "/home/security/cuckoo"
=======
import os

CUCKOO_ROOT = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..", ".."))
>>>>>>> 2f7be47bb5b92017fdd7337121e650fba9956193
CUCKOO_VERSION = "0.4-dev"
CUCKOO_GUEST_PORT = 8000
CUCKOO_GUEST_INIT = 0x001
CUCKOO_GUEST_RUNNING = 0x002
CUCKOO_GUEST_COMPLETED = 0x003
CUCKOO_GUEST_FAILED = 0x004
