.. _handling_time_in_metview:

Handling Time in Metview
########################

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - File `time.tar.gz <https://get.ecmwf.int/repository/test-data/metview/tutorial/data_and_vis/time.tar.gz>`_
    - Mar 19, 2015 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Time
****

Time is a very important dimension in meteorology, and there are many things to keep in mind. 
Here we will explore how Metview handles this dimension.

Overlaying Time Steps
=====================

.. image:: /_static/handling_time_in_metview/overlay-geop-fields.png

Inspect the supplied GRIB files: *z500_fc.grib* contains geopotential forecasts made in one run, but for six different forecast steps; *z500_an.grib* contains analysis fields for two times. 
Visualise the supplied *Geographical View* icon and drop the forecast GRIB icon **together** with its corresponding *Contouring* icon (*cont_fc*) into the **Display Window**, and then drop the analysis GRIB icon **together** with its corresponding *Contouring* icon (*cont_an*) too. 
Go through the frames of animation. The fields have been overlaid, but if you look at the times and dates in the title, you will see that they do not match. 
Metview has simply plotted the first field of each data file together, then the second, and so on. 
We can make it more intelligent.

Edit the Geographical View icon and set this:

.. list-table::

  * - **Map Overlay Control**
    - By Date

Save the icon, visualise it and drop the data with their visdefs in again. 
Go through the animation steps and look at the **Frames** tab in the **Display Window** to see what has happened. 
Now the fields will be overlaid *only if their valid date and time match*.

Metview's overlay rules
=======================

To summarise, Metview's overlay rules can be described like this:

.. note::

  **Rule 1**
  
  Multiple data contained in a single icon or file (data unit) are never overlaid.

In practice, this means that a GRIB file with 5 fields is visualised as 5 separate plots which you can scroll through.

If you wish to overlay data, then you must provide separate data icons for each 'layer'. 
Then we are subject to Rule 2:

.. note::

  **Rule 2**
  
  Multiple data provided in several data icons are overlaid according to the overlay setting in the current view.

Precipitation
*************

.. image:: /_static/handling_time_in_metview/computed-precip.png

Precipitation data provides an interesting challenge. 
Precipitation fields in MARS are stored as *accumulated* fields. 
Visualise the supplied *precip.grib* icon with the *precip_shade* visdef. 
The first field is empty (check using the Cursor Data). 
The first field has a step of 0, meaning that it contains the total precipitation accumulated between the run time and the run time plus step. 
Since these are the same, there is no accumulated precipitation! 
Subsequent steps show more and more precipitation (the amount accumulated over 3, 6, 9, etc hours).

What if we want to plot just the rain that accumulated between 06:00 and 09:00? 
That would be the accumulated precip at 09:00 minus the accumulated precip at 06:00. 
We can compute this in a macro.

Create a new Macro icon and rename it *compute_precip*.

We can see from examining the file that the 6 and 9 o'clock  steps are fields 3 and 4 respectively (using 1-based indexing). So the following macro code will compute the difference and return it:

.. code-block:: python

  precip = read("precip.grib")
 
  precip_6_to_9 = precip[4] - precip[3]
  return precip_6_to_9

Visualise the macro to plot it.

Now we want to go further and compute the precipitation for each and every 3-hour period. 
We can do this with more complex field indexing.

So we want field 2 minus field 1, field 3 minus field 2, etc. 
We can do this in a single line of code because we can handle multiple fields in a single operation as shown:

.. image:: /_static/handling_time_in_metview/fieldset_oper_minus.png

To extract fields 1 to 4, for example, we can use the following syntax:

.. code-block:: python

  fields = precip[1,4]

So the following piece of code will do what we want in a more general way:

.. code-block:: python

  precip = read("precip.grib")
 
  n = count(precip) # the number of fields in the fieldset
  precip_3h = precip[2, n] - precip[1, n-1]
  return precip_3h

Visualise the macro. 
If you drop the precip_shade visdef icon into the plot, it may become blank! 
There is one more trick: we have created a *derived field*, and this changes the automatic scaling algorithm used when plotting. 
Precipitation is stored in metres, but we want to display it in mm. 
Modify the *precip_shade* icon and set:

.. list-table::

  * - **Grib Scaling of Derived Fields**
    - On

Visualise your macro result again and confirm that you now have precipitation only for the 3-hour periods, which does not accumulate with each frame.

Note that the meta-data for each field is taken from the first field in each subtraction; "step9 minus step6" returns a field with meta-data from step9, so be aware of this. 
Macro has :ref:`functions <macro_fieldset_fn>` for setting GRIB meta-data if you need to change it in order to correctly describe the new data.

