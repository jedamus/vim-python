# vim-python
Python scripts for use with vim

These are a collection of python-scripts, which work with vim (if compiled so).
They give a structure to new files (for example perl.pl). Existing files get a date and time stamp and the user, who edited the file. The information is taken from the GECOS-Field.

## Getting started

file structure:
~/.exrc ~/.vimrc ~/.vim/config ~/.vim/python

You have to decide if you use install2.sh OR install3.sh

This depends on which command vim uses to execute a python script.
On my Ubuntu 16.04 LTS it is "py3file" (so use ./install3.sh)
On my Mac it is "pyfile" (so use ./install2.sh).

## Annotations

You need the package variable in java-files. Try the following:
```
  mkdir -p tmp/de/ljedamus/mypack/pack1
  cd tmp/de/ljedamus/mypack/pack1
  vi test.java
```
Now you see that package is set according to the package variable, which is set
to de.ljedamus

The other variables (www and email) are used for example in .html files.
```
cd tmp
vi test.html
```

