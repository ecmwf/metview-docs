.. _how_to_use_the_weather_symbol_editor_in_metview:

How to use the Weather Symbol Editor in Metview
///////////////////////////////////////////////

.. note::

    The Weather Symbol Editor was introduced in Metview 5.14.0, with   
    further development planned for the future                         

The Weather Symbol Editor is a feature that allows you to add
annotations to Metview plots that will survive plot updates such as
zooming, changes of projection and contouring.

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image1.png
   :width: 5.20833in
   :height: 4.23958in

At ECMWF you need the latest Metview version to try out the editor. The
command to run is::

    module swap metview/new    
    metview                                                            

How to start the symbol editor?
===============================

Start uPlot by visualising something, open the sidebar and select the
**Symbols** tab:

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image2.png
   :width: 2.29167in
   :height: 1.40003in

How to add a new item to the map?
=================================

Just click on the item in the sidebar, the cursor changes into a cross,
then click on the map to add the item.

Lines
-----

When you are creating a line, double click to conclude the creation.

Polylines, curves and fronts
----------------------------

When you are creating a polyline or a curve each left-click on the map
adds a new point and double-click concludes the creation.

What kind of symbol are available?
==================================

Fitted geo-shapes
-----------------

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image3.png
   :width: 2.54167in
   :height: 0.67708in

These are special shapes where all the vertices keep their lat-lon
positions as the projection changes and the edges between them are
**sampled linearly** in lat-lon space. It means that in cylindrical
projection the edges are always straight lines, while in other
projections they might be **curves**. The following table shows how a
fitted geo-shape changes as the projection changes from cylindrical to
polar north:

+----------------------+-----------------------+-----------------------+
| Shape                | Cylindrical           | Polar North           |
+======================+=======================+=======================+
| Geo Line             | |\_scroll_external/   | |\_scroll_external/   |
|                      | attachments/image2021 | attachments/image2021 |
|                      | -9-16_10-32-35-b51a67 | -9-16_10-33-13-a93124 |
|                      | 57b8f4cc69ad18696d209 | 79fd4f60ac63cc240754f |
|                      | 322c8211597a54ff90fd0 | b2da5224184daaadb05ab |
|                      | 41b97bfc51f7d453.png| | b8b8201634e76c54.png| |
+----------------------+-----------------------+-----------------------+
| Geo Polyline         | |\_scroll_external/   | |\_scroll_external/   |
|                      | attachments/image2021 | attachments/image2021 |
|                      | -9-16_10-37-23-0b2a7c | -9-16_10-36-46-02fa14 |
|                      | 9d0df46abf9a48de5ffad | 20282b2da0c8a162bef95 |
|                      | b68723e60387a0982f33f | 050c527371cf16e479361 |
|                      | 8d899d5189a1beb8.png| | 00d2eba1440d962d.png| |
+----------------------+-----------------------+-----------------------+
| Geo Polygon          | |\_scroll_external    | |\_scroll_external/   |
|                      | /attachments/image202 | attachments/image2021 |
|                      | 1-9-16_10-38-0-d131d6 | -9-16_10-38-26-0aff38 |
|                      | 98ca79b921062135eeadc | c49a0da3ae8e45ef275b6 |
|                      | e6d4dfc12038212396911 | a3b815a79b1ccdbbf67d4 |
|                      | ca6635b84c13a53a.png| | 30e6054a114f1b9c.png| |
+----------------------+-----------------------+-----------------------+
| Geo Quad             | |\_scroll_external/   | |\_scroll_external/   |
|                      | attachments/image2021 | attachments/image2021 |
| *The corner points   | -9-16_10-40-15-9c1fb1 | -9-16_10-40-38-8fb50c |
| always form a        | 6a20c6b1a5d73b8577733 | 45928abeef50b9fff3ad4 |
| rectangle in the     | e9111f6697a3a53b6f8db | 84d0665483806a4054859 |
| lat-lon space. *     | ee417b99658fd733.png| | 7c7dff4fc2bfa7e2.png| |
+----------------------+-----------------------+-----------------------+

Geo shapes
----------

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image12.png
   :width: 2.54167in
   :height: 0.67708in

In these shapes all the vertices keep their lat-lon positions as the
projection changes and they are always connected with a **straight
line** (or with a B-Spline for curves) in all the projections.

The **geo rectangle** is a special object because it always keeps its
rectangular shape. It means that if we zoom, the lat-lon positions of
the corner points do not change. However, if we change the projection
the lat-lon positions of the corners are automatically adjusted so that
the shape will be a rectangle in the new projection.