Dates in Macro
**************

Macro has specific :ref:`date-handling abilities <macro_date_fn>`. Dates are a built-in data type which in fact describe both a date and a time.

Defining dates
==============

You can create date variables in a number of ways:

 * yyyy-mm-dd
 
 * yyyy-DDD  (DDD is a 3-digit Julian day, e.g. 365 is 31st December in non-leap years)

These will have the time set to 00:00. A different time can be added by adding

* HH:MM

* HH:MM:SS

Create a new *Macro* icon, rename it to *dates* and define a date:

.. code-block:: python

  d1 = 2015-03-11
  print(type(d1))
  print(d1)

Try adding a time:

.. code-block:: python

  d1 = 2015-03-11 12:00

Converting numbers into dates
=============================

The ``date()`` function converts numbers into dates using the same syntax that MARS understands. 
For example:

* ``d1 = date(20150105)``

* ``today = date(0)``

* ``yesterday = date(-1)``

This syntax can be useful if reading dates from a text file or some other source.

Again, the time will be 00:00 unless we add it. We can consider the time to be a fraction of a day:

* ``midday = date(20150105.5)``

**Use this syntax to add another variable**, ``d2``, which contains the date and time for 13:00h at 2015-03-13. Print it to check it.

Note that when passing numeric dates such as ``20150105`` to other modules, such as the *MARS Retrieval* module, these do not need to be converted into date variables. 
However, MARS treats **Date** and **Time** as separate parameters, so a date variable would need to be split into these components.

Date arithmetic
===============

When dealing with dates, the number 1 represents one day. So the expression d1 + 1 gives a date one day later than day 1. 
To compute the difference, in days, between two dates, it's simply:

* ``diff = d2 - d1``

Times can be added as fractions of days, and there are some helper functions too:

* ``d1 = d1 + 0.5                               # add 12 hours``

* ``d1 = d1 + hour(12)                          # hour(12) returns 0.5``

* ``d1 = d1 + hour(23) + minute(58) + second(0) # 2 minutes to midnight``

Compute and print the difference between your two dates, ``d2`` and ``d1``. 

Looping through dates
=====================

Three examples (no need to type these in, but the code is in a macro called dates in the solutions folder), to get a feel for it:

.. code-block:: python

  for d = 2015-01-01 to 2015-03-01 do
    print(d)  # each step is 1 day
  end for
 
  for d = 2015-01-01 to 2015-03-01 by 2 do
    print(d)  # each step is 2 days
  end for
 
  for d = 2015-01-01 to 2015-03-01 by hour(6) do
    print(d)  # each step is 6 hours
  end for

Computing the precipitation rate at a point
===========================================

As an exercise to put all of this together, we will write a new macro to compute the precipitation rate in mm per hour at a particular location for each time period. 
This could be a little complicated, so we'll do it step by step.

Compute the 'period' precipitation from precip.grib
---------------------------------------------------

This is what we already did earlier, so it's done! 
Just make a copy your earlier macro, *compute_precip*, and call it *precip_rate*. 
Change the result variable name to *precip_diff* to make it more generic. 
Remove the *return* line, as we want to use this fieldset, not return it.

Construct a loop to go through the fields
-----------------------------------------

Now, create an empty list (``dates = nil``). 
We will add each date variable to it as we loop through the fields.

We will obtain the date for each field of the original precipitation fieldset and add it to the list. 
We need to loop through the fields - we should already have ``n`` defined as the number of fields from the previous exercise:

.. code-block:: python

  dates = nil

  for i = 1 to n do
   print(i) # we will put proper code here in the next step!
  end for

Extract the date and time from each field
-----------------------------------------

You can get the valid date (including its time) of a field like this, inside the loop, where ``i`` is the field index:

.. code-block:: python

  dt = valid_date(precip[i])

Print the result to see what's being returned.

Add the date to the list
------------------------

We add it to the list like this (inside the loop):

.. code-block:: python

  dates = dates & [dt]

Compute the differences between consecutive dates
-------------------------------------------------

