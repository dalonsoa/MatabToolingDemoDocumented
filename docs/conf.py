"""
Example Sphinx conf.py for auto-documenting a MATLAB package
using sphinxcontrib-matlabdomain, ready to deploy on Read the Docs.

Assumed project layout:
    myproject/
    ├── docs/
    │   ├── conf.py          <- this file
    │   ├── index.rst
    │   └── requirements.txt <- must contain: sphinxcontrib-matlabdomain
    └── src/                 <- your MATLAB source tree
        ├── +mypkg/
        │   ├── func.m
        │   └── ClassA.m
        └── @ClassFolder/
            └── ClassFolder.m
"""

import os

# -- Project information -----------------------------------------------
project = "MyMatlabPackage"
author = "Your Name"
release = "1.0.0"

# -- General configuration ------------------------------------------------
extensions = [
    "sphinxcontrib.matlab",   # MATLAB domain + autodoc support
    "sphinx.ext.autodoc",     # required alongside matlabdomain
    "sphinx.ext.napoleon",    # optional: Google/NumPy style docstrings
]

# Treat MATLAB as the default domain so you don't need the "mat:" prefix
primary_domain = "mat"

# Path to the root of your MATLAB source tree (absolute or relative to docs/)
matlab_src_dir = os.path.abspath("../src")

# Optional style tweaks (uncomment as desired)
# matlab_short_links = True          # cleaner MATLAB-like names e.g. ClassA vs mypkg.ClassA
# matlab_auto_link = "basic"         # auto-hyperlink "See also" references
# matlab_keep_package_prefix = False # hide the '+' prefix in rendered output
matlab_show_property_specs = True   # raw arguments-block validators (size/class constraints) displayed alongside the docstring-derived types

html_theme = "sphinx_rtd_theme"  # matches the Read the Docs look & feel

# -- index.rst example content ------------------------------------------
# .. automodule:: mypkg
#    :members:
#
# .. autoclass:: ClassA
#    :members:
#    :show-inheritance:
#
# .. autoclass:: ClassFolder
#    :members:
