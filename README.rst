abspath
=======

.. image:: http://img.shields.io/pypi/dm/abspath.svg
   :alt: PyPI download counter
   :align: right
   :target: https://pypi.python.org/pypi/abspath#downloads
.. image:: http://img.shields.io/pypi/v/abspath.svg
   :alt: Latest version
   :align: right
   :target: https://pypi.python.org/pypi/abspath
.. image:: http://img.shields.io/badge/license-BSD-yellow.svg
   :alt: BSD License
   :align: right
   :target: http://opensource.org/licenses/BSD-3-Clause


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
~~~~~~~~~~~~~~~~~~~~~~

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
