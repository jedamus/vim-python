#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 04. Dezember 2012 17:21 (C) 2012 by Leander Jedamus
# modifiziert Montag, 20. Mai 2019 17:02 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:41 von Leander Jedamus
# modifiziert Donnerstag, 02. Mai 2019 16:24 von Leander Jedamus
# modifiziert Montag, 16. Juli 2018 16:00 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:26 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modifiziert Freitag, 26. Juni 2015 20:03 von Leander Jedamus
# modifiziert Montag, 11. März 2013 08:40 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:50 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:07 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:57 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:24 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:28 by Leander Jedamus
# modified Dienstag, 04. Dezember 2012 17:25 by Leander Jedamus

import os
import sys
import re
sys.path.append(os.environ['HOME']+'/vim/python')

import vim
import pyvim as p

p.b()[0:0] = [ "#!/usr/bin/env python",
               "# coding=utf-8 -*- python -*-",
               "",
               "# {cb:s}".format(cb=p.cb()),
               "",
               "from __future__ import print_function",
             ]

line=6
command="2k"
if (re.match(r"test_.*\.py",p.bn())):
  n = re.sub(r"(.*).py","\g<1>",p.bn())
  ln = re.sub(r"test_(.*).py","\g<1>",p.bn())
  un = ln[0].upper() + ln[1:]
  t = "Test_{un:s}".format(un=un)
  tm = "test{ln:s}".format(ln=ln)

  p.b()[line:0] = [
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
  line=32
  command="25k"

p.b()[line:0] = [ "",
               "# vim:ai sw=2 sts=4 expandtab"
             ]
vim.command("normal "+command)

# vim:ai sw=2 sts=4 expandtab

