.. _data_part_2:

Data Part 2
###########

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - ZIP Archive `data_2.tar.gz <https://sites.ecmwf.int/repository/metview/test-data/tutorial/data_and_vis/data_2.tar.gz>`_
    - Sep 15, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Introduction
************

Metview has much functionality for meteorological data types stored in ECMWF's MARS archive, for example GRIB, BUFR and ODB. But not all data comes in these formats. 
Therefore Metview has facilities to handle various other data types, which we will explore here.

Visualiser Icons
================

Some formats, such as GRIB, are easy to visualise in Metview - just right-click, **Visualise**. 
This is because they are quite constrained in their contents and have enough standardised meta-data for a program to understand how they should be plotted. 
Some other formats, such as netCDF and tables of ASCII data are not easily interpreted for automatic plotting (which variables/columns should be selected and what do they represent?). 
Metview introduces the concept of the *Visualiser icon*, which we will use in some of the following examples.

NetCDF
******

`NetCDF <http://www.unidata.ucar.edu/software/netcdf/>`_ is a binary file format for storing multi-dimensional arrays of data and enjoys wide academic usage.

Examining netCDF
================

.. image:: /_static/data_part_2/netcdf-examiner.png

Right-click on the supplied *fc_12.nc* icon and choose **examine** to see its structure. 
It consists of multi-dimensional variables, each of which has its own set of attributes; the file also has a set of global attributes. 
The actual fields are t2m and d2m - find their ``long_name`` attributes to see what these represent.

Visualising netCDF
==================

.. image:: /_static/data_part_2/netcdf-visualiser-plot.png

Create a new *NetCDF Visualiser* icon. 
Edit it and drop the *netcdf.nc* icon into the **NetCDF Data** field. 
Set the following parameters:

.. list-table::

  * - **Netcdf Plot Type**
    - Geo Matrix

  * - **Netcdf Latitude Variable**
    - latitude

  * - **Netcdf Longitude Variable**
    - longitude

  * - **Netcdf Value Variable**
    - t2m

Save the changes, and **visualise** this new icon. 
See how the settings in the visualiser icon correspond to the variable names in the data. 
Now visualise another field from the same file. 
Use the supplied *shading_20_levels* icon on the plots.

Extracting netCDF meta-data
===========================

Write the following code into a new *Macro* (you can exclude the comments):

.. code-block:: python

  # read the netCDF file and print its list of variables
  nc = read("fc_12.nc")
  vars = variables(nc)
  print(vars)   #  we could also do:  print(variables(nc))
 
  # set the current variable to be t2m and print its attributes
  setcurrent(nc, 't2m')
  atts = attributes(nc)
  print(atts)

Run the macro - this is what it should print::

  [longitude,latitude,time,t2m,d2m]
  ATTRIBUTES(scale_factor:0.001611,add_offset:254.569370,missing_value:-32767,units:K,long_name:2 metre temperature)

The :func:`variables` function returns a *list* of all the variable names in the netCDF file.

Most of the netCDF functions work on the *current* variable, set in the :func:`setcurrent` function. 
The :func:`attributes` function returns a *definition* - a set of named members, similar to a Python dictionary, relevant to the current variable. 
A definition's elements can be accessed either using the 'dot' operator, e.g. ``atts.units``,  or using indexing notation, e.g. ``atts["units"]``.

.. image:: /_static/data_part_2/netcdf-title-from-attrs.png

Adapt this macro so that it plots the t2m field and gives it a title based on its ``long_name`` attribute. 
Here are some hints:

* drop your *NetCDF Visualiser* icon into the Macro Editor

* also drop the *Contouring* icon

* create a *Text Plotting* icon and enter a random title string, then drop this into the Macro Editor

* replace the value to the right of ``text_line_1`` with the value of the long_name attribute

* add a :func:`plot` command which contains the *NetCDF Visualiser* variable, the *Contouring* variable and the *Text Plotting* variable

* feel free to add the units attribute to the title as well, using the ampersand operator & to concatenate parts of the string

Computations on netCDF data
===========================

Simple computations between netCDFs can be performed in a similar way to fieldsets, but they are only performed on the *current variable* for each netCDF. 
The folder contains two netCDF files: ``fc_12.nc`` and ``fc_36.nc``, representing a 12-hour and a 36-hour forecast valid at the same time. 
Write a small macro which reads both files, sets their current variable to ``t2m`` and computes the difference. 
The last line should look something like:

