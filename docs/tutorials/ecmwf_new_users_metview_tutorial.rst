.. _ecmwf_new_users_metview_tutorial:

ECMWF New Users Metview Tutorial
################################

.. note::

  This tutorial was written for ECMWF's Introduction for New Users course (COM_MARS) and shows how to retrieve data from MARS using Metview, perform some basic manipulations and plot the result.

Preparation
***********

First start Metview; at ECMWF, the command to use is simply metview. 
You should see the main Metview desktop which looks something like Figure 1.

In Metview, all operations can be performed via icons. All icons are available via the Create New Icon context menu of the Metview desktop.

You will create some icons yourself, but some are supplied for you - please download the following file and save it in your ``$HOME/metview`` directory:

.. list-table::

  * - `metview_intro.tar.gz <https://get.ecmwf.int/repository/test-data/metview/tutorial/new_users/metview_intro.tar.gz>`_

Alternatively, if at ECMWF then you can copy it like this from the command line::

  cp /scratch/graphics/cgi/metview_intro.tar.gz $HOME/metview/

You should see it appear on your main Metview desktop, from where you can right-click on it, then choose **execute** to extract the files. 
You should now (after a few seconds) see a *metview_intro* folder which contains the icons we will work with. 
You should work in this folder, not the embedded *solutions* folder.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/default-desktop.png
     
    Figure 1 - the Metview desktop


Exercise 1: forecast - analysis difference
******************************************

This exercise shows how to retrieve GRIB data from MARS, examine its structure, compute the differences between fields and visualise the data in various ways.

Retrieving the analysis data
============================

To perform a MARS retrieval in Metview, right-click on an empty area of the Metview desktop and select **Create New Icon** from the context menu. 
Select Mars Retrieval and hit Return or click **OK**. 
This will create a copy of the icon for you to customise. 
Rename the new icon to *temperature_analysis* by clicking on its name. 
Edit your icon (right-click & **edit**, see **Figure 2**) and set the following parameters:

.. list-table::

  * - **Parameter**
    - **Value**
    - **Notes**

  * - **Param** 
    - T
    - Note: sets the desired meteorological parameter to Temperature

  * - **Date** 
    - -3
    - Note: sets the analysis base time to 3 days ago

  * - **Grid** 
    - 1/1
    - Note: interpolates the result onto a 1.0-degree grid

To save these settings, click the Save button at the bottom-left of the icon editor (or click Ok to save and close the editor).

.. figure:: /_static/ecmwf_new_users_metview_tutorial/mars-editor.png

    Figure 2 - the Mars Retrieval icon editor

Inspecting the analysis data
============================

Perform the data retrieval by choosing **execute** from the icon's context menu. 
The icon name should turn orange whilst the retrieval takes place, then green to indicate success (if the name turns red, then the retrieval failed and you should look in the output log, available from the **Log** entry in the context menu). 
The data is now cached locally. 
To see what was retrieved, right-click **examine** the icon. 
This brings up Metview's GRIB Examiner tool (**Figure 3**). 
Here we can see that we retrieved six vertical levels of data; this is as expected if we look at the **Levelist** parameter in the icon editor.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-25_16-35-56.png

    Figure 3 - the GRIB Examiner

.. note::

  The GRIB Examiner allows in-depth examination of GRIB files with many ways to customise the information. 
  We will not cover these facilities in this introduction.

Now **visualise** the data, again using the icon's context menu. 
You will see a map plot with the default contouring style in the Display Window (**Figure 4**). 
The *zoom* controls in the toolbar give control over the area selection.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-25_16-36-59.png

    Figure 4 - a default map plot

To plot the data with shaded colours, create another new icon - this time select the *Contouring* icon. 
Rename it *shade* and edit it, providing these parameters:

