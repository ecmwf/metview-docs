Installation
------------

Binaries and Python Bindings
============================

Metview consists of two parts. The 'binaries' are the core of Metview, incorporating the
user interface, the majority of the data processing code and the Macro programming language.
The Python bindings sit on top of the binaries and provide a powerful Python interface to
Metview's functionality. The binaries can run standalone, and the Python bindings require
the binaries.


Metview on conda and PyPi
=========================

These packages are maintained by ECMWF and are generally up to date.

Metview's binaries are available on conda for both Linux and MacOS. From a conda environment, the following command will install Metview without any
need to compile from source:

.. code-block:: bash

    conda install metview  -c conda-forge

Once installed, Metview can be updated with this command:

.. code-block:: bash

    conda update metview  -c conda-forge


There is also a batch-only version of Metview's binaries on conda, called metview-batch. This does not include the graphical user interface and is therefore more lightweight and can be used in environments such as Binder. It does include the ability to produce graphical plots, and they must be generated as files (PNG, PDF, SVG, ...) or as inline plots in Jupyter notebooks.

.. code-block:: bash

    conda install metview-batch  -c conda-forge

Metview's Python interface is installed separately. If you are working in a conda environment, then
it is recommended to install via conda:

.. code-block:: bash

    conda install metview-python  -c conda-forge

If not in a conda environment, then install via pip:

.. code-block:: bash

    pip install metview


Community-built Binary Packages
==================================

Community-built Metview binaries for a number of Linux distributions can be found here:
https://software.opensuse.org/download.html?project=home%3ASStepke&package=Metview

From Ubuntu 16.04, Metview is available from the standard repositories and can be installed like this:

.. code-block:: bash

    sudo apt-get install metview

These packages are not maintained by ECMWF, so any issues with installation should be reported to
their maintainers.

Metview Source Releases
============================

See the `Change History <https://confluence.ecmwf.int/display/METV/Change+History>`_ for details
of each release. The source of each Metview version can be found on the
`Releases <https://confluence.ecmwf.int/display/METV/Releases>`_ page.

To build Metview and its ECMWF dependencies in one go, try
`The Metview Source Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`_.

Metview's Python bindings are available on github:
https://github.com/ecmwf/metview-python


Possible Startup Issues
=======================

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
