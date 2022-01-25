.. _layout_in_metview:

Layout in Metview
#################

**Download**

The download for this session is contained on the page :ref:`Analysis Views  <analysis_views>`.

Plot Layout 
************

Sophisticated layouts are possible in Metview, with multiple plots on a single page as shown below:

.. image:: /_static/layout_in_metview/Picture8.png

To demonstrate the layout facility in Metview, let's re-create the above plot. 
The Display Window icon allows us to design a layout, and also to choose the size of the page (e.g. A4).
 
.. image:: /_static/layout_in_metview/SUPERPAGE.png

Instantiate a new Display Window icon and edit it. 
This is what you will produce over the next few steps:

.. image:: /_static/layout_in_metview/image2015-3-6_11-27-12.png

Click on the **Add new frame** button to create the first frame. 
By default, this contains just a single plot scene which uses a *Geographic View*. 
Select (left-click) this plot scene and click **Expand selected frames** to make it fill the whole area. 
Divide it up into three areas as follows:

* click **Split selected frames**, select **2x1** in order to obtain two vertically stacked frames and click **OK**.

* select (left-click) the lower frame, click **Split selected frames** and select **1x2**.

Give a different *View* to each scene:

* drag a *Cross Section View* icon (either one you previously created or else a new one) into the top scene.

* drag a *Vertical Profile View* icon into the bottom-left scene.

* drag a *Geographic View* icon into the bottom-right scene.

**Save** the changes and **Visualise** this icon. 
Drag the *t_fc96.grib* icon into all three of the scenes in the **Display Window** (each of the frames defined in the editor is referred to as a scene in the **Display Window**. 
Apply some *Visdefs*: 

* drag the *shade* icon into the cross section scene.

* drag the *vdline* icon into the vertical profile scene. 

Your result should look something like the plot at the start of this section.

If you look at the **Frames** and, more interestingly, the **Layers** tabs, you will see that they are linked to only one of these scenes at a time. Try using the **Active scene** control to change which one is used (you can visually highlight the active scene from the **View** menu). 
You can also right-click on a scene and choose "Select as active scene" from the context menu.

Generate a macro from this plot by clicking on the **Generate macro** button in the toolbar. 
This is a great way to interactively design a plot layout and then create a macro which uses it. 
To run it on a day-to-day basis, probably only the data file reading step would have to be modified.

Legend    
******

.. image:: /_static/layout_in_metview/MLEGEND.png

Legends are an important part of any scientific and operational plot. 
If enabled, an automatic legend will be built from the data provided.

To enable a legend, parameter **Legend** needs to be set to **On**. 
This parameter is available in some of the *Visual Definition* icons (e.g. *Contouring*, *Graph Plotting* and *Wind Plotting*).

To specify how a plot's legend is displayed, Metview provides a specific icon, named :ref:`Legend <mlegend_icon>`. 
This controls features such as the legend's position, style and fonts. To demonstrate the *Legend's* concept, do the following:

* **Visualise** icon *t_fc24.grib*.

* drop icon shade into the **Display Window** (verify that parameter **Legend** is set to **On**).

The result shows a default legend sitting at the top of the plot. Let's move the plot legend into a column at the right of the map. 
Create a new *Legend* icon and rename it to *legright*. 
Edit it, and set:

.. list-table::

  * - **Legend Automatic Position**
    - Right

Drop it into the **Display Window** to see the result.

We can also manually set the position of the legend by setting the following parameters, noting that the position of the legend is specified in cm from the bottom-left corner of the page, and that the default page size is A4 (29.7cm x 21cm):

.. list-table::

  * - **Legend Box Mode**
    - Positional

  * - **Legend Box X Position**
    - 5

  * - **Legend Box Y Position**
    - 2

  * - **Legend Box X Length**
    - 20

  * - **Legend Box Y Length**
    - 2

.. list-table::

  * - .. image:: /_static/layout_in_metview/Picture9.png
    - .. image:: /_static/layout_in_metview/legend-right.png
    - .. image:: /_static/layout_in_metview/legend-pos.png
  
  * - **Automatic legend, top**
    - **Automatic legend, right**
    - **Positional Legend**

Note that the direction of the legend, by default, is computed automatically depending on the longest dimension of its positional box  It can also be manually set in the *Legend* icon.

Annotation View    
***************

.. image:: /_static/layout_in_metview/ANNOTATIONVIEW.png

The :ref:`Annotation View <annotationview_icon>` icon provides a container for user-defined text boxes. 
This view can also be used for layout purposes - if no user text is defined then an empty box will be created in the Display Window / paper sheet.

.. image:: /_static/layout_in_metview/annotation-view-plot.png


The user-defined text is provided by means of a :ref:`Text Plotting <mtext_icon>`  icon.

.. image:: /_static/layout_in_metview/MTEXT.png

Create a new *Annotation View* icon and visualise it - the **Display Window** will be empty. 

Now create a new *Text Plotting* icon and rename it to note1. 
Edit it, setting the following parameters:

.. list-table::

  * - **Text Line 1**
    - Metview Training Course

  * - **Text Mode**
    - Positional

  * - **Text Box X Position**
    - 10

  * - **Text Box Y Position**
    - 10

  * - **Text Box X Length**
    - 5

  * - **Text Box Y Length**
    - 5

  * - **Text Border**
    - On

**Apply** the changes and drag this icon into the **Display Window**.

Multiple *Text Plotting* icons can be placed in this *View*:

* duplicate the *note1* icon and rename it to *note2*.

* customise it by changing for instance the font style and size (remember to re-define an appropriate text box).

* drag it into the **Display Window**.

Extra work
**********

.. note::

  If you are attending the training course at ECMWF, please also consider the extra tasks in :ref:`Analysis Views  <analysis_views>`.


Create an A3 version of your plot layout
========================================

Copy your *Display Window* icon from the 3-plot exercise and set its paper size to A3 (**page setup** button).

Create a custom size plot, projection Mollweide
===============================================

At global size, the Mollweide map is much wider than it is high. 
Create a new *Display Window* and experiment with a custom paper size until most of the white space has been removed from around the plot.

Customise the size of the map/view area
=======================================
The automatic placement of the legend may not always be perfect for your particular plot. 
When we set the legend to be on the right-hand side of the map, there may not have been enough room for it. We can fix this by reducing the amount of space that the map takes up. 
Each view icon has a set of parameters to set the size and placement of the "subarea". 
This is the area on the physical page occupied by the view. 
These parameters are defined in percentage of the page size. 
Try setting **Subpage X Length** to 80, then plot some shaded data and apply your *legright* icon to it to confirm that it now fits better.

Geographic and annotation view, side-by-side
============================================

Try and reproduce the following plot:

.. image:: /_static/layout_in_metview/layout-2.png

Five Profiles
=============

Create a layout with 5 Vertical Profile views, each showing a profile for a different location.
