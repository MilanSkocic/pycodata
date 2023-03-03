Description
============

Python wrapper around the
`(Modern) Fortran codata library <https://milanskocic.github.io/codata/index.html>`_.
Follow the `installation instructions <https://milanskocic.github.io/codata/md_introduction_install.html>`_.
for compiling and installing the library.

The wrapper must be compiled on Linux and MacOS platforms after installing the codata library.
The compilation of the wrapper is trivial on those platforms and 
it should work with every C compiler as long as the codata library was compiled and installed 
with all paths set properly.

The wrapper can also be compiled on Windows with the Intel Fortran compiler and MSVC. 
Binaries for 64bit architectures are provided on `pypi <https://pypi.org/project/pycodata/>`_.
On Windows `Intel Fortran Redistributable <https://www.intel.com/content/www/us/en/developer/articles/tool/compilers-redistributable-libraries-by-version.html>`_ 
are necessary.

The list of the available constants is available 
`here <https://milanskocic.github.io/codata/md_introduction_raw_codata.html>`_.

The version of the python wrapper follows the versions (major and minor) of the codata library.
The patches will be independent.

Installation
===================
See  ``INSTALL.txt``.

Dependencies
================

See ``requirements.txt``.


License information
===========================
See ``LICENSE.txt``.