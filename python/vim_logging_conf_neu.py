#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Freitag, 20. November 2020 15:40 (C) 2020 von Leander Jedamus
# modifiziert Samstag, 21. November 2020 08:43 von Leander Jedamus
# modifiziert Freitag, 20. November 2020 15:55 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine Datei namens
  logging.conf erzeugt werden soll.
"""

import os
import sys
import re
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

p.b()[0:0] = [
"[loggers]",
"keys=root,__main__,module",
"",
"[handlers]",
"keys=stdoutHandler,fileHandler,rotateFileHandler,nullHandler",
"",
"[formatters]",
"keys=stdFormatter",
"",
"[logger_root]",
"level=DEBUG",
"handlers=fileHandler,stdoutHandler",
"",
"[logger___main__]",
"level=DEBUG",
"#level=INFO",
"handlers=fileHandler,stdoutHandler",
"#handlers=nullHandler",
"qualName=__main__",
"propagate=0",
"",
"[logger_module]",
"level=DEBUG",
"#level=INFO",
"handlers=fileHandler,stdoutHandler",
"#handlers=nullHandler",
"qualName=module",
"propagate=0",
"",
"[handler_fileHandler]",
"class=FileHandler",
"level=DEBUG",
"formatter=stdFormatter",
"args=(\"logger.log\", \"a\")",
"",
"[handler_stdoutHandler]",
"class=StreamHandler",
"level=DEBUG",
"formatter=stdFormatter",
"args=(sys.stdout,)",
"",
"[handler_rotateFileHandler]",
"class=logging.handlers.RotatingFileHandler",
"level=DEBUG",
"formatter=stdFormatter",
"args=(\"logger.log\",\"a\", 1024, 5)",
"",
"[handler_nullHandler]",
"class=NullHandler",
"level=DEBUG",
"formatter=stdFormatter",
"args=()",
"",
"[formatter_stdFormatter]",
"format=%(asctime)s %(name)-10s %(levelname)-8s: %(message)s",
"datefmt=%d.%m.%Y %H:%M:%S %Z",
]
vim.command("normal 56k")

# vim:ai sw=2 sts=4 expandtab

