.. _graph_plotting_in_metview:

Graph Plotting in Metview
#########################

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - ZIP Archive `graph.tar.gz <https://confluence.ecmwf.int/download/attachments/46596114/graph.tar.gz?api=v2>`_
    - Sep 16, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Overview
********

In addition to geographic map plots, Metview can also generate XY plots including time series.
The possible ways to provide data for graph plotting are:

* :ref:`Input Visualiser  <input_visualiser_icon>`

* :ref:`Table Visualiser <table_visualiser_icon>`

* :ref:`NetCDF Visualiser <netcdf_visualiser_icon>`

* :ref:`ODB Visualiser <odb_visualiser_icon>`

The coordinate system is defined by the :ref:`Cartesian View <cartesianview_icon>` icon, the visual appearance of the axes by the :ref:`Axis Plotting <maxis_icon>` icons and the title by the :ref:`Text Plotting <mtext_icon>` icon. The data points themselves can be modified with the :ref:`Symbol Plotting <msymb_icon>` (for points) and :ref:`Graph Plotting <mgraph_icon>` (for lines) icons.

A Simple Graph
**************

.. image:: /_static/graph_plotting_in_metview/simple-graph.png

Create a new *Input Visualiser* icon. 
Set **Input Plot Type** to XYPoints and type a list of values (forward slash-delimited) for both **Input X Values** and **Input Y Values** (they should have the same number of elements). 
So the first number from **Input X Values** together with the first number from Input Y Values form one point in the graph, and so on.

Visualise the icon to get a basic plot of the data. 
You can drop a customised *Symbol Plotting* icon into the **Display Window** to change the numbers into markers. 
If you wish to have a plot where the individual points are coloured according to some value, set **Input Values** to a list of numbers. 
Then an appropriate *Symbol Plotting* icon will colour the markers.

Also try dropping a *Graph Plotting* icon to get connecting lines between the points. 
Try changing the plot type to a bar chart using the *Graph Plotting* icon.

Notice that the automatically-generated view fits your data so that the 'edge points' are on the axes.

Customising the view
====================

.. image:: /_static/graph_plotting_in_metview/simple-graph-with-cview.png

Now that we have a simple plot, we can make it more professional.

Create a new *Cartesian View* icon. 
Ensure that **X Automatic** and **Y Automatic** are set to Off, then set **X Min**, **X Max**, **Y Min** and **Y Max** so that they provide some space around your data points. 
Visualise the icon and drop your *Input Visualiser* into the **Display Window** to see the result.

Customising the axes
====================

.. image:: /_static/graph_plotting_in_metview/simple-graph-with-axes.png

Create a new *Axis Plotting* icon and rename it *h_axis*. 
Try modifying it to produce a horizontal axis similar to the one shown (change the title, the font sizes and the line thickness). Just drop it into the **Display Window** to test it.

Now create another one called *v_axis* and make it the vertical axis:

.. list-table::

  * - **Axis Orientation**
    - Vertical

Customise this similarly.

You can bind the axis icons to the view icon by dropping them into the **Horizontal Axis** and **Vertical Axis** parameter boxes in the *Cartesian View* icon editor. 
Now when you visualise this view icon, it will have your customised axes.

Add a title
===========

.. image:: /_static/graph_plotting_in_metview/simple-graph-with-title-and-bars.png

We will look in more detail at plot titles, but for now just create a new *Text Plotting* icon and set **Text Line 1** to a suitable title for your plot; drop it into the **Display Window** to apply it. 
The above plot also shows the data plotted as a bar chart via the *Graph Plotting* icon.

Putting it into a macro
=======================

Now drop the *Cartesian View* icon into the editor of a new *Macro* icon - the *Axis* icon definitions will be automatically included. 
Do the same with the other icons and add a :func:`plot` command, remembering that the view should be the first argument, followed by a data variable, followed by any visdefs to be applied to it.

Now make it more robust to changing data by computing the **X Min**, etc extents of the view to be 10% less and more than the min and max data values. These are the steps:

* put the lists of x and y values into *list* variables at the top of the macro and use these variables in the :func:`cartesianview` call

* to find the minimum value from a list, we need to convert it into a *vector* variable, then use the :func:`minvalue` function on the new vector

  * hint: ``min_x = minvalue(vector(x_values))``

* similarly for the maximum

* we need to do this for min and max of both x and y variables to get what we need to set **X Min**, **X Max**, **Y Min** and **Y Max** correctly

* now adjust each value by 10%

You should now be able to change the data values at the top of the macro, and the plot should still look ok.

Plotting a Time Series
**********************

.. image:: /_static/graph_plotting_in_metview/time-series-chart.png

We will now extract data values from a particular location for different times and plot as a time series graph. 
It will be a Macro-based exercise, so create a new *Macro* icon, rename it *time_series* and go through the steps below.

Extract the location values from the data
=========================================

Inspect the supplied *t2m_forecast_24.grib* icon - this contains a 24-hour forecast for a number of time steps.

Read the data into a *fieldset* variable and extract the point values into a list with code similar to this:

.. code-block:: python

  lat = 51
  lon = 1
  fs = read("t2m_forecast_24.grib")
  vals = nearest_gridpoint(fs, lat, lon)
  print(vals)

