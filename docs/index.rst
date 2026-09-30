.. MyMatlabPackage documentation master file
   This file should be placed at docs/index.rst, alongside conf.py

MyMatlabPackage Documentation
==============================

Welcome to the documentation for **MyMatlabPackage**, a MATLAB package
auto-documented with `sphinxcontrib-matlabdomain
<https://github.com/sphinx-contrib/matlabdomain>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------

This documentation is generated directly from the MATLAB source tree
located at ``../src`` (see ``matlab_src_dir`` in ``conf.py``). Any
public function, class, or package member is scraped automatically
from its leading MATLAB help-text comment block.

Functions: Loose function files in the src directory
----------------------------------------------------

.. currentmodule:: .

.. autofunction:: maxOdd

.. autofunction:: processModel

Package: demopackage
--------------------

.. automodule:: demopackage
   :members:
   :undoc-members:
   :show-inheritance:

Class Folder: ClassFolder
--------------------------

We do not have them in this repo, but if we did, this is how we
document the class folder, i.e. one called `@ClassFolder`

.. autoclass:: ClassFolder
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
