.. _install:

************
Installation
************

Binaries and Python Bindings
============================

Metview consists of two parts. The 'binaries' are the core of Metview, incorporating the
user interface, the majority of the data processing code and the Macro programming language.
The Python bindings sit on top of the binaries and provide a powerful Python interface to
Metview's functionality. The binaries can run standalone, and the Python bindings require
the binaries.


Installing Metview's binaries
=============================

The following package managers provide pre-built Metview binaries.
The brew and conda packages are maintained by ECMWF and are generally up to date.

Homebrew
^^^^^^^^

Metview's binaries are available from Homebrew on macOS, including the M1 processors, and Linux
(Linux distribution on brew exists but has not been tested). They are installed like this:

.. code-block:: bash

    brew install metview

Once installed, Metview can be updated with this command:

.. code-block:: bash

    brew upgrade metview


Conda
^^^^^

Metview's binaries are available on conda for both Linux and macOS, including the M1 processors. From a
conda environment, the following command will install Metview:

.. code-block:: bash

    conda install metview  -c conda-forge

Once installed, Metview can be updated with this command:

.. code-block:: bash

    conda update metview  -c conda-forge


There is also a batch-only version of Metview's binaries on conda, called metview-batch. This does not include the graphical user interface and is therefore more lightweight and can be used in environments such as Binder. It does include the ability to produce graphical plots, and they must be generated as files (PNG, PDF, SVG, ...) or as inline plots in Jupyter notebooks.

.. code-block:: bash

    conda install metview-batch  -c conda-forge


Community-built Binary Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Community-built Metview binaries for a number of Linux distributions can be found here:
https://software.opensuse.org/download.html?project=home%3ASStepke&package=Metview

From Ubuntu 16.04, Metview is available from the standard repositories and can be installed like this:

.. code-block:: bash

    sudo apt-get install metview

These packages are not maintained by ECMWF, so any issues with installation should be reported to
their maintainers.



Installing Metview's python interface
=====================================

Metview's Python interface is installed separately. Note: Metview's Python interface requires the binaries
to be present.

Conda
^^^^^

If you are working in a conda environment, then
it is recommended to install via conda:

.. code-block:: bash

    conda install metview-python  -c conda-forge


PyPi
^^^^

If not in a conda environment, then install via pip:

.. code-block:: bash

    pip install metview



Metview Source Releases
============================

See the `Change History <https://confluence.ecmwf.int/display/METV/Change+History>`_ for details
of each release. The source of each Metview version can be found on the
`Releases <https://confluence.ecmwf.int/display/METV/Releases>`_ page.

To build Metview and its ECMWF dependencies in one go, try
`The Metview Source Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`_.

Metview's Python bindings are available on github:
https://github.com/ecmwf/metview-python


Tips on installing Metview into environments
============================================

These small guides are not intended to replace the official documentation on how to create and used
conda environments and virtualenvs, they are just a quick suggested way to get started!

Conda
^^^^^

Conda allows you to install binaries and Python packages into the same environment.
With conda, it's almost always neater to install software into a created environment rather than the
base environment. Here are some suggested steps, assuming that conda itself has been installed:

.. code-block:: bash

   conda create --name myenv
   conda activate myenv
   conda install metview -c conda-forge
   conda install metview-python -c conda-forge

Once this is done, any new shell should call the 'conda activate' command in order to use this Metview.

Virtualenv
^^^^^^^^^^

Virtualenvs provide separate environments in which you can install Python packages. Binaries must be installed
separately using one of the methods described above. For example, it could be a good idea to use Homebrew to install
the binaries and use a virtualenv to install the Python bindings. Here's a quickstart:

.. code-block:: bash

   python3 -m venv $HOME/venvs/myenv
   source $HOME/venvs/myenv/bin/activate
   pip install metview

Once this is done, any new shell should call the above 'source ..../activate' command in order to use these Metview
Python bindings.


Possible Startup Issues
=======================

The Python bindings can be tested for installation correctness by running
the following command:

.. code-block:: bash

   python3 -m metview selfcheck

If your environment has Metview installed or built but it is not in the system PATH,
you can tell the Python bindings where to find it by setting this environment variable to
the path to the 'metview' startup command:

.. code-block:: bash

    export METVIEW_PYTHON_START_CMD=/path/to/build/metview/bin/metview

To activate extra debugging information, set this before starting Python:

.. code-block:: bash

    export METVIEW_PYTHON_DEBUG=1

For more output from MARS requests, set this before starting Python:

.. code-block:: bash

    export METVIEW_MARS_LOG=1

When you import metview, the Metview startup script is run in order to set up the working
environment. Usually this is pretty much instant, but on very heavily loaded machines, it may
take a few seconds. There is a default timeout of 8 seconds, but this can be increased if needed,
by setting the following environment variable, to, for example, 15 seconds:

.. code-block:: bash

    export METVIEW_PYTHON_START_TIMEOUT=15
