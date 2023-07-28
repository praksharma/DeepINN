Use Markdown in Sphinx
======================

We can use the markdown language, which is easy and has quiate a lot of online GUI tools to save our time. Moreover, Jupyter Lab also has a markdown editor.

First of all, install this package.

.. code-block:: bash

    $ pip install myst-parser

In the ``/docs/conf.py`` add the follwoing:

.. code-block:: bash

    extensions = ['myst_parser']

This will activate the MyST Parser extension, causing all documents with the .md extension to be parsed as MyST.