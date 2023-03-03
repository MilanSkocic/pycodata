Description
============

Python wrapper around the
`(Modern) Fortran codata library <https://milanskocic.github.io/codata/index.html>`_.
Follow the `installation instructions <https://milanskocic.github.io/codata/md_introduction_install.html>`_.
for compiling and installing the library.

For now,the wrapper must be compiled on Linux, windows and MacOS platforms
after installing the codata library using the compiler that was used to compile your python interpreter.

On Windows 
`Intel Fortran Redistributable <https://www.intel.com/content/www/us/en/developer/articles/tool/compilers-redistributable-libraries-by-version.html>`_ 
and 
`Visual C++ Redistributable for Visual Studio 2015 <https://www.microsoft.com/en-us/download/details.aspx?id=48145>`_
are necessary.

The list of the available constants is available 
`here <https://milanskocic.github.io/codata/md_introduction_raw_codata.html>`_.

The version of the python wrapper follows the versions (major and minor) of the codata library.
The patches will be independent.


How to install
=================

.. literalinclude:: ../../../INSTALL.txt
    :language: python

Dependencies
==============

.. literalinclude:: ../../../requirements.txt

License
==========

.. literalinclude:: ../../../LICENSE.txt