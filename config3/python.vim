autocmd BufNewFile test_*.py py3file ~/vim/python/vim_test_py_neu.py

autocmd BufNewFile *.py py3file ~/vim/python/vim_py_neu.py
autocmd BufWritePre *.py py3file ~/vim/python/vim_py_geaendert.py
autocmd BufEnter *.py py3file ~/vim/python/vim_py_enter.py

