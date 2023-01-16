.. _customising_your_plot_title:

Customising Your Plot Title
###########################

**Download**

.. list-table::

  * - **File**
    - **Modified**

  * - ZIP Archive `titles.tar.gz <https://get.ecmwf.int/repository/test-data/metview/tutorial/data_and_vis/titles.tar.gz>`_
    - Sep 16, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Text Plotting
*************

A plot's title should not be underestimated - it provides vital information about what is being displayed.

During the exercises, remember to give your icons useful names!

Automatic Titles
================

The :ref:`Text Plotting <mtext_icon>` icon controls the content and appearance of the title. 
By default, it contains this:

.. list-table::

  * - **Text Line Count**
    - 1

  * - **Text Line 1**
    - <magics_title/>

So we have a single-line title which uses the default content defined by Magics, Metview's plotting engine.

For GRIB data, the automatic title is constructed using the meta-data from each field in the plot.

.. image:: /_static/customising_your_plot_title/automatic-grib-title.png

For netCDF data, an automatic title consists of the value of the file's *title* global attribute if it exists.

For ODB data, some information about the number of points plotted and the columns used from the table go into the automatic title.

There is no automatic title for BUFR, geopoints or ASCII table data.

Customising an automatic title
------------------------------

.. image:: /_static/customising_your_plot_title/automatic-grib-title-large-bold.png

Visualise the supplied GRIB file *relative_humidity.grib* to see its automatic title.

Create a new *Text Plotting* icon and try to get the title to look similar to the image above. 
You should play with the parameters **Text Colour**, **Text Font**, **Text Font Style**, and **Text Font Size**.

Positioning a title
-------------------

.. image:: /_static/customising_your_plot_title/automatic-grib-title-positional.png

Make a duplicate of your *Text Plotting* icon. 
We will move the title to another location in the plot using the new icon. 
Use the following parameters:

.. list-table::

  * - **Text Mode**
    - Positional

  * - **Text Box X Position**
    - X coordinate of lower left corner of text box (in cm)

  * - **Text Box Y Position**
    - Y coordinate of lower left corner of text box (in cm)

  * - **Text Box X Length**
    - Width of the box (in cm)

  * - **Text Box Y Length**
    - Height of the box (in cm)

  * - **Text Box Blanking**
    - On

  * - **Text Border**
    - On

Remember that Metview uses an A4 page by default, which is 29.7cm wide by 21.0cm high. 
Try to figure out the coordinates of the box, or look in the *solutions* folder!

Notice that the original title did not disappear - we added a new one! Here are the rules:

* there can be only one *Text Plotting* icon where **Text Mode** is Title - dropping new such icons into the plot replace the current title

* dropping different Positional *Text Plotting* icons into the plot *add* text boxes; **but** dropping *the same* Positional icon multiple times (e.g. with modifications in between) will not accumulate - the text box will be updated

All of this means that if we want to remove the title at the top, we must create an empty title - a default *Text Plotting* icon with **Text Line Count** set to 0 will do the trick.

User Defined Titles
*******************

.. image:: /_static/customising_your_plot_title/user-formatted-grib-title.png

If you know (or can figure out from some Macro code) exactly what your plot is going to show, then you can construct a title with no automatically computed elements. 
Or you can combine the two.

Create a new *Text Plotting* icon and set **Text Line Count** to 2. 
Leave the automatic title in line 1. We will create a nicely formatted line of text using HTML notation. 
Enter the following text into line 2:
  
.. code-block:: html

  My title which has <b>bold</b>, <u>underlined</u> and <font color='rose'>coloured</font> text

Some Metview users have used coloured text in the title as an alternative legend.

If you are writing a macro, then you can use all of the string manipulation capabilities to construct the title. 
Type the following macro code, or try the one in the *solutions* folder. It calls :func:`grib_get` functions to retrieve meta-data from the GRIB header, then constructs a title using it.

.. note::

  using the Grib Examiner is a good way to find the available keys to extract meta-data from a GRIB field.

.. code-block:: python
  
  rh = read("relative_humidity.grib")
   
  field_name       = grib_get_string(rh[1], 'name')
  field_valid_date = grib_get_string(rh[1], 'validityDate')
  field_level      = grib_get_double(rh[1], 'level')
   
  title_text = field_name & ' ' & field_valid_date & ' at level ' & field_level
  print(title_text)
   
  title = mtext(text_line_1: title_text)
   
  plot(rh, title)
  
The :func:`print` command shows you what is going into the :func:`mtext` definition (which is the Macro function for the *Text Plotting* icon).

This is fine for a single field, but if you move between the two fields in the plot, there are two different vertical levels - but we only have one title, and it was constructed using the meta-data from the first field. 
We cannot tell it to "use this title for the first field, but use another title for the second field". 
So in this case we should use a handy feature of the *Text Plotting* icon which is described in the next section.

Using meta-data references in titles
====================================

In the previous example, Macro constructed a title string and passed it to the :func:`plot` command, which used it directly. 
However, the :func:`plot` command can be more clever than that. 
For a start, it knows to translate ``<magics_title/>`` into the automatic title. 
It also has some other tricks.

Instead of having Macro extract the meta-data, we can pass *references* to the meta-data, which will be replaced with their values at plot time, per field.

Create a copy of your macro and change just one line:

.. code-block:: python

  field_level = "<grib_info key='level'/>"
  
Now, we are no longer extracting the level ourselves, but we are asking the plotting module to extract it at plotting time. 
With this change, the title will show the correct level for each field. 
We could extend this to construct complex titles showing various information.

Dealing with multiple overlaid fields
-------------------------------------

.. image:: /_static/customising_your_plot_title/grib-title-multiple-fields.png

Adapt your macro to also read and overlay the geopotential data. 
Use the supplied *rh_shade* icon to colour the relative humidity field:

.. code-block:: python
  
    rh = read("relative_humidity.grib")
  z  = read("geopotential.grib")
  ...
   
  rh_shade = mcont( ... )
   
  plot(rh, rh_shade, z, title)
  
We now have two title lines. When we ask the plotting engine to extract meta-data from its fields, it will produce one title line per field. 
If we don't want this, then we need to tell it which field we do want a title line for.
Modify the field_level definition so that the ``<grib_info>`` tag contains a where clause:

.. code-block:: python

  field_level = "<grib_info key='level' where='shortName=r'/>"
  
Now, the title will only be produced for the relative humidity field (its shortName key is "r"). 
We would need to do this for all ``<grib_info>`` tags if there were more.

We should also update the parameter names in the title - let's assume that each frame will contain the same parameters (they contain different levels), so we could change ``field_name`` to this:

.. code-block:: python
  
  field_name = grib_get_string(rh[1], 'name') & ' / ' & grib_get_string(z[1], 'name')
  

Extra Work
**********

Text boxes
==========

To exemplify the *Text Plotting's* dropping rules, do the following:

* **Visualise** GRIB file *relative_humidity.grib*

* apply a *Text Plotting* icon to move the title to another location (this icon was created previously)

* apply a new *Text Plotting* icon to remove the default automatic title

* apply a new *Text Plotting* icon to draw a chosen text near the top-left corner of the plot and customise its colour, font, style and size

* apply a new *Text Plotting* icon to draw a chosen text around the middle of the plot and customise its border and box-blanking

Next, create a Macro program, name it *custom_text_boxes*, using all the above icons.

Meta-data references in Macro
=============================

The title just shows the date - add the time of the data.
