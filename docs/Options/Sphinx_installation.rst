Sphinx Installation
===============

`Here <https://docs.readthedocs.io/en/stable/tutorial/>`_ is a nice tutorial about Read the Docs.

Use this command to install Sphinx:

.. code-block:: bash

    $ pip install sphinx

Now make a new directory inside your Github repo named ``/docs``.

.. code-block:: bash

    $ mkdir docs
    $ cd docs

Use ``sphinx-quickstart`` to setup a basics documentation generator. This creates ``index.rst`` and ``conf.py`` inside the ``/docs`` directory.

.. code-block:: bash

    $ sphinx-quickstart

Now use ``make html`` with the ``/docs`` as ``pwd`` to generate ``index.html``.

.. code-block:: bash

    $ make html

Now manually open ``/docs/_build/html/index.html`` to view the created documentation.

Apply Read the Docs theme
-------------------------

In ``/docs/conf.py`` add the following:

.. code-block:: bash

    html_theme = 'sphinx_rtd_theme'