.. code-block:: python

  diff = fc_36 - fc_12
  
The variable ``diff`` is also a netCDF variable - confirm with this line: "``print(type(diff))``". 
Its contents should be identical to the first netCDF in the computation (``fc_36``), but with the values of its ``t2m`` variable updated to be the differences between the two fields. 
Adapt some of the code from the previous exercise to plot the difference field (and use the supplied *Contouring* icons *pos_shade* and *neg_shade*).

Note that in these netCDF files, the data values are *scaled* in the netCDF file. 
The actual values for the ``t2m`` variable are encoded as 16-bit integers, but they have ``scale_factor`` and ``add_offset`` attributes which Metview applies by default.

.. image:: /_static/data_part_2/netcdf-examiner2.png

We can see this by extracting the values. 
Try the following macro, which will print the 'real world' values from ``t2m``:

.. code-block:: python

  # read the netCDF file
  nc = read("fc_12.nc")
 
  # set the current variable to be t2m and print its values
  setcurrent(nc, 't2m')
  vals = values(nc)
  print(vals)
  print('max: ', maxvalue(vals))
  print('min: ', minvalue(vals))

Now add the following line *before* the call to :func:`values` :

.. code-block:: python

  netcdf_auto_scale_values(0) # 1 means 'on', 0 means 'off'
  
Now the results should look different and will reflect the values as they are packed in the file.

Try something similar with the ``time`` variable:

.. code-block:: python

  # select time as the current variable and print its values
  setcurrent(nc, 'time')
  times = values(nc)
  print(times)

The result is a list of date variables. 
These will be explained in more detail in the session :ref:`Handling Time in Metview  <handling_time_in_metview>`.

To get the "packed" values for this variable, put this line before the call to :func:`values` :

.. code-block:: python

  netcdf_auto_translate_times(0)  # 1 means 'on', 0 means 'off'

ASCII Data
**********

ASCII Table Data
================

Metview incorporates functionality to read, process and visualise data stored in ASCII table files, including the commonly-used CSV (comma-separated value) format.

Visualising ASCII table data
----------------------------

Look at the supplied file ``t2_20120304_1400_1200.csv``. 
This is a standard CSV file, with a header row at the top, followed by one row per observation, one column per field.

::

  Station,Lat,Lon,T2m

  1,71.1,28.23,271.3

  2,70.93,-8.67,274.7

  . . .

A CSV file can have any number of columns, but this is a simple example.

To plot the data, we need to tell Metview which columns contain the coordinates and which contain the values. 
Create a new *Table Visualiser* icon and edit it. 
Drop the CSV icon into the **Table Data** field and set the following parameters:

.. list-table::

  * - **Table Plot Type**
    - Geo Points

  * - **Table Longitude Variable**
    - Lon

  * - **Table Latitude Variable**
    - Lat

  * - **Table Value Variable**
    - T2m

Notice that this icon contains several parameters at the bottom which allow you to read differently-formatted ASCII table files. 
The question-mark buttons beside the parameter names give brief information on what they mean. 
The defaults are set up to read a standard CSV file, so we don't need to touch these parameters in this example.

Visualise this icon to plot the data, and apply the supplied *symb_colours* icon to get a nicer plot.

Converting ASCII Table data to geopoints format
-----------------------------------------------

Although Metview has some functionality for handling this type of data in Macro, it can do much more with the :class:`Geopoints` format. 
Therefore, if the data points are in geographic coordinates, one useful exercise is to read one of these files and convert it to geopoints.

Create a new *Table Reader* icon - this is purely a helper icon which exists only to aid the generation of Macro code. 
Drop the CSV file into the **Data** field. 
We do not need to touch the other parameters since this is a standard CSV file.

Drop the icon into a new Macro to generate the code to read the file. 
Rename the resulting variable to data. 
The following lines of code will print some information about the data:

.. code-block:: python

  print('Num cols: ', count(data))
  print('Col 4: ', name(data, 4))

Now we will create a new geopoints variable, and set its lats, lons and values to those from the CSV data.

First, use the :func:`values` function to extract arrays of lats, lons and T2m from the CSV data. 
These will be returned in variables of type :ref:`vector <macro_vector>` - this is an in-memory array of double-precision numbers.

.. code-block::

  vector or list values( table, number )
  vector or list values( table, string )

Returns the given column specified either by an index (starting at 1) or a name (only valid if the table has a header row). 
If the column type is number, a vector is returned; if it is string, then a list of strings is returned. 
If the column cannot be found, an error message is generated.