.. list-table::

  * - **Parameter**
    - **Value**
    - **Notes**

  * - **Legend**
    - On
    -  

  * - **Contour Shade**
    - On
    - 

  * - **Contour Shade Method**
    - Area Fill
    - 

  * - **Contour Shade Max Level Colour**
    - Red
    - Note: to select a colour, click the small triangle
    
      next to the parameter name to reveal the colour
      
      selection dialogue

  * - **Contour Shade Min Level Colour**
    - Blue
    - 

  * - **Contour Shade Colour Direction**
    - Clockwise
    - 

Save the icon settings (Save) and drop this into the Display Window (re-visualise the data if you have closed the Display Window). 
The result should resemble **Figure 5**. 

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-25_16-45-44.png

    Figure 5 - map plot with shaded contours

Metview's *Contouring* icon provides much flexibility in choosing how to display gridded fields; this tutorial uses only simple colour schemes.

The fields can be visualised using different *views*. 
These can be defined by a set of icons such as *Geographical View* and *Cross Section View*. 
In the *solutions* folder are 2 pre-prepared view icons for you to try. 
Visualise the *polar_stereo_europe* icon and drop your *temperature_analysis* icon into the resulting Display Window. If you edit this view icon, you will see how to define a geographical view. 
Now close the Display Window and visualise your data in the same way with the the *cross_section_example* view. 
This icon defines a geographical line along which a cross section of the data is computed (remember that the data consists of a number of vertical levels). 
You can also drop your *shade* icon into the plot (**Figure 6**).

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-27_9-27-57.png

    Figure 6 - cross section plot of data

.. note::

  The Display Window provides a number of facilities for further inspection of the data (e.g. magnifier, point values, histogram), not covered here.

Retrieving the forecast data
============================

In your original Metview directory create a copy of your *temperature_analysis* icon (right-click, **Duplicate**) and rename the copy to *temperature_forecast*. 
Edit this icon and set the following parameters:

.. list-table::

  * - **Parameter**
    - **Value**

  * - **Type**
    - FC

  * - **Param**
    - T

  * - **Date**
    - -5

  * - **Step**
    - 48

  * - **Grid**
    - 1/1

The analysis data was valid for 3 days ago; this new icon retrieves a 48-hour forecast data generated 5 days ago, so it is also valid for 3 days ago. 
You don't need to separately **execute** and **visualise** the icon - if you **visualise** it, the data will automatically be retrieved first. 
The plot title will verify that this data is valid for the same date and time as the analysis data. 
It also contains the same set of vertical levels.

Compute the forecast-analysis difference
========================================

Create a new *Simple Formula* icon. 
Rename it to *fc_an_diff*. 
Edit the icon, ensure that the first **FORMULA** option is selected (F+G) and that the operator is minus ( - ). 
Drop your *temperature_forecast* icon into the **Parameter 1** box, and drop *temperature_analysis* into the **Parameter 2** box. Save the icon and visualise it. 
The difference will be computed and the result plotted. 
Note that all 6 fields in each data icon are used in the computation - the result is a set of 6 fields. 
The *solutions* folder contains two *Contouring* icons which can be used to show the differences: select both *pos_shade* and *neg_shade* with the mouse and drop them both together into the Display Window (see Figure 7). 
It is also possible to drop them one at a time, but they do not accumulate - one will replace the other.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-26_17-3-10.png

    Figure 7 - difference plot with two contour icons

Automating the whole procedure
==============================

Ensure that the difference fieldset is visualised with the contouring applied. 
To generate a Metview Macro script from this plot, click the **Generate Macro** button (also available from the **File** menu). 
A new Macro script will be generated - have a look at it to confirm that it contains code to retrieve all the data, compute the difference and plot the result. 
Run the macro to obtain the plot, either by using the Run button from the Macro Editor, or by selecting *visualise* from the icon's context menu). 
By default, the macro is written so that it will produce an interactive plot window; it will generate a PostScript file if it is run with the **execute** command, or if it is run from the command line::

  metview -b  <macro-name>
 
