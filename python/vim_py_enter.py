#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Freitag, 20. November 2020 07:33 von Leander Jedamus
# modifiziert Donnerstag, 19. November 2020 09:08 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 14:48 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:45 von Leander Jedamus
# modifiziert Montag, 16. Juli 2018 15:45 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:56 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:37 von Leander Jedamus

"""
  Dieses Skript wird bei jedem Bufferwechsel in eine *.py-
  oder *.pyw-Datei aufgerufen und setzt einige Register:

  @g (gettext): Setzt einige Zeilen für die Verwendung von gettext
  (um verschiedene Sprachen zu benutzen).

  @l (logging): Setzt einige Zeilen zum Loggen.

  @p (print): Setzt den import der print-Funktion aus __future__.

  @h (home): Setzt einige Zeilen für ~/.vim/python/Dateien, die das
  Modul pyvim.py sonst nicht finden.

"""

import os
import sys
sys.path.append(os.environ['HOME']+"/.vim/python")

import pyvim as p

p.drs()
#p.sr("a","iich bin in python.\n\e")
p.sr("g",":se noai\ni\nimport os\nimport sys\nimport gettext\n\nscriptpath = os.path.abspath(os.path.dirname(sys.argv[0]))\ntry:\n  trans = gettext.translation(\"download-sortierer.py\",os.path.join(scriptpath, \\\n                              \"locale\"))\n  trans.install(unicode=True)\nexcept IOError:\n  print (\"Fehler in gettext\")\n  def _(s):\n    return s\n\e7k7w:se ai\n")
p.sr("o",":se noai\ni\nimport os\nimport sys\nimport logging\n\nlog_path_and_filename = os.path.join(\"/tmp\",\"download-sortierer.log\")\nfile_handler = logging.FileHandler(log_path_and_filename)\nstdout_handler = logging.StreamHandler(sys.stdout)\nformatter = logging.Formatter(\"%(asctime)s %(levelname)s: %(message)s\",\n                              \"%d.%m.%Y %H:%M:%S\")\nfile_handler.setFormatter(formatter)\nstdout_handler.setFormatter(formatter)\nlog = logging.getLogger()\nlog.addHandler(file_handler)\nlog.addHandler(stdout_handler)\nlog.setLevel(logging.INFO)\n\e:se ai\n11k7w2l")
p.sr("l",":se noai\ni\nimport os\nimport sys\nimport logging\nimport logging.config\nimport atexit\nimport time\n\natexit.register(logging.shutdown)\nlogging.Formatter.converter=time.gmtime\nlogging._srcFile=None\nlogging.logThreads=0\nlogging.logProcesses=0\nlogging.config.fileConfig(\"logging.conf\")\nlogger = logging.getLogger(__name__)\n\e:se ai\n")
p.sr("p",":se noai\nifrom __future__ import print_function\n\e:se ai\n")
p.sr("h",":se noai\n/import\nkA\nimport os\nimport sys\nsys.path.append(os.environ['HOME']+'/vim/python')\n\e:se ai\n")

# vim:ai sw=2 sts=4 expandtab

