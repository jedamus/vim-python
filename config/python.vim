autocmd BufNewFile *.py pyfile ~/vim/python/vim_last_py_neu.py
autocmd BufNewFile test_*.py pyfile ~/vim/python/vim_test_py_neu.py

autocmd BufNewFile *.py pyfile ~/vim/python/vim_py_neu.py
autocmd BufWritePre *.py pyfile ~/vim/python/vim_py_geaendert.py
autocmd BufEnter *.py pyfile ~/vim/python/vim_py_enter.py

