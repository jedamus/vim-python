#!/usr/bin/env sh

# erzeugt Montag, 14. Dezember 2020 14:29 (C) 2020 von Leander Jedamus
# modifiziert Montag, 14. Dezember 2020 14:43 von Leander Jedamus

vim=$HOME/.vim

cd $HOME
ln -svf $vim/vimrc3 .vimrc
cp -vp $vim/.exrc $HOME

# vim:ai sw=2