+----------------+--------------------------+--------------------------+
| Object         | Cylindrical              | Polar North              |
+================+==========================+==========================+
| Line           | |\                       | |\_                      |
|                | _scroll_external/attachm | scroll_external/attachme |
|                | ents/image2021-9-16_13-3 | nts/image2021-9-16_13-3- |
|                | -0-f244510931c40cd1d3942 | 28-a5fc1ee6acf3dd0445d02 |
|                | 88409091dd8b2ec6ca8ad512 | 58bc759e1b8c7c501b9b957b |
|                | e7e4958229b2ce7f1d2.png| | 0d5400242cf7ce592e0.png| |
+----------------+--------------------------+--------------------------+
| Geo rectangle  | |\_s                     | |\_s                     |
|                | croll_external/attachmen | croll_external/attachmen |
|                | ts/image2021-9-16_10-51- | ts/image2021-9-16_10-52- |
|                | 45-e72412a124b41c49472e5 | 14-a5d9cf1c19153d3bf15e4 |
|                | 23ba138d60a4ac654a9fca9f | 154f4e2be1ef19d6223d26f6 |
|                | e3e6807f0218b714235.png| | 4deb02ff3b0006d2b51.png| |
+----------------+--------------------------+--------------------------+

Markers and text
----------------

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image17.png
   :width: 2.47917in
   :height: 0.6875in

For these objects only the anchor point (see below) keeps its lat-lon
position as the projection changes, while the extent is defined in terms
of pixels:

+------------+----------------------------+----------------------------+
| Object     | Cylindrical                | Polar North                |
+============+============================+============================+
| Text       | |\_scroll_external/        | |\_scroll_external         |
|            | attachments/image2021-9-16 | /attachments/image2021-9-1 |
|            | _13-5-35-767a0ed0eeab0431c | 6_13-6-1-fa6df9a6d791cfebf |
|            | d2c64d486608a7f3c55c6ea0a2 | be552b85ac1fa35aafceabff8f |
|            | 0c4c8e2340fcbd4376027.png| | d14dbcde16ab6fec278e5.png| |
+------------+----------------------------+----------------------------+
| Placemark  | |\_scroll_external/        | |\_scroll_external/        |
|            | attachments/image2021-9-16 | attachments/image2021-9-16 |
|            | _13-7-48-38ef98294cc7fe2dd | _13-7-29-92b632672f1dfa9d8 |
|            | de05479c11004e6ae3def2cdf4 | d80aebee74ff867c4938f8238b |
|            | cd65940f29b84b9e26541.png| | d76d58b1f6910554b87a0.png| |
+------------+----------------------------+----------------------------+

The anchor position depends on the object type:

-  for a text box it is the top left corner

-  for a placemark it is the tip of the symbol (bottom-centre)

-  for the other shapes it is the centre

Surface analysis
----------------

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image22.png
   :width: 2.73958in
   :height: 0.94792in

This is a collection of standard meteorological curves and symbols.

WMO symbols
-----------

All the WMO weather symbols are available here. They behave like
markers, i.e. their centre keeps its lat-lon position when the
projection changes and the extent is defined in pixels.

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image23.png
   :width: 2.9375in
   :height: 2.47917in

Can I add my own symbols?
=========================

You can use any square shaped SVG or PNG file as a symbol. These have to
be added to the **System/Symbols** folder in your Metview home
directory. On top of that you can also use symbols from the directory
specified by the **METVIEW_EXTRA_FEATURE_SYMBOLS_DIR** environment
variable. When you start a uPlot window it scans these directories and
adds all the files with .*svg or \*.png  suffix to the **Markers and
text** group in the Symbols sidebar.

How can I edit the symbols?
===========================

First, make sure you are not in zoom mode, because clicks will be taken
as zooms! Single click on the symbol: it gets into edit mode where you
can move and resize it and edit its graphical properties from the
**ribbon editor** at the top of the view area. Note that the filled
shapes allow you to remove the filling and just keep the outline. Also
note that all the 'line' objects can have arrow heads.

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image24.png
   :width: 3.7502in
   :height: 2.60417in

How can I edit the points on a polyline, curve or front?
========================================================

Double click the symbol and the control points become visible. You can
drag them now to a new location.

|\_scroll_external/attachments/image2021-9-16_13-12-26-d17addfe0a7aa67794c455c00a5949fad115501aed49746a197e77ea2a6e5499.png|\ |\_scroll_external/attachments/image2021-9-16_13-13-18-c427ec1536f2505cda5c0f426c44a060c17dbbb11baca056a8ee7c24e30164fe.png|

You can **add/remove** points to a curve when you are in the point edit
mode. Right click on a control point and use the actions in the context
menu:

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image27.png
   :width: 2.57365in
   :height: 2.60417in

