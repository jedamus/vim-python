autocmd BufNewFile *.pas pyfile ~/.vim/python/vim_pas_neu.py
autocmd BufWritePre *.pas pyfile ~/.vim/python/vim_pas_geaendert.py
autocmd BufEnter *.pas pyfile ~/.vim/python/vim_pas_enter.py
