#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:56 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:37 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in python.\n\e")
p.sr("g",":se noai\ni\nimport os\nimport sys\nimport gettext\n\nscriptpath = os.path.abspath(os.path.dirname(sys.argv[0]))\ntry:\n  trans = gettext.translation(\"download-sortierer.py\",os.path.join(scriptpath, \\\n                              \"translate\"))\n  trans.install(unicode=True)\nexcept IOError:\n  print (\"Fehler in gettext\")\n  def _(s):\n    return s\n\e7k7w:se ai\n")
p.sr("l",":se noai\ni\nimport os\nimport sys\nimport logging\n\nlog_path_and_filename = os.path.join(\"/tmp\",\"download-sortierer.log\")\nfile_handler = logging.FileHandler(log_path_and_filename)\nstdout_handler = logging.StreamHandler(sys.stdout)\nformatter = logging.Formatter(\"%(asctime)s %(levelname)s: %(message)s\",\n                              \"%d.%m.%Y %H:%M:%S\")\nfile_handler.setFormatter(formatter)\nstdout_handler.setFormatter(formatter)\nlog = logging.getLogger()\nlog.addHandler(file_handler)\nlog.addHandler(stdout_handler)\nlog.setLevel(logging.INFO)\n\e11k7w2l")

# vim:ai sw=2 sts=4 expandtab

