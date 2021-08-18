# ZSH

- Victim Machine
```python
1. python -c 'import pty; pty.spawn("/bin/bash")'
2. ctrl + z
```
- Attack Machine
```bash
1. stty -a | head -n1 | cut -d ';' -f 2-3 | cut -b2- | sed 's/; /\n/'
2. stty raw -echo; fg (This has to be run as one line on zsh)
```
- Vicitm Machine
```bash
1. reset
2. export TERM=xterm-256color
3. stty rows ROWS cols COLS
```

- Useful if you need to edit with vim, etc.