How can I edit the text?
========================

The text item has two modes: a **normal mode** and an **edit mode**
where the text can be interactively typed in or altered. In edit mode a
frame is rendered around the text item to distinguish it from the normal
mode.

|\_scroll_external/attachments/image2021-11-25_13-3-15-462da741982224186391fd5888a05bb961f1c1c9b2ac07f730fed821653a84ef.png|\ |\_scroll_external/attachments/image2021-11-25_13-3-43-7a33ab0df2f46cf78a2a4a1368f2631202342860dd77bd01b3df847203e4ab28.png|

To enter the edit mode double-click on the item. To leave the edit mode
click outside the item. You can also drag an edited item by the editor
frame (the item will switch automatically into normal mode). Please note
that when a text item is created it automatically appears on the screen
in edit mode.

How do I add an arrow?
======================

Just add any of the line objects (including polylines) and go to the
property editor to add arrow heads to either or both ends of the line.

Can I rotate the objects?
=========================

It is not yet available.

Is redo-undo available?
=======================

Yes, there is a redo-undo functionality for all the symbol operations.
You can access it via the toolbar buttons or using the Ctrl+Z (undo)
Shift+Ctrl+Z (redo) shortcuts:

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image30.png
   :width: 3.125in
   :height: 0.51764in

Please note that when performing zoom or dropping an icon into the plot
the undo history is cleared.

Can I drag symbols out of the map area?
=======================================

It is only possible for the **markers, the text and the WMO symbols**.
The other symbols and shapes are all **clipped** to the map area, so any
parts outside of it become invisible. The policy is even stricter for
the **fitted geo shapes**: these are fully bound to the map area and
none of their points or edges can be moved outside!

How does clipping work?
=======================

The clipping policy is based on the object type.

For **markers, text and WMO symbols** no clipping is applied. However,
when we zoom the following things happen:

-  items that were outside the map area stay at their scene (i.e.
   window) position

-  items that were inside the map area before zoom but get out of the
   map will be hidden. They become visible again when we unzoom.

The snapshots below illustrates how it works.

|\_scroll_external/attachments/image2021-12-9_8-38-11-b7f3d8d4371aaf1fc47129c5b4537281cdce0cbbfd50ae9abde7262963e6030a.png|\ |\_scroll_external/attachments/image2021-12-9_8-46-22-e6ac5031d4af861840d9a5c6d34e153cd0907b63916488de3345b797801b8e9d.png|\ |\_scroll_external/attachments/image2021-12-9_8-46-46-31782c0978188bc33e97f026c394c049e6cf0d257092300ab066f96cbcfe8e31.png|

For all the other types **clipping is always applied** (the example
below shows how it works for a cold front).

|\_scroll_external/attachments/image2021-12-9_8-57-56-a31fe8bcdc2ac825f2796a799d59fc45a0cbb728ea1b3db62b5de95443f81201.png|\ |\_scroll_external/attachments/image2021-12-9_8-58-19-25692faf4c967b92f0ec95667bdb8e7a224fde4749ebf1e0c17f73faf002c36e.png|\ |\_scroll_external/attachments/image2021-12-9_8-58-37-aa86d36e2a030060c9f7e559a69210d414b1c5dfebe24f58edf35e525cbe5b94.png|

**Fitted geo shapes** are fully bound to the map area and none of their
points or edges can be moved outside! 

How to generate a PNG or PDF from the scene?
============================================

Just use the **Export** button in the toolbar and choose between the
PDF_QT or PNG_QT output formats.

Alternatively, just take a screenshot!

Can I save the edited objects for later reuse?
==============================================

It is not possible at the moment, so you will lose all the objects when
you close the uPlot window.

How do these features behave across different time steps in the plot?
=====================================================================

The symbols are preserved as they are between time steps; you cannot
define different sets of symbols, or move them between time steps.

Feedback
========

If at ECMWF, you should be able to see the `Weather Symbol Editor
feedback
page <https://confluence.ecmwf.int/display/METV/Weather+Symbol+Editor+feedback+page>`__
- please leave any comments there!

.. |\_scroll_external/attachments/image2021-9-16_10-32-35-b51a6757b8f4cc69ad18696d209322c8211597a54ff90fd041b97bfc51f7d453.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image4.png
   :width: 1.93889in
   :height: 1.24125in
