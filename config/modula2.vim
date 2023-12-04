autocmd BufNewFile *.mod pyfile ~/.vim/python/vim_mod_neu.py
autocmd BufWritePre *.mod pyfile ~/.vim/python/vim_mod_geaendert.py
autocmd BufEnter *.,mod pyfile ~/.vim/python/vim_mod_enter.py
autocmd BufNewFile *.def pyfile ~/.vim/python/vim_def_neu.py
autocmd BufWritePre *.def pyfile ~/.vim/python/vim_def_geaendert.py
" autocmd BufEnter *.def pyfile ~/.vim/python/vim_def_enter.py
