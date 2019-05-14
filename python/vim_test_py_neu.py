#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Donnerstag, 02. Mai 2019 15:48 (C) 2019 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:46 von Leander Jedamus
# modifiziert Donnerstag, 02. Mai 2019 16:27 von Leander Jedamus

from __future__ import print_function
import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import re
import vim
import pyvim as p

n = re.sub(r"(.*).py","\g<1>",p.bn())
ln = re.sub(r"test_(.*).py","\g<1>",p.bn())
un = ln[0].upper() + ln[1:]
t = "Test_{un:s}".format(un=un)
tm = "test{ln:s}".format(ln=ln)

p.b()[0:0] = [
               "import sys",
               "import unittest",
               "import {ln:s}".format(ln=ln),
               "",
               "class {t:s}(unittest.TestCase):".format(t=t),
               "",
               "  def setUp(self):",
               "    pass",
               "",
               "  def tearDown(self):",
               "    pass",
               "",
               "  def {tm:s}1(self):".format(tm=tm),
               "    pass",
               "",
               "  def {tm:s}2(self):".format(tm=tm),
               "    pass",
               "",
               "if __name__ == '__main__':",
               "# unittest.main()",
               "  suite = unittest.TestSuite()",
               "  test1 = {t:s}('{tm:s}1')".format(t=t,tm=tm),
               "  test2 = {t:s}('{tm:s}2')".format(t=t,tm=tm),
               "  suite.addTests((test1, test2))",
               "  testrunner = unittest.TextTestRunner(verbosity=2, stream=sys.stderr)",
               "  testrunner.run(suite)",
             ]

# vim:ai sw=2 sts=4 expandtab

