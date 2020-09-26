autocmd BufNewFile *.java py3file ~/.vim/python/vim_java_neu.py
autocmd BufWritePre *.java py3file ~/.vim/python/vim_java_geaendert.py
autocmd BufEnter *.java py3file ~/.vim/python/vim_java_enter.py