This will return a list of values, one for each field.

Now extract the dates and times of the fields and combine them into a list of *date* variables.

.. code-block:: python

  dates = valid_date(fs)
  print(dates)

Now construct an *Input Visualiser* icon which you will drop into the Macro Editor: ensure that the **Input X Type** is set to type **Date** and enter some dummy values so that useful Macro code generated. 
In the macro, replace the values of ``input_date_x_values`` and ``input_y_values`` with your lists of data. 

In your macro, plot the *Input Visualiser* variable to get your time series plot. 
Use the Macro code for a *Graph Plotting* icon to connect the points with blue lines. 
If you have time at the end, you can customise the plot further.

Now duplicate the bulk of the code (change some variable names!) in order to additionally plot the time series for the data stored in *t2m_analysis.grib*, with the points connected by red lines. 
The plotting part can be done either with an additional :func:`plot` command, or else by adding the new *Input Visualiser* and *Graph Plotting* code to the end of the existing :func:`plot` command.

.. note::

  In :ref:`Organising Macros <organising_macros>` we will see how to put similar code into functions in order to reduce duplication of code.

Plotting onto a Map
*******************

.. image:: /_static/graph_plotting_in_metview/geolines.png

All of the icons (and their Macro equivalent functions) which plot graph data to an X/Y (Cartesian) axis can also plot graph data onto a map using lat/lon coordinates. As an example, we will plot a box which bounds a simple geographical region.

We will do this in two different ways; first, using the *Input Visualiser*.

Marking an area using *Input Visualiser*
======================================

Create a new Input *Visualiser* icon and set **Input Plot Type** to Geo Points. 
We want to define 4 lines, therefore we need a list of 5 points to connect together in order to create a closed box.

You can choose your own coordinates, or use these: top latitude = 65, bottom latitude = 51, left longitude = -5, right longitude = 26. 
Set **Input Longitude Values** and **Input Latitude Values** to each be a list of 5 numbers which will describe the four corners (and repeat the first). 
When you drop a *Graph Plotting* icon into the plot, the points should be connected into a rectangle (if this is not the case, check the ordering of your points!). 
This can be a simple way or marking an area on a map. You can have as many points as you wish, and therefore have more complex polygons. 
You could also read polygons from a file and plot them on the map using some Macro code - an example of this will be see in :ref:`Case study: Plotting the Track of Hurricane Sandy  <case_study_plotting_the_track_of_hurricane_sandy>`.

Depending on what you want, this method has a limitation - the lines do not follow the projection of the view; they are just straight lines on the screen (see the images above). 
This is fine in cylindrical projection, but not in many others. 
Try plotting the lines in a polar stereographic *Geographical View*.

Marking an area using mvl_geoline
=================================

Macro has a function called :func:`mvl_geoline` which simply splits a geographic line into smaller parts which will follow any view projection.

::

  definition mvl_geoline(lat1 : number, lon1 : number, lat2 : number, lon2 : number,  incrm : number)

    The first four parameters define the end-points of the line. 
    Parameter incrm specifies the increment, in degrees, into which the line should be split.

Create a new *Macro* icon and set up the coordinates of the box, for example:

.. code-block:: python

  toplat   = 65
  botlat   = 51
  leftlon  = -5
  rightlon = 26

Define the first line of the box like this:

.. code-block:: python

  increment = 0.1
  line1 = mvl_geoline(toplat, leftlon,  toplat, rightlon, increment)

Now finish off the box with the remaining 3 lines. 
They can then all be put into the :func:`plot` command like this, with an optional *Graph Plotting* visdef defined somewhere in the macro:

.. code-block:: python

  plot(line1, line2, line3, line4, red_line)

Run the macro and drop a polar stereographic view into the Display Window to see the difference from the previous version.

An alternative is to combine the lines into a list before passing it to the :func:`plot` command:

.. code-block:: python

  to_plot = [line1, line2, line3, line4]
  plot(to_plot, red_line)

Extra Work
**********

Customise the time series plot:
===============================

.. image:: /_static/graph_plotting_in_metview/time-series-extra.png

* put some extra space around the data points - add a day to each end of the x axis using a custom *Cartesian View*

* add a useful legend indicating that the blue line is the 24h forecast data and the red line is the analysis data

Logarithmic scales
==================

.. image:: /_static/graph_plotting_in_metview/simple-graph-with-log-y-cview.png

Create an X/Y plot similar to the first one from this session. 
Make sure there are some large y-values (e.g. 100, 1000). 
Set up a *Cartesian View* icon with **Y Axis Type** = Logarithmic to view your data differently. 
Logarithmic Y axes are often used when representing the atmospheric levels.

Scatterplot
===========

.. image:: /_static/graph_plotting_in_metview/fc-vs-an-graph-plot.png

Plot the analysis values on the x-axis and the forecast values on the y-axis. 
Add a diagonal line.

Geo boxes side-by-side
======================

Write a macro which creates a 2-page layout similar to the image under "Plotting onto a Map". 
Use the two different box-drawing techniques, one in each page. Ensure they use the same variables to define the bounds of the box.
