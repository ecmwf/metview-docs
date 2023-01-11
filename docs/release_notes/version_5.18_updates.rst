.. _version_5.18_updates:

Version 5.18 Updates
////////////////////


Version 5.18.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2023-xx-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.xx.xx.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2023-xx-xx**

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
* fixed issue when :func:`mhovmoeller_vertical` randomly crashed
  
  
**Plotting**

* streamlines: fixed issue when the arrowhead direction on the streamlines was inconsistent 

**Python/Macro**

* fixed issue when :func:`sort` called form Macro unnecessarily repacked the messages in the resulting :class:`Fieldset`
* fixed issue when :func:`float` repacked the input messages 
  
**User interface**

* added Python code preview mode for icon editors:
 
   .. image:: /_static/ui/editor_python_preview.png
      :width: 280px

* added syntax highlighting to text edit mode for icon editors:

   .. image:: /_static/ui/editor_text_mode.png
      :width: 280px

* added button to access online documentation for icon editors:

   .. image:: /_static/ui/editor_doc_link.png
      :width: 350px

* issues warning when the value of a list parameter contains a comma in the icon editor. While the list separator is a comma in script (Python or Macro), it is '/' in the user interface. So if a comma appears in a list it was most probably put there by mistake.  

   .. image:: /_static/ui/editor_list_separator_warning.png
      :width: 350px

* :func:`eccharts`: added new layer called "tcw" (Total Column Water)
* :func:`mcont`: add style "sh_tcw_f5t100" to the predefined list of styles for parameter ``contour_style_name``
* added the **Properties** context menu action to icons. It brings up a dialog showing the file properties and offering an editor for symbolic links.
* gzip and bzip2 files are now represented by an icon in the user interface. The supported context menu actions: "Compress", "Extract here" and "Extract to subfolder"
* added the "Extract here" and "Extract to subfolder" actions to all the supported archive formats (tar, tgz, tbz, tz, zip)
* fixed issue when the "examine" command did not work on archive (tar, tgz, tbz, zip) icons on macOS
* fixed issue when a broken link to a folder could be opened/entered
* fixed issue when double clicking on a Desktop icon caused a crash
* GRIB Examiner: fixed issue when used too much memory for large GRIB fields in the Values tab. With this change data is only loaded into the Values tab when there are no more than 7 million values in the GRIB field. Otherwise a warning message is displayed:

   .. image:: /_static/ui/grib_examiner_values_limit_warning.png
      :width: 320px
* GRIB Examiner: improved speed and memory usage when loading data for the Values tab
  
**Code editor**

* Documentation web links now point to pages on Read The Docs

**New Gallery Examples**

   .. image:: /_static/gallery/t2_animation.gif
      :width: 300px
      :target: ../gen_files/gallery/t2_animation.html


   .. image:: /_static/gallery/rotating_geos_globe_animation.gif
      :width: 300px
      :target: ../gen_files/gallery/rotating_geos_globe_animation.html