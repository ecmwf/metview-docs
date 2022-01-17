.. _customising_your_plot:

Customising Your Plot
#####################

**Download**

Download the icons for this session from the link below. 
Create a sub-directory called ``training`` inside your Metview home directory, ``$HOME/metview``, and save the .tar.gz file there. 
Then, from Metview, navigate to this folder and right-click on the tar.gz icon; choose **Extract** to uncompress the files into their folder. Work from there. The main instructions are written for participants of the `Data analysis and visualisation using Metview <https://confluence.ecmwf.int/display/METV/Data+analysis+and+visualisation+using+Metview>`_ training course at ECMWF. Any files to be copied from the file system will also be downloadable from this page.
 
 .. list-table::
 
  * - **File**
    - **Modified**

  * - ZIP Archive `customising your plot.tar.gz <https://confluence.ecmwf.int/download/attachments/59791892/customising your plot.tar.gz?api=v2>`_
    - Sep 08, 2016 by `Iain Russell <https://confluence.ecmwf.int/display/~cgi>`_

Creating and Editing an Icon
****************************

This session uses the same *t1000.grib* data file as `A Simple Visualisation <https://confluence.ecmwf.int/display/METV/A+Simple+Visualisation>`_; a copy of that file already exists in the folder for this session.

Metview uses icons to control the various aspects of a plot's appearance. We will look at some of these now, starting with the coastline plotting.

.. image:: /_static/customising_your_plot/t1000-with-shaded-coastines.png

First, create a new :ref:`Coastlines <mcoast_icon>` icon. 
You can right-click within the **Metview desktop** to obtain a context menu from where the option **Create new icon** is available (shortcut: CTRL-N).

.. image:: /_static/customising_your_plot/desktop_context_menu_new_icon.png
.. image:: /_static/customising_your_plot/new_icon_dialog.png


This brings up a dialogue from where you can find the :ref:`Coastlines <mcoast_icon>` icon; either double-click the icon, or drag it onto the desktop to create a new instance. 
Close the dialogue.

Edit the newly-created icon by either double-clicking on it or else right-click, **edit** (double-clicking an icon performs the edit action for most icon types). 
This brings up the icon editor for coastline plotting. 
All user-selectable parameters for plotting coastlines are here. Set the following parameters:

.. list-table::

  * - Map Coastline Thickness
    - 2
    
      **Note**: an undo button now appears beside this parameter

  * - Map Coastline Land Shade
    - On

  * - Map Coastline Land Shade Colour
    - Cream

For colour-based parameters, there are two small arrows - the one on the right reveals a drop-down list of predefined colours (use this one); then one on the left reveals an advanced colour selection tool.

.. image:: /_static/customising_your_plot/coastline_editor_compact.png

After making these changes, click the **Ok** button to save and exit the editor.

Visualise the data again, and drag your new :ref:`Coastlines <mcoast_icon>` icon into the **Display Window**.

Your :ref:`Coastlines <mcoast_icon>` icon can be dragged into any plot, and `later <https://confluence.ecmwf.int/display/METV/Optimising+Your+Workflow>`_ we'll see how to store useful icons so that they can be easily accessed from anywhere.

So you know what it does, rename the icon to *land_shade* by clicking on its name and editing the text.

The Coastlines icon is an example of a Visual Definition (visdef) icon. 
The purpose of these icons is to modify the plotting attributes of various data.

Changing the Map Projection and Storing the Area
************************************************

.. image:: /_static/customising_your_plot/t1000-on-polar-projection.png

Metview's default map projection is Cylindrical. However, meteorologists often use other projections when plotting data.

Create a new Geographical View icon and rename it to polar_europe. Edit the icon and change the following parameter:

.. list-table::

  * - **Map Projection**
    - Polar Stereographic

Save the changes and **visualise** the icon. 
Drop the GRIB data icon into the **Display Window** to see it on the new map. 
It is also possible to visualise the GRIB icon and then drop the *Geographical View* icon into the plot to achieve the same effect. Have a look at some of the other projections on offer, then go back to polar stereographic.

Now we want to set the area used in the view. 
Although we can interactively zoom into smaller areas in the **Display Window**, we now want to store a particular area so that we can use exactly the same one again and again. Set the **Map Area Definition** to Corners and click on the **Geography Tool** button next to the **Area** parameter (shown in the picture below).

.. image:: /_static/customising_your_plot/geography_help_tool_button.png

This tool helps you define a region.

.. image:: /_static/customising_your_plot/geography_help_tool.png

