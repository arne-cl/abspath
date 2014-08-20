abspath
=======

``abspath`` is a command line tool that prints the absolute paths of all given
files. File names can be piped via ``STDIN`` or given as arguments.

Usage
-----

::

    abspath file1.txt path/to/file2.pdf
    abspath Desktop/*
    find . -name *.pdf | abspath

Installation
------------

Installation from PyPI
----------------------

::

    sudo pip install abspath

Installation from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    git clone https://github.com/arne-cl/abspath.git
    cd abspath
    sudo python setup.py install

License
-------

3-clause BSD.
