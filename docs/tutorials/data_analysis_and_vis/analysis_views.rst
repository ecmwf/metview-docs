.. _analysis_views:

Analysis Views
##############

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - ZIP Archive `analysis_views.tar.gz <https://sites.ecmwf.int/repository/metview/test-data/tutorial/data_and_vis/analysis_views.tar.gz>`_
    - Sep 13, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_


Views in Metview
****************

A fundamental concept in Metview is the *View*. 
A *View* specifies the following definitions in a Metview plot:

* type of visualisation (e.g. geographical map, cross section, vertical profile, tephigram)

* parameters specific to that plot type (e.g. geographical area, cross section line, min/max axes values)

* plot position within the page (several plots can share a page)

* how to overlay different data in the same plot (explored in :ref:`Handling Time in Metview  <handling_time_in_metview>`)

* plot decoration (e.g. draw a frame around the plot)

If you do not provide a *View*, then Metview will use a sensible default *View*. 
For instance, when you visualise a GRIB icon, a default *Geographical View* containing a global map in a Cylindrical projection is used.

The following customised *Geographical View* shows some of these concepts including plot position and coloured frames.

.. image:: /_static/analysis_views/geo-view-params.png

The Geographical View 
=====================

.. image:: /_static/analysis_views/GEOVIEW.png 

This is the default View for plotting geographic-based data. This View was discussed previously in :ref:`Customising Your Plot <customising_your_plot>`

The Cartesian View     
==================

.. image:: /_static/analysis_views/CARTESIANVIEW.png

This view is for plots that are not on a map, and will be covered in another session: :ref:` Graph Plotting in Metview <graph_plotting_in_metview>`.

The Annotation View    
===================

.. image:: /_static/analysis_views/ANNOTATIONVIEW.png

This will be covered in another session: :ref:`Layout in Metview <layout_in_metview>`.

The Cross Section View    
======================

.. image:: /_static/analysis_views/MXSECTIONVIEW.png

The :ref:`Cross Section View <mxsectview_icon>` icon is a plotting specification for cross section plots along a given transect line.

.. image:: /_static/analysis_views/cross-section-plot.png

Create a new *Cross Section View* icon, **Visualise** it and drop the *t_fc24.grib* icon into the resulting **Display Window**. 
A default cross section along the Equator is generated.

To customise the transect line (coordinates along which the cross-section is calculated), **Edit** the *Cross Section View* icon and either click on the **Geography Tool** button to bring up an editor (or type the coordinates by hand).

.. image:: /_static/analysis_views/image2015-2-19_14-52-15.png

**Save/OK** the changes and re-visualise the data with this new cross section.

Note that you can still drag any valid *Contouring* icons you may have into the **Display Window** when visualising a cross section. 
For instance, apply the given *shade* icon. You may want to customise it and try different configurations.

Inspect the GRIB icon (right-click on it and choose **examine**) to see the type of input data this View requires - it should be *gridded* data (rather than spherical harmonics) and it should contain fields at multiple vertical levels. 
This view accepts data stored in either pressure levels or model levels (optionally supply a Logarithm of Surface Pressure field to transform model levels to pressure levels).

The Vertical Profile View    
=========================

.. image:: /_static/analysis_views/MVPROFILEVIEW.png

The :ref:`Vertical Profile View <mvertprofview_icon>` icon is a computation/plotting specification for vertical profiles.

.. image:: /_static/analysis_views/vertical-profile-plot.png

Create a new *Vertical Profile View* icon, **Visualise** it and drop the *t_fc24.grib* icon into the **Display Window**. 
The result shows a vertical profile at a point (or averaged over an area). 
Experiment with this icon in a similar way to how you did with the *Cross Section View* icon.

The :ref:`Graph Plotting <mgraph_icon>` icon is the visual definition used for the plotting of graphs (e.g. lines, curves and bar charts).

.. image:: /_static/analysis_views/MGRAPH.png

To customise the line displayed in this plot, create a new instance of *Graph Plotting* and rename it to *vdline*. 
Edit it, setting the following parameters:

.. list-table::

  * - **Graph Line Style**
    - Dash

  * - **Graph Line Colour**
    - Black

  * - **Graph Line Thickness**
    - 5

**Save/OK** the changes and drag it into the **Display Window**.

The Average View    
================

