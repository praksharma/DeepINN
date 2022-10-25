Section
=======

subsection
------

just a heading 
**************

hello
-----
.. _label:

*italic*
**bold**

``this is a code``

* bullet 1
    * sub bullet
* bullet 2

#. number 1
#. number 2




.. caution:: 
    Do not use Windows.

.. danger::
    delete system32

.. note::
    use apptainer on HPC

.. code-block:: python
    :caption: how to cook python
    :name: this is a name

    import numpy 
    print 'Explicit is better than implicit.'
    import torch
    print(torch.__version__)

Another way::

    import numpy 
    print 'Explicit is better than implicit.'
    import torch
    print(torch.__version__)

.. images:: https://deepxde.readthedocs.io/en/latest/_images/pinn.png

use this link to generate tables:  https://www.tablesgenerator.com/text_tables

.. table:: table title

    +----+-----+----+-----+----+
    | f  | g   | bv | b   | bc |
    +====+=====+====+=====+====+
    | b  | bc  | b  | c   | c  |
    +----+-----+----+-----+----+
    | g  | d   | b  | b   | b  |
    +----+-----+----+-----+----+
    | fs | fgf | sf | sdf | s  |
    +----+-----+----+-----+----+

Hyperlink relative files. :doc:`/Options/demo2` 

refer relative section: :ref:`this is a label link <label>` 