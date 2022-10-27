.. _version_5.18_updates:

Version 5.18 Updates
////////////////////


Version 5.18.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-xx-xx
* Became metview/new at ECMWF on 2022-xx-xx (Linux desktops, ecgate, lxc, lxop, Cray HPC)
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2022.xx.xx.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2022-xx-xx**

   -  Built
      with **Magics** `4.12.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.27.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.27.0+released>`__

   -  Built with **ODC** version **1.4.6**

   -  Includes
      version `1.13.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface

**Hovmoller**

* Area and Vertical Hovmoeller: added new parameter ``area_statistics`` to define the computation performed in the ``area``. See ::func:`mhovmoeller_area`,  :func:`mhovmoeller_vertical` and :func:`mhovmoellerview` See the :ref:`gallery example <gallery_hovmoeller_stats>`:

   .. image:: /_static/gallery/hovmoeller_stats.png
      :width: 350px
      :target: ../gen_files/gallery/hovmoeller_stats.html

* fixed issue when dropping a matching Hovmoeller Data icon into a :func:`mhovmoellerview` window an empty plot was produced
* fixed issue when plotting a Hovmoeller Data object into a non-matching :func:`mhovmoellerview` in a script resulted in a crash. Now an error message is generated.
  
  
**Plotting**

* streamlines: fixed issue when the arrowhead direction on the streamlines was inconsistent 

**Python/Macro**

* fixed issue when :func:`sort` called form Macro unnecessarily repacked the messages in the resulting :class:`Fieldset`
* fixed issue when :func:`float` repacked the input messages 
* fixed issue when the ``POLAR_VECTOR`` and ``XY_VECTOR`` output modes did not work in :func:`bufr_picker`

**User interface**

* :func:`eccharts`: added new layer called "tcw" (Total Column Water)
* :func:`mcont`: add style "sh_tcw_f5t100" to the predefined list of styles for parameter ``contour_style_name``
* added the Properties context menu action to icons. It brings up a dialog, which shows the file properties and offers and editor for symbolic links.
* gzip and bzip2 files are represented by an icon in the user interface. The supported context menu actions: "Compress", "Extract here" and "Extract to subfolder"
* added the "Extract here" and "Extract to subfolder" actions to all the supported archive formats (tar, tgz, tbz, tz, zip)
* fixed issue when the "examine" command did not work on archive (tar, tgz, tbz, zip) icons on macOS
* fixed issue when the GRIB Examiner used too much memory for large GRIB fields in the Values tab. With this change data is only loaded into the Values tab when there are no more than 7 million values in the GRIB field.
  