Next, find out how many values there are, using the :func:`count` function on one of the returned vectors.

Finally, the following code shows how to construct a simple geopoints variable using only these columns (i.e. it will be in XYV format):

.. code-block:: python

  geo = create_geo(num_vals, 'xyv')
  geo = set_latitudes (geo, lats)
  geo = set_longitudes(geo, lons)
  geo = set_values    (geo, vals)

The macro can now write this to disk, return it to the user interface or process it further using all the available geopoints functions.

ASCII Lat / Lon Matrices
========================

Have a look at the supplied *Lat Lon Matrix* file with the **edit** action. 
This is a simple text format for storing regularly-spaced geographical matrix data, which Metview can directly import. 
As soon as you do anything with this file (e.g. **visualise** or **examine**), Metview internally converts it into GRIB format (leaving the original file untouched). 
In this way, we can import such data into Metview and have access to all its GRIB/fieldset functionality.

Reading/Writing General ASCII Data to/from Disk
===============================================

ASCII files that are not in *Geopoints*, *ASCII Table* or *Lat/Long Matrix* format can be read using the :ref:`read() <read_fn>` function. 
It will return a list of strings - one string will contain the contents of one line of the file. 
Look at the supplied text file, *params.txt*, and see that it contains a list of codes for meteorological parameters:

.. code-block::

  Parameters:
  Z/T/U/V/RH

Create a new *Macro* and type the following code to read and parse this data:

.. code-block:: python

  lines = read('params.txt')
  print(lines) # lines is a list of strings
 
  params = lines[2] # take the second line; params is a string
  param_list = parse(params, '/') # split the string into a list of strings
  print(param_list)

There are many more :ref:`string functions <macro_string_fn>` available.

Now do the reverse: write this list of parameters into another text file. 
The new file should look exactly like the original. 
Here are some hints:

* the :func:`write` function always takes a filename as its first argument, and it can take a string as its second argument

* it always overwrites an existing file of the same name, so there exists another function, append() which will add your string to a new line on an existing file

* so you will need to call :func:`write` once with the first line of text, and :func:`append` once with the list of parameters

* the list of parameters will need to be flattened out into a string with '/' as the separator - this will need to be done in a loop with a string variable initialised to '', and each element added with the ``&`` operator

* the global variable ``newline`` can be used to add a newline character between the lines

ODB
***

.. image:: /_static/data_part_2/odb-plot.png

*ODB* stands for **Observational DataBase** and is developed at ECMWF to manage very large observational data volumes through the ECMWF IFS/4DVAR-system. 
The data structure of an ODB database can be seen as a table of variables called columns. 
Right-click **examine** the *ODB Database* icon *AMSUA.odb* to see a list of the variables in the data. 
The **Data** tab provides access to the actual data itself. 
ODB data can be filtered using ODB/SQL queries. 
The supplied :ref:`ODB Filter <odb_filter_icon>` icon contains an ODB/SQL query to retrieve certain columns of data. 
Edit it - note that this pre-prepared icon is using the *AMSUA.odb* icon as its data input. 
Look at the **ODB Query** field to get an idea of what data will be filtered. 
Now close the editor and **examine** the icon to see the filtered subset of data it has produced. 
The :ref:`ODB Visualiser <odb_visualiser_icon>` icon *tb_plot* tells Metview which columns of data to use for the visualisation; visualise it and apply the symb_colours icon to obtain a nice plot.

There is a dedicated tutorial for handling ODB data in Metview on the :ref:`Tutorials <tutorials>` page.

Extra Work
**********

NetCDF
======

Modify your first netCDF macro which plots the ``t2m`` variable and make it compute the temperature in degrees Celcius by subtracting 273.15 from it before plotting.

Optimisations to file writing
=============================

The last ASCII example could be made more optimal, which could be important if dealing with large amounts of data:

* in fact, it could be done with a single :func:`write` function if we just build up a string representing the whole file with ``newline`` characters between lines

* if writing many many lines, there is another syntax which avoids multiple file open and close operations:

  .. code-block:: python

    fh = file('output.txt')  # open a file handle
    for i = 1 to 100 do
      write(fh, 'Line ' & i & newline)
    end for
    fh = 0 # close the file handle

ODB
===

Visualise different columns of data in the supplied ODB file.

See if you can write a macro which extracts lat, lon and value columns into vectors and creates a new geopoints variable from the data.
