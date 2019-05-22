#!/bin/sh

# erzeugt Mittwoch, 22. Mai 2019 17:53 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:40 von Leander Jedamus

mv vim_doc.py vim.py
make
mv vim.py vim_doc.py
#rm -rf __pycache__

# vim:ai sw=2

