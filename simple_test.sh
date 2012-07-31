#!/usr/bin/env sh
echo
echo "python 2"
echo
echo 'table.hl { margin: 2em 0; td.ln { text-align: right; } }' | python2 src/sass.py
echo
python2 src/sass.py -f examples/simple.scss

echo
echo "python 3"
echo
echo 'table.hl { margin: 2em 0; td.ln { text-align: right; } }' | python3 src/sass.py
echo
python3 src/sass.py -f examples/simple.scss

echo
echo "pypy"
echo
echo 'table.hl { margin: 2em 0; td.ln { text-align: right; } }' | pypy src/sass.py
echo
pypy src/sass.py -f examples/simple.scss

