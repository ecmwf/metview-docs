.. _ws_add_your_symbol:

Adding your own weather symbols
====================================

.. note::

    Adding your own Interactive Weather Symbols was introduced in Metview 5.15.0.


You can use any square shaped SVG or PNG file to define a new Weather Symbol Object type. These images can be placed in two possible directories:

* The primary directory is **System/Symbols/images** in your Metview home directory.

* You can also specify an extra directory using the **METVIEW_EXTRA_FEATURE_SYMBOLS_DIR** environment variable. If it is defined and it has an **images** subdirectory its contents will be scanned for user defined images.

**System/Symbols/images** takes precedence over the extra directory, so if they both contain an image with the same name the one from the extra directory will not be available as a symbol type!

When you start Metview's plot window it scans these directories and
adds all the files with .*svg or \*.png  suffix to the **Images** group in the Symbols > Types sidebar: 

.. image:: /_static/ug/ws_add_your_symbol/images_group.png
   :width: 200px

.. note::

    These symbols are static in a sense that you can only change their size in the plot and no styling is available for them.