.. note::

  Metview Macro is a rich, powerful scripting language designed for the high-level manipulation and plotting of meteorological data. 
  For examples of the available functions, see :ref:`List of Operators and Functions <macro_fn_list>`. 
  The code generated automatically above is intended as a starting point only - usually at least some editing will be required in order to make the code more streamlined for your needs.


Exercise 2: forecast - observation difference
*********************************************

This exercise builds on Exercise 1, but uses observation data in BUFR format instead of analysis fields.

Retrieving the observation data
===============================

Create a new *Mars Retrieval* icon and rename it to *obs*. 
Edit it and set the following parameters in order to retrieve BUFR observation data from 3 days ago:

.. list-table::

  * - **Parameter**
    - Value

  * - **Type**
    - OB

  * - **Repres**
    - Bufr

  * - **Date**
    - -3

Retrieve the data and **examine** it. 
Metview's BUFR Examiner displays the contents of the BUFR data (**Figure 8**). Each message contains many measurements. 

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-27_9-47-38.png

    Figure 8 - the BUFR Examiner

If you **visualise** the data, you will see a standard display of synoptic observations. 
**Figure 9** shows this, using the shaded_coastlines icon from the solutions folder (this plot has also been zoomed to show a smaller area).

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-27_9-53-3.png

    Figure 9 - synoptic observation plotting

Extracting the 2 metre temperature
==================================

Create a new *Observation Filter* icon and rename it to *filter_obs_t2m*. 
With this icon we will extract just the 2m temperature into Metview's custom ASCII format for scattered geographical data - *geopoints*. Set these parameters:

.. list-table::

  * - **Parameter**
    - Value

  * - **Data**
    - Drop your *obs* icon here

  * - **Output**
    - Geographical Points

  * - **Parameter**
    - 012004

.. note::

  012004 is the code for 'Dry bulb temperature at 2m'. 
  If you **examine** this icon now, you will see the result: a table of geo-located temperature values. 
  When you **visualise** the data, you will see that the actual values are plotted as text on the screen; we can do better than this. 
  From the *solutions* folder, drop the *coloured_markers* icon into the Display Window. 
  The *shaded_coastlines* icon may also help make the points easier to see (**Figure 10**).

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-27_10-0-50.jpg

    Figure 10 - 2m temperature observations
 
Retrieving the forecast data
============================

Create a new *Mars Retrieval* icon, rename it to *t2m_forecast*, and set these parameters in order to retrieve the 48-hour forecast made 5 days ago for 2-metre temperature. 
The result will be a single field.

.. list-table::

  * - **Type**
    - FC

  * - **Levtype**
    - Surface

  * - **Param**
    - 2t

  * - **Date**
    - -5

  * - **Step**
    - 48

  * - **Grid**
    - 1/1

Computing the forecast-observation difference
=============================================

This is just the same as in Exercise 1, using a *Simple Formula* icon; create a new one and rename it to *fc_obs_diff*. 
Drop *t2m_forecast* into the **Parameter 1** box, and *filter_obs_t2m* into the **Parameter 2** box. 
Visualise the result - you will see that the result of a field minus a scattered geopoints data set is another geopoints data set. 
For each geopoint location, the interpolated value from the field was extracted before performing the computation. From the solutions folder, drop both the *diff_symb_hot* and the *diff_symb_cold* icons together into the plot in order to get a more graphical representation of the result.

Overlaying data in the same plot
================================

To plot the forecast field together with the observation differences, do the following. 
Visualise *t2m_forecast* and drop the *shade* icon into the plot. 
Now drop *fc_obs_diff* into the plot, followed by (or with) *diff_symb_hot* and *diff_symb_cold*. 
The observation differences don't stand out well against the strongly coloured field, so drop *shade_light* into the plot to obtain something like Figure 11.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/image2013-2-27_13-7-29.jpg

    Figure 11 - temperature forecast field with obs-forecast differences overlaid


