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

Bulk Name Generation
~~~~~~~~~~~~~~~~~~~~
If you're generating a large volume of names, the bulk names module will be more
memory intensive, but faster. To use this module, simply replace:

.. code-block:: pycon

    >>> import names

with

.. code-block:: pycon

    >>> import names.bulk as names

and it will cache all of the names into memory, instead of going to the files
for each lookup. For example:

.. code-block:: pycon

    >>> import names.bulk as names
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

.. _mit license: http://th.mit-license.org/2013
.. _available on PyPI: http://pypi.python.org/pypi/names/
