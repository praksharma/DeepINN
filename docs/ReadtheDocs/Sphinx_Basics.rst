Sphinx Tutorial
===============
Click on "View page source" and then click on "Raw" to see the source code.

A subsection
------------

A heading 
**************

A label
-------
.. _label:

*italic text*

**bold text**

``this is a code block``

* bullet 1
    * sub bullet
* bullet 2

#. number 1
#. number 2




.. caution:: 
    This is a caution.

.. danger::
    This is a warning.

.. note::
    This is a note.

.. code-block:: python
    :caption: Code block caption
    :name: This is a name

    import numpy 
    print 'Explicit is better than implicit.'
    import torch
    print(torch.__version__)

Another way::

    import numpy 
    print 'Explicit is better than implicit.'
    import torch
    print(torch.__version__)

``.. images:: https://deepxde.readthedocs.io/en/latest/_images/pinn.png``

Use this link to generate tables:  https://www.tablesgenerator.com/text_tables

.. table:: Table title

    +----+-----+----+-----+----+
    | f  | g   | bv | b   | bc |
    +====+=====+====+=====+====+
    | b  | bc  | b  | c   | c  |
    +----+-----+----+-----+----+
    | g  | d   | b  | b   | b  |
    +----+-----+----+-----+----+
    | fs | fgf | sf | sdf | s  |
    +----+-----+----+-----+----+

Hyperlink relative files. :doc:`/ReadtheDocs/Sphinx_installation` 

Refer relative section: :ref:`this is a label link <label>` 