Exercise 3: ODB data
********************

This exercise introduces ODB data and some ways that Metview can use it. 
To save time, we will mostly use pre-prepared icons. 
**Enter the *ODB* folder to do these exercises**.

Retrieving the ODB data
=======================

The *'ret_temp' MARS Retrieval* icon is already prepared for you to fetch Land TEMP ODB data from MARS from 3 days ago. Edit the icon to see which parameters are set. 
The most important ones are these:

.. list-table::

  * - **Parameter**
    - **Value**
    - **Notes**

  * - **Type**
    - MFB
    - Mondb feedback

  * - **Reportype**
    - 16022
    - land TEMP

  * - **Obsgroup**
    - 17
    - Conventional

Close the icon editor and perform the data retrieval by choosing **execute** from the icon's context menu. 
Right-click **examine** the icon to bring up Metview's ODB Examiner tool. 
Here you can see the metadata (Columns tab) and the actual data values themselves (Data tab). 
Close the ODB Examiner.

Save a local copy of the ODB data to the current folder by right-clicking **Save result** on the *ret_temp* icon; save as 'temp.odb'. 
A few seconds later an *ODB Database* icon (**Figure 12**) with the given name will appear at the bottom of your folder. 
We will work with this to avoid repeating the retrieval.

.. figure:: /_static/ecmwf_new_users_metview_tutorial/odb-icons.png

    Figure 12 - ODB and ODB Visualiser icon

Using the ODB Visualiser
========================

We will select and visualise the 500 hPa temperature values from our ODB using the '*vis_temp*' :ref:`ODB Visualiser <odb_visualiser_icon>` icon.

Now edit the *vis_temp* icon.

First, drop your *ODB Database* icon into the **ODB Data** field.

Next, specify the where statement of the query in the **ODB Where** parameter as:
  
.. code-block:: SQL
  
  varno = 2 and vertco_reference_1=50000
  
Save these settings, then right-click **visualise** the '*vis_temp*' icon to generate the plot. 
Then drag the the provided :ref:`Symbol Plotting <msymb_icon>`, :ref:`Coastlines <mcoast_icon>`, :ref:`Legend <mlegend_icon>` icon and :ref:`Text Plotting <mtext_icon>` icon icons into the plot for further customisation. Metview's plot window has many tools for inspecting data values, described in detail in the standalone tutorial "`Using ODB with Metview <https://confluence.ecmwf.int/display/METV/Using+ODB+with+Metview>`_". Do not close the plot window yet.

Overlaying with GRIB data
=========================

The '*fc.grib*' GRIB icon contains 12 h global forecasts of temperature and wind at different vertical levels, valid for the date and time of our TEMP ODB data.

To overlay the 500 hPa temperature forecast we need to filter the matching field from the GRIB file. 
The '*t500_fc*' GRIB Filter icon is already already set up to perform this task. 
Just drag '*t500_fc*' into the plot, then drag the '*t_cont*' :ref:`Contouring <mcont_icon>` icon icon into the plot as well to customise the contour lines (**Figure 13**).

.. figure:: /_static/ecmwf_new_users_metview_tutorial/odb-t-overlay.png

    Figure 13 - ODB and GRIB data overlai

Further ODB work
================

If you have time, inspect and run the supplied macros:

* '*diff.mv*' - computes and plots the difference between the ODB observation data and the GRIB model forecast
* '*plot_wind.mv*' - extracts U and V wind components from the ODB data, converts to *geopoints* format and plots the result
* '*plot_tephi.mv*' - computes and plots a tephigram for a given station ID

The results can be seen in the images below:

.. image:: /_static/ecmwf_new_users_metview_tutorial/odb-diff.png

.. image:: /_static/ecmwf_new_users_metview_tutorial/odb-wind.png

.. image:: /_static/ecmwf_new_users_metview_tutorial/odb-tephi.png