.. |\_scroll_external/attachments/image2021-9-16_10-33-13-a9312479fd4f60ac63cc240754fb2da5224184daaadb05abb8b8201634e76c54.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image5.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-37-23-0b2a7c9d0df46abf9a48de5ffadb68723e60387a0982f33f8d899d5189a1beb8.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image6.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-36-46-02fa1420282b2da0c8a162bef95050c527371cf16e47936100d2eba1440d962d.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image7.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-38-0-d131d698ca79b921062135eeadce6d4dfc12038212396911ca6635b84c13a53a.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image8.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-38-26-0aff38c49a0da3ae8e45ef275b6a3b815a79b1ccdbbf67d430e6054a114f1b9c.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image9.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-40-15-9c1fb16a20c6b1a5d73b8577733e9111f6697a3a53b6f8dbee417b99658fd733.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image10.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_10-40-38-8fb50c45928abeef50b9fff3ad484d0665483806a40548597c7dff4fc2bfa7e2.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image11.png
   :width: 1.93889in
   :height: 1.31631in
.. |\_scroll_external/attachments/image2021-9-16_13-3-0-f244510931c40cd1d394288409091dd8b2ec6ca8ad512e7e4958229b2ce7f1d2.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image13.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_13-3-28-a5fc1ee6acf3dd0445d0258bc759e1b8c7c501b9b957b0d5400242cf7ce592e0.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image14.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_10-51-45-e72412a124b41c49472e523ba138d60a4ac654a9fca9fe3e6807f0218b714235.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image15.png
   :width: 1.53125in
   :height: 0.91667in
.. |\_scroll_external/attachments/image2021-9-16_10-52-14-a5d9cf1c19153d3bf15e4154f4e2be1ef19d6223d26f64deb02ff3b0006d2b51.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image16.png
   :width: 1.53125in
   :height: 0.91667in
.. |\_scroll_external/attachments/image2021-9-16_13-5-35-767a0ed0eeab0431cd2c64d486608a7f3c55c6ea0a20c4c8e2340fcbd4376027.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image18.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_13-6-1-fa6df9a6d791cfebfbe552b85ac1fa35aafceabff8fd14dbcde16ab6fec278e5.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image19.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_13-7-48-38ef98294cc7fe2ddde05479c11004e6ae3def2cdf4cd65940f29b84b9e26541.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image20.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_13-7-29-92b632672f1dfa9d8d80aebee74ff867c4938f8238bd76d58b1f6910554b87a0.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image21.png
   :width: 1.53125in
   :height: 1.0625in
.. |\_scroll_external/attachments/image2021-9-16_13-12-26-d17addfe0a7aa67794c455c00a5949fad115501aed49746a197e77ea2a6e5499.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image25.png
   :width: 1.875in
   :height: 1.83333in
.. |\_scroll_external/attachments/image2021-9-16_13-13-18-c427ec1536f2505cda5c0f426c44a060c17dbbb11baca056a8ee7c24e30164fe.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image26.png
   :width: 1.875in
   :height: 1.83333in
.. |\_scroll_external/attachments/image2021-11-25_13-3-15-462da741982224186391fd5888a05bb961f1c1c9b2ac07f730fed821653a84ef.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image28.png
   :width: 2.08333in
   :height: 1.28808in
.. |\_scroll_external/attachments/image2021-11-25_13-3-43-7a33ab0df2f46cf78a2a4a1368f2631202342860dd77bd01b3df847203e4ab28.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image29.png
   :width: 2.08333in
   :height: 1.28808in
.. |\_scroll_external/attachments/image2021-12-9_8-38-11-b7f3d8d4371aaf1fc47129c5b4537281cdce0cbbfd50ae9abde7262963e6030a.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image31.png
   :width: 2.60417in
   :height: 2.01042in
.. |\_scroll_external/attachments/image2021-12-9_8-46-22-e6ac5031d4af861840d9a5c6d34e153cd0907b63916488de3345b797801b8e9d.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image32.png
   :width: 2.60417in
   :height: 1.94792in
.. |\_scroll_external/attachments/image2021-12-9_8-46-46-31782c0978188bc33e97f026c394c049e6cf0d257092300ab066f96cbcfe8e31.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image33.png
   :width: 2.60417in
   :height: 2.23958in
.. |\_scroll_external/attachments/image2021-12-9_8-57-56-a31fe8bcdc2ac825f2796a799d59fc45a0cbb728ea1b3db62b5de95443f81201.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image34.png
   :width: 2.60417in
   :height: 1.77282in
.. |\_scroll_external/attachments/image2021-12-9_8-58-19-25692faf4c967b92f0ec95667bdb8e7a224fde4749ebf1e0c17f73faf002c36e.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image35.png
   :width: 2.60417in
   :height: 1.77282in
.. |\_scroll_external/attachments/image2021-12-9_8-58-37-aa86d36e2a030060c9f7e559a69210d414b1c5dfebe24f58edf35e525cbe5b94.pn.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image36.png
   :width: 2.60417in
   :height: 1.77282in