Use the **Zoom** tools to enlarge the European area and use the **Area tool** to select a region over Europe. 
Click **Ok** to save your selection - your choices will now be updated in the *Geographical View* editor. 
Click **Apply** in the *Geographical View* editor to save everything. 
Plot your data in this view to confirm that the area and projection are as desired.

Linking the Coastlines icon with the Geographical View Icon
***********************************************************

Although they can be used separately, the :ref:`Coastlines <mcoast_icon>` icon can be linked into the *Geographical View* icon through the concept of *embedded* icons.

Notice that a *Geographical View* icon editor contains a place for an embedded :ref:`Coastlines <mcoast_icon>` icon. If you drop a `Coastline <https://confluence.ecmwf.int/display/METV/Coastlines>`_ 's icon here and apply the changes, then the *Geographical View* icon will use your chosen coastlines.

.. image:: /_static/customising_your_plot/embedded-coastlines-icon.png

Try it with your *land_shade* and *polar_europe* icons, and test the result by visualising *polar_europe*. 
Note that your two icons are now *linked* - if you modify *land_shade*, the changes will be picked up the next time you visualise *polar_europe*. 
Another type of embedded icon is discussed in `Analysis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.

Creating a Simple Macro
***********************

Metview incorporates a powerful :ref:`Macro <macro_lang>` language, which can be used for tasks ranging from simple automation of tasks to complex post-processing of data. We will now create a simple macro which reads the GRIB file and plots it in our chosen projection.

Create a new *Macro* icon and edit it. 
This time we see a code editor, custom-built for the Macro language. The editor can automatically translate Metview icons into Macro code, so do the following:

* drop the *t1000.grb* icon into the Macro Editor; a variable called ``t1000_2e_grb`` is assigned to the value of the ``read()`` command, which reads the GRIB data. Such variable names are based on the names of the icons used to generate them, but with non-permitted characters replaced by their hexadecimal code (in this case, the dot in the filename is replaced with 2e).

* rename the variable to simply be ``t1000``

* drop your *polar_europe* icon into the Macro Editor

* underneath the generated code, type the following line:

.. code-block::

  plot(polar_europe, t1000)

This says, "In the polar_europe view, plot data t1000". Your complete macro should look like this:

.. code-block::

  # Metview Macro
 
  t1000 = read("/path/to/user/metview/training/day_1/a quick tour/t1000.grb")
 
  land_shade = mcoast(
      map_coastline_thickness         : 2,
      map_coastline_land_shade        : "on",
      map_coastline_land_shade_colour : "cream"
      )
 
  polar_europe = geoview(
      map_projection      : "polar_stereographic",
      map_area_definition : "corners",
      area                : [30,-25,50,65],
      coastlines          : land_shade
      )
 
  plot(polar_europe, t1000)

Now run the macro to generate the plot - either directly from the Macro Editor, or by right-clicking on the *Macro* icon and selecting **execute**.

Note that we can put a relative path into the ``read()`` command:

Modifying Layers
****************

Now look at the **Layers** tab again. 
Drag the shaded *Coastlines* layer so that it is above the *t1000.grb* layer - a quick way to mask out the sea points! 
Imagine looking down through the layers from the top to the bottom in order to understand how they work. 
You can also select the *Coastlines* layer and change its transparency value. 
You can also toggle layers on and off using the checkboxes next to them. 
Note that these adjustments are not carried through to the various export image formats (see later).

Future versions of Metview will incorporate more advanced plot-editing facilities available directly from the **Layers** tab. 
You can close the **Display Window** again.

Modifying the Contouring
************************

.. image:: /_static/customising_your_plot/t1000-with-shading.png

Metview provides many ways to style the contours when plotting data. 
These are controlled via the :ref:`Contouring <mcont_icon>` icon. 
This is another visdef icon. Create a new instance of this icon and rename it to shade. Edit it, setting the following parameters:

.. image:: /_static/customising_your_plot/mcont_icon.png

.. list-table::

  * - **Contour Shade**
    - On

  * - **Contour Shade Method**
    - Area Fill

  * - **Contour Shade Max Level Colour**
    - Red

  * - **Contour Shade Min Level Colour**
    - Blue

  * - **Contour Shade Colour Direction**
    - Clockwise

Apply the changes, visualise *t1000.grb* again and drag the shade icon into the **Display Window**.

Our palette is automatically generated from a colour wheel. 
Try setting **Contour Shade Colour Direction** to Anti Clockwise to see the difference in the generated palette.

.. image:: /_static/customising_your_plot/hsl-colour-wheel.png

Creating a Legend
=================
Create a legend by changing the first parameter in the *Contour* editor and dragging the icon into the **Display Window** again:

.. list-table::

  * - **Legend**
    - On

Fixing the Contour Levels
=========================

Now zoom in and out of different areas. W
hat happens to the palette - does it stay constant? 
The default behaviour is to create contours at 10 levels *within the range of data actually plotted*. 
As the area changes, so does the range of values being plotted.
Let's create a palette which will not be altered when we change the area. 
Copy the *shade* icon (either right-click + **duplicate**, or drag with the middle mouse button), and rename the copy '*fixed_t*' by clicking on its title. 
Edit the icon and make the following changes:

.. list-table::

  * - **Contour Level Selection Type**
    - Level List

  * - **Contour Level List**
    - -35/-20/-10/-5/0/5/10/20/35

  * - **Contour Shade Colour Direction**
    - Clockwise

Now when you apply this icon you will see that the palette is fixed wherever you zoom. 
There will probably be parts of the plot which are not filled; this is because our range of contour levels does not cover the whole range of values in the data. 
Change the list of contour levels so that the whole plot will be covered - you only need to add one number to each end of the level list to do this (or else change the current numbers at the ends of the list).

Updating the Macro
==================

Edit your macro icon again and drop the *fixed_t* icon into the editor, aiming the drop so that the code is generated above the ``plot()`` command. 
The code to generate the contouring specification will appear, assigned to the variable ``fixed_t`` (the variable is always named after the icon that was dropped). 
Add this to the end of the plot command:

.. code-block::

  plot(polar_europe, t1000, fixed_t)

Visual definition variables must appear just after the data variables to which they are to be applied. In fact, now that we have a shaded field covering the whole globe, there is no need to shade the land; we can remove the ``coastlines`` element from the ``polar_europe`` definition. 
We will still see the coastlines, but Metview will use the default coastline definition, which is to draw the outline without shading the sea or the land.

Overlaying Another Field
************************

.. image:: /_static/customising_your_plot/t1000-and-z500.png

We will now overlay our plot with fields of geopotential.

Copy the geopotential GRIB data file into your Metview directory (``~/metview``); if you are attending the training course at ECMWF, then you can instead type the following command in a terminal window:

.. code-block::

  cp ~trx/mv_data/z500.grb $HOME/metview/training/day_1

You should see the new GRIB icon in your ``day_1`` folder. 
Move this icon into the folder you are working in.

Plot your temperature data by running your macro again, then drop *z500.grb* into the **Display Window**. 
The geopotential field appears as blue isolines (the default contouring style) over the shaded temperature field.

We will now change these isolines to black. 
Create a new :ref:`Contouring <mcont_icon>` icon and rename it to black_contour. 
Edit it and set the following:

.. list-table::

  * - **Contour Line Thickness**
    - 2

  * - **Contour Line Colour**
    - Black

  * - **Contour Highlight**
    - Off

Drop this into the **Display Window** - the result is not as intended! 
The new :ref:`Contouring <mcont_icon>` definition was applied to both fields, not just the geopotential. 
Close the **Display Window** and re-run the macro to get us back to the point before we added the geopotential. 
This time, select both the *z500.grb* and *black_contour* icons and drop them together into the **Display Window**. 
This forces the association between the data and the visual definition. 
You might want to remove the temperature isolines by setting **Contour** to Off in the macro.

Extra Work
**********

Contouring
==========

Spend some time exploring the :ref:`Contouring <mcont_icon>` icon. 
Here are some suggestions:

* try different types of shading by setting **Contour Shade Method** and **Contour Shade Technique**. 
  Also try turning off **Contour** so that only the shading is visible, with no isolines.

* shade only the values which are below freezing point

.. image:: /_static/customising_your_plot/conotur-shading-styles.png

Map projections
===============

Create a new *Geographical View* icon (or make a copy of an existing one) and try out some of the different map projections.

.. image:: /_static/customising_your_plot/projections-montage.png

Coastlines
==========

Spend some time exploring the :ref:`Coastlines <mcoast_icon>` icon. Here are some suggestions:

* adjust the grid lines
* plot country boundaries
* plot rivers
* add sea shading

.. image:: /_static/customising_your_plot/boundaries-and-rivers.png

Histogram sidebar
=================

.. image:: /_static/customising_your_plot/histogram-coloured.png

Visualise the temperature data with one of the coloured :ref:`Contouring <mcont_icon>` icons and view the histogram in the **Data** tab of the sidebar (ensure the sidebar is visible if you previously hid it!). At the bottom, there is a control with which you can select to use your :ref:`Contouring <mcont_icon>` icon colours and levels to compute and display the histogram - try it!
