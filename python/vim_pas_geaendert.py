#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 10. Oktober 2017 12:01 (C) 2017 by Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:40 von Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 12:02 von Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import pyvim as p

p.M(3,"(* "," *)")

# vim:ai sw=2 sts=4 expandtab

