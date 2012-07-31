SassPython - bindings for libsass
=================================

why?
----

* the guy on this talk asqued for it: http://www.confreaks.com/videos/859-railsconf2012-the-future-of-sass
* I wanted to play with ctypes

who?
----

marianoguerra

how?
----

first of all download, compile and install libsass::

        git clone https://github.com/hcatlin/libsass.git
        cd libsass
        ./configure
        make
        sudo make install

then you can play with this project in two ways

command line
............

if no options provided read from stdin::

        ➜  src  ./sass.py                           
        table.hl td.ln {
          text-align: right;
        }

        table.hl td.ln {
          text-align: right; }

from a file::

        ➜  src  ./sass.py -f ../examples/simple.scss

        .content-navigation {
          border-color: #3bbfce;
          color: darken(#3bbfce, 9%); }

        .border {
          padding: 8px;
          margin: 8px;
          border-color: #3bbfce; }

from a folder:

.. image:: http://chzscience.files.wordpress.com/2011/11/funny-science-news-experiments-memes-dog-science-fuzzy-logic.jpg

::

        # I think it doesn't work, never used sass before and don't know what
        # this means :)
        ➜  src  ./sass.py -d ../examples/

you can't chew gum and walk at the same time::

        ➜  src  ./sass.py -f ../examples/simple.scss -d ~
        usage: sass.py [-h] [-f FILE_PATH | -d DIR_PATH]
        sass.py: error: argument -d/--dir: not allowed with argument -f/--file

code
....

from a string::

        Python 2.7.3 (default, Apr 20 2012, 22:44:07) 

        >>> import sass
        >>> STYLE = """
        ... table.hl td.ln {
        ...   text-align: right;
        ... }
        ... """

        >>> ok, style = sass.compile(STYLE)

        >>> ok
        True

        >>> print style
        table.hl td.ln {
          text-align: right; }

from a file::

        >>> ok, style = sass.compile_path("../examples/simple.scss")

        >>> ok
        True

        >>> print style
        .content-navigation {
          border-color: #3bbfce;
          color: darken(#3bbfce, 9%); }

        .border {
          padding: 8px;
          margin: 8px;
          border-color: #3bbfce; }

from a folder::

        >>> ok, style = sass.compile_folder("../examples/")
        
        # ???
        # Profit!

how to install?
---------------

from sources
............

python 2::

        sudo python2 setup.py install

python 3::

        sudo python3 setup.py install

using pip
.........

::

        sudo pip install SassPython

license?
--------

MIT + optional beer for the creator

what's left to do?
------------------

* make the folder stuff work
* add command line options to specify option styles
* see what the return value of the compile_* means and use it if needed