.. image:: /_static/analysis_views/MAVERAGEVIEW.png

The :ref:`Average View <maverageview_icon>` icon is a plotting specification for average (zonal or meridional) cross-section plots over an area.

.. image:: /_static/analysis_views/average-view-plot.png

Create a new *Average View* icon, **Visualise** it and drop the *t_fc24.grib* icon into the **Display Window**. 
A default meridional average over the global area is generated. 
Notice the horizontal axis - it only contains E/W co-ordinates, because the data values have been averaged along N/S meridional lines; for each point of longitude, there is one computed value per 2D field. 
With multiple fields in the vertical direction we can produce this plot.

Experiment with this icon in a similar way to how you did with the *Cross Section View* icon. 
You can use a *Contouring* icon, e.g. the *shade* icon, to style the contours of the plotting.

The Hovmoeller View    
======================

.. image:: /_static/analysis_views/MHOVMOELLERVIEW.png

The :ref:`Hovmoeller View <mhovmoellerview_icon>` icon is a computation/plotting specification for Hovmoeller diagrams along a specified arbitrary transect line or a rectangular area. The diagram displays a two-dimensional graph with latitude or height as one axis, and time as the other.

.. image:: /_static/analysis_views/hovmoeller-plot.png

Create a new *Hovmoeller View* icon, **Visualise** it and drop the *t_ts.grib* icon into the **Display Window**. 
A default diagram derived from a transect line along the Equator is generated. 

Three types of Hovmoeller diagrams can be produced:
 
1. Area Hovm - diagram derived from an input rectangular area
 
2. Line Hovm - diagram derived from an input transect line

3. Vertical Hovm - diagram derived from an input rectangular area and a set of levels.

For now, only consider the **Area Hovm** type and try a different transect line. 
As previously, you can use a *Contouring* icon to style the contours of the plotting.

This view requires data at different time steps. 
**Examine** the GRIB icon to see the fields used for this example.

The Thermo View   
===============

.. image:: /_static/analysis_views/THERMOVIEW.png

The :ref:`Thermo View <thermoview_icon>` icon is a plotting specification for Thermodynamic diagram plots from a suitable GRIB (:func:`thermo_grib`) or BUFR (:func:`thermo_bufr`) data source. In such a diagram, temperature, humidity (represented by the dew point) and wind values are displayed with respect to pressure. Note that only the Tephigram diagram is currently available, although there exist other types of thermodynamic diagrams, such as Skew-T, Emagram and Stuve.

.. image:: /_static/analysis_views/tephi-view.png

Create a new *Thermo View* icon, **Visualise** it and drop the *tquv_pl.grib* icon into the **Display Window**.
A default diagram related to a geographical location [0,0] is generated.

**Examine** the GRIB icon to see the type of input data this *View* requires. 
Fields Temperature and Specific Humidity are mandatory and they will be used to compute the Dew Point parameter. 
Fieldsets U and V wind components are optional, but if given they will be used to compute the wind vectors. 
If the data is given in model levels then a Logarithm of Surface Pressure field must be provided too in order to help the conversion to pressure levels fields.

To customise the curves displayed in this plot, you can apply (or edit it first) icon *vdline*. 
The changes will be applied to both lines. 
The ability to customise each line individually (temperature and dew point) is available in the :ref:`Thermo Plotting <mthermo_icon>` icon. Try it!

The :ref:`Wind Plotting <mwind_icon>` icon is the visual definition responsible for specifying how wind vector data is displayed. 
It controls the plotting of features such as wind arrows and wind flags.

.. image:: /_static/analysis_views/MWIND.png

To customise the wind flags displayed in the plot, create a new instance of this icon and rename it to *vdwind*. 
**Edit** it, setting the following parameters:

.. list-table::

  * - **Wind Field Type**
    - Flags

  * - **Wind Flag Colour**
    - Coral

  * - **Wind Flag Length**
    - 1.3

  * - **Wind Flag Thickness**
    - 2

**Save/OK** the changes and drag it into the **Display Window**.

Macro example
*************

Let's create a Macro program to analyse the vertical structure of temperature changes in time. 
This exercise reads two forecast steps, computes the differences and visualises the result in a *Cross Section View*.

Create a new Macro icon and rename it to *xsdiff*. 
Edit it and do the following:

