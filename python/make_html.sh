#!/bin/sh

# erzeugt Mittwoch, 22. Mai 2019 17:53 (C) 2019 von Leander Jedamus
# modifiziert Samstag, 21. November 2020 13:55 von Leander Jedamus
# modifiziert Sonntag, 26. Mai 2019 11:58 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:47 von Leander Jedamus

export PATH=/usr/local/bin:/usr/bin:/bin

#mv vim_doc.py vim.py
make
#mv vim.py vim_doc.py
rm -rf vim.pyc __pycache__

# vim:ai sw=2

