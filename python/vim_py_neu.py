#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 04. Dezember 2012 17:21 (C) 2012 by Leander Jedamus
# modifiziert Mittwoch, 12. Juni 2019 12:41 von Leander Jedamus
# modifiziert Dienstag, 11. Juni 2019 16:31 von Leander Jedamus
# modifiziert Montag, 10. Juni 2019 20:31 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 14:36 von Leander Jedamus
# modifiziert Montag, 20. Mai 2019 17:23 von Leander Jedamus
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

"""
  Dieses Skript wird aufgerufen, wenn eine *.py- oder *.pyw-Datei
  neu erzeugt werden soll.

"""

import os
import sys
import re
sys.path.append(os.environ['HOME']+'/vim/python')

import vim
import pyvim as p

command_line = 0
insert = []

"""
  Das ist der Header einer Python-Datei. cb steht für created by
  (siehe pyvim.py).
"""
kette = [ "#!/usr/bin/env python",
          "# coding=utf-8 -*- python -*-",
          "",
          "# {cb:s}".format(cb=p.cb()),
          "",
          "from __future__ import print_function",
        ]

insert.extend(kette)
command_line = 7

"""
  Wenn der Dateiname mit test_ beginnt, so liegt eine
  Datei für eine Testumgebung (unittest) vor.
"""
if (re.match(r"test_.*\.py",p.bn())):
  """ Hier wird der Dateiname ohne Pfad extrahiert. """
  n = re.sub(r"(.*).py","\g<1>",p.bn())

  """ Hier wird der zu testenden Klasse extrahiert. """
  ln = re.sub(r"test_(.*).py","\g<1>",p.bn())

  """ Der erste Buchstabe soll groß sein, der Rest wird
      übernommen. """
  un = ln[0].upper() + ln[1:]

  """ Name der Klasse """
  t = "Test_{un:s}".format(un=un)

  """ Name der Testmethode """
  tm = "test{ln:s}".format(ln=ln)

  kette = [ "import os",
            "import sys",
            "import unittest",
            "import {ln:s}".format(ln=ln),
            "",
            "file = sys.stderr",
            "wert1 = 2",
            "wert2 = 2",
            "",
            "class {t:s}(unittest.TestCase):".format(t=t),
            "",
            "  def setUp(self):",
            "    print('Erzeuge Testdaten. ', sep='', end='', file=file)",
            "",
            "  def tearDown(self):",
            "    print('Lösche Testdaten. ', sep='', end='', file=file)",
            "    try:",
            "      os.remove('not_existing.txt')",
            "    except OSError:",
            "      pass",
            "",
            "  def {tm:s}1(self):".format(tm=tm),
            "    msg = 'Werte sind unterschiedlich.'",
            "    self.assertEqual(wert1, wert2, msg)",
            "",
            "  def {tm:s}2(self):".format(tm=tm),
            "    self.assertEqual(-1*wert1, -1*wert2)",
            "",
            "if __name__ == '__main__':",
            "# unittest.main()",
            "  suite = unittest.TestSuite()",
            "  test1 = {t:s}('{tm:s}1')".format(t=t,tm=tm),
            "  test2 = {t:s}('{tm:s}2')".format(t=t,tm=tm),
            "  suite.addTests((test1, test2))",
            "  testrunner = unittest.TextTestRunner(verbosity=2, stream=file)",
            "  testrunner.run(suite)",
          ]
  insert.extend(kette)
  command_line += 4

""" Der Abschluß der Datei """
kette = [ "",
          "# vim:ai sw=2 sts=4 expandtab",
        ]
insert.extend(kette)

p.b()[0:0] = insert
vim.command("normal " + ":1\n:{cl:d}\n".format(cl=command_line))

# vim:ai sw=2 sts=4 expandtab