This is very similar to computing the precipitation data earlier (ok, we know it's 3 hours, but in theory it could be anything). 
We do this after the previous loop:

.. code-block:: python

  date_diffs = dates[2, n] - dates[1, n-1]

Now you have a list of time differences in days. You can multiply by 24 to get them in hours.

.. code-block:: python

  date_diffs_in_hours = date_diffs * 24

Extract the point value for each field in ``precip_diff``
----------------------------------------------------------

Use the ``nearest_gridpoint()`` function on the ``precip_diff`` fieldset. 
It returns a list of values, one for each field. 
Choose a location with some high precipitation.

The ``nearest_gridpoint()`` function can be called in a number of ways, but we will use it like this (giving actual numbers for ``lat`` and ``lon``) :

.. code-block:: python

  values = nearest_gridpoint(precip_diffs, lat, lon)

The result is a *list* of values, a value for each field. 
You can directly multiply a list variable by a number to obtain a new list where each element has been multiplied - **do this to scale from metres to mm**.

Compute precipitation rate in mm per hour
-----------------------------------------

The final calculation requires converting the data values into mm per hour - divide the list of precipitation values by the list of time differences, which are in hours.

Print the result - it will be a list of numbers, one for each time period.

Computing a climatology
=======================

.. image:: /_static/handling_time_in_metview/era-jan-mean.png

The supplied GRIB file *era_t2m_jan_2009_2013.grib* contains 2 metre temperature fields from the ERA Interim data set, interpolated onto a low-resolution 5x5 degree grid. The data are from years 2009 to 2013 and only include the month of January. The data are also from two times: 00:00 and 12:00. Check that all of this is true!

We will compute a small climatology dataset, which will simply be the mean of all these fields. 
Write a small macro to do this - it should be just 2 lines long: one to read the GRIB file, and one to compute the mean (simply the :func:`mean` function). 
Return or plot the result to confirm that it looks sensible.

.. note::

  Remember that the result is a derived field, and so the default temperature scaling from Kelvin to Celcius will not be applied unless **Grib Scaling of Derived Fields** is set to On in the *Contouring* icon.

Often, these climatological averages are computed individually for each time step. 
So in our case, we want to now produce two means: one for all the fields at 00:00 and one for all the fields at 12:00. 
Hint: use the *GRIB Filter* icon (and its equivalent Macro code) to extract all the fields where **Time** = 0, and compute their mean. 
Do the same with all the 12:00 fields. Concatenate the two mean fields into a 2-field fieldset and plot it.

Extracting dates from other data types
======================================

Geopoints
---------

To extract dates from a geopoints file/variable, use the :func:`dates` Macro function. 
Try it on the supplied geopoints file to see what it returns.

BUFR
----

The easiest way to extract dates from a BUFR file is to convert it to geopoints using the *Observation Filter* and then extract the dates from the resulting geopoints.

GRIB
----

For GRIB, we also have the :func:`base_date` function, which returns the model run time for each field.

NetCDF
------

The :func:`values` function will return a list of dates when the current variable is a time variable - see :ref:`Data Part 2 <data_part_2>`.

Extra Work
**********

If you have time, try the following.

Computing monthly anomalies
===========================

.. image:: /_static/handling_time_in_metview/era-jan-anoms.png

Continuing from the section "Computing a climatology", we will now take some data from 2014 and compute its difference from the climatology data we produced.

Examine the supplied GRIB file *era_t2m_jan_2014.grib*. 
It contains low-resolution temperature fields (4x4 degree) from the ERA Interim data set for each day in January 2014 at time steps 00:00 and 12:00. 
Try the following in a new macro:

* separate the data into the two different time steps and compute the mean field for each. The end result should be two fields - one is the mean of all the 00:00 fields and the other is the mean of all the 12:00 fields.

* for each time step, compute the difference between the 2014 mean and the climatological mean computed earlier (you may wish to combine both macros into a single macro at this point)

  a. note that the two data sets are on different grids - you will need to change one of them to the other's grid

* plot the result (it should be two fields) with *Contouring* icons appropriate for showing temperature anomalies.

Your result shows the monthly anomalies for January 2014 compared with the previous 5 years.

Finding points with large anomalies
===================================

.. image:: /_static/handling_time_in_metview/jan-larg-anoms.png

See if you can find the points which have anomalies over a certain threshold (e.g. 4 degrees). 
Create a geopoints variable with the result.

One possible way to do it:

* convert the anomaly field to geopoints (conversion to geopoints only works with one field at a time)

* use the :func:`filter` and :func:`abs` functions to find just the absolute values greater than 4

* plot with customised *Symbol Plotting* icons (we could take the ones used in the :ref:`Processing Data <processing_data>` tutorial)

* these points could be written to a file

In :ref:`Missing Values and Masks  <missing_values_and_masks>`, we will see how we could do this sort of thing directly with the GRIB fields