* drop the *t_fc24.grib* icon into the Macro Editor. A variable called *t_fc24_2e_grib* is assigned to the value of the :ref:`read() <read_fn>` command, which reads the GRIB data. Rename the variable to simply be *t_fc24*.

* drop the *t_fc96.grib* icon into the Macro Editor. Rename the variable to *t_fc96*.

* compute the differences: ``diff = t_fc96 - t_fc24``

* drop the two contouring icons, *neg* and *pos*, into the editor

* drop the *xs_europe* icon into the editor

* underneath the generated code, type the following line:

.. code-block:: python

  plot(xs_europe,diff,neg,pos)

The says, "In the ``xs_europe`` view, plot the data field ``diff`` using the visual definitions ``neg`` and ``pos``."

Your complete macro should look like this:

.. code-block:: python

  t_fc96 = read("/path/to/home/metview/training/day_2/analysis views/t_fc96.grib")
  t_fc24 = read("/path/to/home/metview/training/day_2/analysis views/t_fc24.grib")
 
  diff = t_fc96 - t_fc24
 
  pos = mcont(
      legend                         : "on",
      # <code omitted for brevity>
      )
 
  neg = mcont(
      legend                         : "on",
      # <code omitted for brevity>
      )
 
  xs_europe = mxsectview(
      line : [55,-6,43,16]
      )
 
  plot(xs_europe,diff,neg,pos)
  
Now run the macro to generate the plot. 
You can also omit ``xs_europe`` from the :func:`plot` command; in this case, Metview will use the default view for GRIB data, which is a *Geographic View*, giving a map plot.

Finally, **Examine** the two input GRIB icons to see how the fields differ in terms of date, time and step.

View / Data Modules
*******************

Metview uses a netCDF format internally for the results of some computations (this format will be covered in the session :ref:`Data Part 2 <data_part_2>`). 
Most of the Views described in this session (i.e. Cross Section, Vertical Profile, Average, Hovmøller and Thermo) do this, but the resulting data file is not available to the user. 
Therefore, each of these *Views* has a corresponding *Data Module* icon. 
If the intention is to simply plot the result, then the *View* icons are more useful. 
But to store the result data, the corresponding *Data Module* icon is required.

* create both a *Vertical Profile View* and a *Vertical Profile Data* icon.

* **Edit** both to see the differences.

All the parameters related to the visualisation of the result are only in the *View* icon, and the **Data** parameter exists only in the *Data Module* icon.

Now dealing only with the *Vertical Profile Data* icon:

* drop the supplied input GRIB icon *t_fc24.grib* into the **Data** parameter box.

* set the **Point** parameter to whatever you like and save the icon.

* **Examine** this icon to see the resulting netCDF file in the **NetCDF Examiner**.

* **Save Result** to save the result into a file for storage.

All of this can also be put into a Macro, where the resulting netCDF variable can be further manipulated before being written to a file (or visualised):

* create a new *Macro* icon and rename it to *save_vp*; edit it

* into the Macro Editor, drop the *Vertical Profile Data* icon that you already set up

* write the result to a file

To write a netCDF variable to a file, the syntax is the same as for any other data type:

.. code-block::

  write('output_file', data)

Your macro should be 3 lines long (well, 3 commands anyway) - one to read the input GRIB file, one to compute the profile and one to write the result to disk.

Extra Work
**********

.. note::

  If you are attending the training course at ECMWF, please do :ref:`Layout in Metview <layout_in_metview>` before tackling the extra work here.

Hovmoeller Types
================

Investigate the different types of Hovmoeller diagrams available. 
Please note that type **Vertical Hovm** requires the input GRIB data *t_ts_nlevels.grib*. 
Examine this data to see that it contains fields from different vertical levels.

Axis Customisation
==================

.. image:: /_static/analysis_views/xs-axis-defs.png

All of these views allow the ability to customise the rendering of the axes. 
While the view itself defines the limits and projection parameters for the plot, the axis lines themselves can be customised, for example in terms of colour and title.

Create a new *Axis Plotting* icon and rename it to *H Axis*. 
Edit it to change the colour of the axis and to add an axis title. 
Repeat the process to create a vertical axis icon.

Edit a *Cross Section View* icon and drop your icons into the **Horizontal Axis** and **Vertical Axis** parameter boxes. 
**Visualise** the view to see the results.
