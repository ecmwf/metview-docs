.. _metview_startup:

Startup options 
==============================

This page only lists a selection of the Metview startup options. To see a more complete list, type

.. code-block:: python

    metview -h


How to
++++++++

Get logging information to the console:

.. code-block:: python

    metview -slog

Change the font size:

.. code-block:: python

    metview -fs <font size> , e.g. metview -fs 16

To run a Macro from the command line:

.. code-block:: python

    metview -b /path/to/macro

To run a Macro and add logging information:

.. code-block:: python

     metview -slog -b /path/to/macro

To quickly bring up the interactive plot window for a given data file:

.. code-block:: python

    metview -p /path/to/grib/bufr/or/geopoints/file
    
    *Note: this will use the default ecCharts style for the given data*


To quickly bring up a data examiner for a given data file:

.. code-block:: python

    metview -e grib|bufr|geopoints|netcdf|odb /path/to/data/file, e.g. metview -e grib /path/to/data.grib

    *Note: Metview 5.10 removes the need to specify the type as an argument*


To start Metview with a home directory different from $HOME/metview

.. code-block:: python
    
    metview -u /path/to/new/home


To obtain useful logging information from the MARS client without setting -slog::

    set the environment variable  METVIEW_MARS_LOG=1 before starting Metview

