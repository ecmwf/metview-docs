.. _running_metview_in_batch_mode:

Running Metview in Batch Mode
#############################
  
**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - File `batch.tar.gz <https://confluence.ecmwf.int/download/attachments/45758470/batch.tar.gz?api=v2>`_ 
    - Mar 19, 2015 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_ 

Overview
********

In addition to all its interactive functionality, Metview can be run in a purely batch mode from the command line. 
Of course, in this mode we cannot have an interactive plot window, but we can save plots in various formats (see `Working with graphical output <https://confluence.ecmwf.int/display/METV/Working+with+graphical+output>`_) and we can save computed data into files of various formats (see `Processing Data <https://confluence.ecmwf.int/display/METV/Processing+Data>`_).

Running Metview in Batch Mode
=============================

Metview runs in batch mode when the option ``-b`` is specified when you first call it. 
You can run Metview in batch mode while having a Metview interactive session up and running - they will not interfere with each other. 
To run a macro in batch mode simply specify its name on the command line after the ``-b`` option:
  
.. code-block:: python
  
  % metview -b macro_name [arg1 arg2 ...]
  
where ``macro_name`` is the name of the macro you want to run. 
You can specify a path to the macro if it is not in the current directory.

The ``arguments()`` function returns a list of command-line arguments.
Write a short new Macro which requires a single argument (a meteorological parameter short name such as Z, T or RH) to be passed to it on the command line. 
It should fail if more or less arguments are passed. 
It should print the argument that has been passed to it. 
Useful hints:

* the ``count()`` function returns the number of elements in a list

* the ``fail()`` function takes a string as its argument and will print the string and exit Metview with an error code

Expand the macro to retrieve this parameter from MARS on a 1x1 degree grid. 
The only parameters required to be set in the ``retrieve()`` function are **Parameter** and **Grid**. 
You can use the ``print()`` function to confirm that the fields have been retrieved.

.. note::

  The additional command-line argument ``-slog`` tells Metview to provide more output - this can be useful to diagnose problems. 
  This argument (and indeed all other arguments) must come *before* the ``-b``, and anything after it will be interpreted as an argument to your macro.

Getting Environment Variables
=============================

Environment variables can be queried, not only in batch mode but also in interactive mode. 
This can be an alternative way to pass information to a macro.

In a macro, get the value of a chosen environment variable (e.g. HOST) using the ``getenv()`` function. 
For example:
  
.. code-block:: python
  
  machine = getenv('HOST')
  print('Running on ', machine)
  

Detecting Whether Metview is Running in Batch Mode
==================================================

The macro function ``runmode()`` returns a string which tells us the mode in which it has been run. 
If the return value is "batch" then Metview has been invoked in batch mode.

Add a check to your macro: if it is running in batch mode, then take the parameter from the command line arguments as before; otherwise, set it to some string of your choosing. 
In both cases, the name should be printed. 
Try running the macro in batch mode, and also from the Macro Editor.

If running in interactive mode (i.e. not "batch") then plot the data to an interactive **Display Window**. 
If in batch mode, plot the data to a PostScript file called ``my_field.ps``. 
See `Working with graphical output <https://confluence.ecmwf.int/display/METV/Working+with+graphical+output>`_ for more detail if required.

Invoking Metview's Data Examiners from the Command Line
=======================================================

Metview has a shortcut for invoking the data examiners from the command line for quick data inspection.
Find a GRIB file somewhere in your Metview directory structure (it can also be outside the Metview home directory). From the command-line, type:
  
.. code-block:: python
  
  metview -e grib /path/to/grib
  
This works for GRIB, BUFR, ODB and netCDF files. The file type must be the first argument.

Plotting a Data File from the Command Line
==========================================

For the same GRIB file, from the command-line, type:
  
.. code-block:: python
  
  metview -p /path/to/grib
  
This gives a quick way to plot a file outside the Metview environment. 
The visualisation uses the same settings as ecCharts, so depending on the meteorological parameter you will get different contouring styles.

Extra Work
==========

Take some of the macros you've already written and convert them so that they can run in batch mode. In most cases it will not require much work - here are the main things to consider:

* the macro should be runnable both interactively and in batch mode

* if the macro returns data, it should write it to disk instead

* if the macro plots data, it should generate a graphics file instead

* if the macro has some parameters hard-coded into it, they should become command-line arguments
