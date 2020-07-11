Installation
============

As a package
------------

Install the extension with:

.. code-block:: shell

    $ pip install sphinxcontrib-platformpicker

Add the extension to the ``conf.py`` file to use it:

.. code-block:: shell

    extensions = ["sphinxcontrib.platformpicker"]


Vendoring
---------

Copy the ``sphinxcontrib`` directory to ``_ext/sphinxcontrib``. Then, declare the extension in the ``conf.py`` file to use it. There are two steps necessary here:

#. Add the ``_ext`` directory to the `Python path`_ using ``sys.path.append``. This should be placed at the top of the file.
#. Update or create the ``extensions`` list and add the extension file name to the list.

For example:

.. code-block:: python

   import sys, os

   sys.path.append(os.path.abspath("./_ext"))

   extensions = ["sphinxcontrib.platformpicker"]

.. _Python path: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
