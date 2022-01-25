.. _data_overlay:

Data Overlay
////////////

Overlay rules
=============

Metview’s overlay settings determine which data are combined on the same
plot rather than appearing sequentially in the frame list. For example,
we can plot with temperature, geopotential and wind overlaid together.
Metview has some default rules, which can be overridden using the
Overlay Control parameter in the view icons.

.. image:: /_static/ug/data_overlay/image1.png
   :width: 3.64583in
   :height: 2.11486in

To understand what Metview does with data contained in a single data
icon, see Rule 1:

.. note::

    **Rule 1**                                                         
                                                                       
    Multiple data contained in a single icon or file (data unit) are  
    never overlaid                                                     

In practice, this means that a GRIB file with 5 fields is visualised as
5 separate plots which you can scroll through.

If you wish to overlay data, then you must provide separate data icons
for each ‘layer’. Then we are subject to Rule 2:

.. note::

    **Rule 2**                                                         
                                                                       
    Multiple data provided in several data icons are overlaid          
    according to user or system defined overlay control parameters     

Overlay settings
================

The :ref:`Geographical
View <geoview_icon>`
icon contains a parameter **Map Overlay Control**, which determines the
overlay behaviour when plotting multiple data icons together. Its
possible values are:

-  **Always**: fields from different data units are always overlaid; the
   first fields from each data unit form the first plot frame, the
   second fields form the second frame and so on

-  **Never**: fields are never overlaid, but will appear sequentially

-  **By Date**: fields with the same valid date and time will be
   overlaid; there will be one plot frame for each distinct date and
   time across all the data units

-  **By Level**: fields with the same vertical level will be overlaid;
   there will be one plot frame for each distinct level across all the
   data units

The default behaviour is **Always**. This can be changed by modifying
the default Geographical View icon.
