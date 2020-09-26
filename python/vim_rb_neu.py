#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Donnerstag, 30. Mai 2019 14:30 (C) 2019 von Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:54 von Leander Jedamus
# modifiziert Freitag, 14. Juni 2019 13:14 von Leander Jedamus
# modifiziert Freitag, 07. Juni 2019 17:56 von Leander Jedamus
# modifiziert Freitag, 31. Mai 2019 11:13 von Leander Jedamus
# modifiziert Donnerstag, 30. Mai 2019 14:32 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.rb-Datei neu
  erzeugt werden soll.

"""

from __future__ import print_function
import os
import sys
import re

sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

command_line = 0
insert = []

"""
  Das ist der Header einer Ruby-Datei. cb steht für created by
  (siehe pyvim.py).
"""
kette = [ "#!/usr/bin/ruby -w",
          "# -*- coding: utf-8 -*-",
          "",
          "# {cb:s}".format(cb=p.cb()),
          "",
          'require "English"',
        ]

insert.extend(kette)
command_line = 7

if (re.match(r"test_.*\.rb",p.bn())):
  kette = [ 'require "test/unit"' ]
  insert.extend(kette)
  command_line += 1 

kette = [ '$LOAD_PATH.unshift(ENV["HOME"]+"/Projekte/ruby/lib")',
          '$LOAD_PATH.unshift(File.expand_path(File.dirname($PROGRAM_NAME)))',
          '$LOAD_PATH.unshift(".")',
        ]

insert.extend(kette)
command_line += 3

"""
  Wenn der Dateiname mit test_ beginnt, so liegt eine
  Datei für eine Testumgebung (unittest) vor.
"""
if (re.match(r"test_.*\.rb",p.bn())):
  """ Hier wird der Dateiname ohne Pfad extrahiert. """
  n = re.sub(r"(.*).rb","\g<1>",p.bn())

  """ Hier wird der zu testenden Klasse extrahiert. """
  ln = re.sub(r"test_(.*).rb","\g<1>",p.bn())

  """ Der erste Buchstabe soll groß sein, der Rest wird
      übernommen. """
  un = ln[0].upper() + ln[1:]

  """ Name der Klasse """
  t = "Test_{un:s}".format(un=un)

  """ Name der Testmethode """
  tm = "test{ln:s}".format(ln=ln)

  kette = [ 'require "{ln:s}"'.format(ln=ln),
            "",
            "class {t:s} < Test::Unit::TestCase".format(t=t),
            "",
            "  def setup",
            '    print("Erzeuge Testdaten. ")',
            "  end",
            "",
            "  def teardown",
            '    print("Lösche Testdaten. ")',
            "  end",
            "",
            "  def {tm:s}1".format(tm=tm),
            "    wert1 = 2",
            "    wert2 = 2",
            '    msg = "Werte sind unterschiedlich."',
            "    assert_equal(wert1, wert2, msg)",
            "  end",
            "",
            "end",
          ]
  insert.extend(kette)
  command_line += 1


kette = [ "",
          "# vim:ai sw=2 sts=4 expandtab"
        ]
insert.extend(kette)

p.b()[0:0] = insert
vim.command("normal " + ":1\n:{cl:d}\n".format(cl=command_line))

# vim:ai sw=2 sts=4 expandtab

