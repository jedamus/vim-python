# vim-python
Python scripts for use with vim

These are a collection of python-scripts, which work with vim (if compiled so).
They give a structure to new files (for example perl.pl). Existing files get a date and time stamp and the user, who edited the file. The information is taken from the GECOS-Field.

Maybe you have to export PYTHONPATH="~/vim/python".

file structure:
~/.exrc ~/.vimrc ~/vim/config ~/vim/python

You have to decide if you copy ~/vim/.vimrc or ~/vim/.vimrc3.
This depends on which command vim uses to execute a python script.
On my Ubuntu 16.04 LTS it is py3file (so use ~/vim/.virmrc3 for ~/.virmrc).
On my Mac it is pyfile (so use ~/vim/.vimrc for ~/.vimrc).

