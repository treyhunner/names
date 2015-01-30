names
=====

.. image:: https://secure.travis-ci.org/treyhunner/names.png?branch=master
   :target: http://travis-ci.org/treyhunner/names
.. image:: https://coveralls.io/repos/treyhunner/names/badge.png?branch=master
   :target: https://coveralls.io/r/treyhunner/names
.. image:: https://pypip.in/v/names/badge.png
   :target: https://crate.io/packages/names
.. image:: https://pypip.in/d/names/badge.png
   :target: https://crate.io/packages/names

Random name generator

NOTE: This package was made to demonstrate how easy it is to create a real thing with Python.  Check out the *Related Projects* section for a list of similar projects.


Installation
------------

The script is `available on PyPI`_.  To install with pip::

    pip install names


Usage
-----

Names can be used as a command line utility or imported as a Python package.

Command Line Usage
~~~~~~~~~~~~~~~~~~
To use the script from the command line:

.. code-block:: bash

    $ names
    John Powell

Python Package Usage
~~~~~~~~~~~~~~~~~~~~
Here are examples of all current features:

.. code-block:: pycon

    >>> import names
    >>> names.get_full_name()
    u'Patricia Halford'
    >>> names.get_full_name(gender='male')
    u'Patrick Keating'
    >>> names.get_first_name()
    'Bernard'
    >>> names.get_first_name(gender='female')
    'Christina'
    >>> names.get_last_name()
    'Szczepanek'


License
-------

This project is released under an `MIT License`_.

Data in the following files are public domain (derived from 1990 Census data):

- dist.all.last
- dist.female.first
- dist.male.first


Related Projects
----------------

- `faker`_ is a more mature and full-featured fake data generation package

.. _faker: http://www.joke2k.net/faker/
.. _mit license: http://th.mit-license.org/2013
.. _available on PyPI: http://pypi.python.org/pypi/names/
