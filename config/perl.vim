autocmd BufNewFile *.pl pyfile ~/vim/python/vim_pl_neu.py
autocmd BufWritePre *.pl pyfile ~/vim/python/vim_pl_geaendert.py
autocmd BufEnter *.pl pyfile ~/vim/python/vim_pl_enter.py

autocmd BufNewFile *.pm pyfile ~/vim/python/vim_pm_neu.py
autocmd BufWritePre *.pm pyfile ~/vim/python/vim_pm_geaendert.py
autocmd BufEnter *.pm pyfile ~/vim/python/vim_pl_enter.py
