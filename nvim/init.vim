set tabstop=4
set softtabstop=4
set shiftwidth=4
set nu
set relativenumber
set nohlsearch
set hidden
set expandtab
set smartindent
set nowrap
set ignorecase
set smartcase
set noswapfile
set nobackup
set undodir=~/.nvim/undodir
set undofile
set incsearch
set scrolloff=999
set signcolumn=yes
set termguicolors
set ve+=onemore
set t_Co=256
set cursorline
set cursorcolumn
set splitright
set splitbelow
set noimd

"korean related settings
set fileencodings=ucs-bom,utf-8,euc-kr,latin1
set fileencoding=euc-kr
"set encoding=euc-kr



let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync <bar> source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')
Plug 'nvim-telescope/telescope.nvim'
Plug 'gruvbox-community/gruvbox' 
Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'pbrisbin/vim-colors-off'
Plug 'sainnhe/everforest'
Plug 'junegunn/seoul256.vim'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'neoclide/coc.nvim'
Plug 'jiangmiao/auto-pairs'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'
Plug 'mzlogin/vim-markdown-toc'
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install' }
Plug 'logico/typewriter-vim'
Plug 'tanvirtin/monokai.nvim'
Plug 'fatih/vim-go', { 'tag': '*'  }
Plug 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim'  }
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'ap/vim-css-color'

call plug#end()

" use <tab> for trigger completion and navigate to the next complete item
function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()

inoremap <expr> <Tab> coc#pum#visible() ? coc#pum#next(1) : "\<Tab>"
inoremap <expr> <S-Tab> coc#pum#visible() ? coc#pum#prev(1) : "\<S-Tab>"

let g:seoul256_background = 235
colo seoul256


let g:airline_theme='zenburn'

"split navigation
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

inoremap <C-a> <Esc>:set wrap <bar> Limelight <bar> Goyo<CR>
nnoremap <C-a> <Esc>:set wrap <bar> Limelight <bar> Goyo<CR>
inoremap <C-q> <Esc>:set nowrap <bar> Limelight! <bar> Goyo!<CR>
nnoremap <C-q> <Esc>:set nowrap <bar> Limelight! <bar> Goyo!<CR>

inoremap <C-o> <Esc>:e .<CR>
nnoremap <C-o> <Esc>:e .<CR>


nmap <CR> :a<CR><CR>.<CR>
nmap <CR> o<Esc>

nnoremap <C-p> :Files<CR>
nnoremap <C-f> :Files ~<CR>
nnoremap <C-s> :Buffers<CR>


