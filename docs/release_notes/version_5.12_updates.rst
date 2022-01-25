.. _version_5.12_updates:

Version 5.12 Updates
////////////////////


Upcoming Version 5.12.1
=======================

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2021-06-17
* Became metview/new at ECMWF on 2021-06-17 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2021-06-17**

   -  Built
      with **Magics** `4.8.2 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.22.1 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.22.1+released>`__

   -  Built with **ODC** version **1.3.0**

   -  Includes
      version `1.7.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

   -  Includes MetZoom beta 0.9.2

**Fixes:**

-  fixed issue where a Geopoints variable created via the create_geo()
   function with an elevation column did not list 'elevation' as one of
   its columns, nor did it write the elevation column to disk

-  fixed issue where the Geopoints Examiner only showed one station id
   in the stnid column

-  fixed issue where the setting 'Order' to 'Sorted' in the :func:`read`
   command 
   did not work properly with fields of daily climatologies

-  fixed issue where the :ref:`Symbol
   Plotting <msymb_icon>`
   icon/function did not honour symbol_text_blanking in 'advanced' mode
   (fix is in Magics 4.8.2)

-  allow environment variable METVIEW_MARS_CONFIG_POSTFIX to specify
   different config files for testing different MARS configurations

Version 5.12.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2021-05-19
* Became metview/new at ECMWF on 2021-05-19 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2021-05-19**

   -  Built
      with **Magics** `4.8.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.22.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.22.0+released>`__

   -  Built with **ODC** version **1.3.0**

   -  Includes
      version `1.7.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

   -  Includes MetZoom beta 0.9.2

**Documentation:**

-  try out the all-new documentation for the Python interface on
   `readthedocs <https://metview.readthedocs.io/en/latest/index.html>`__!


.. image:: /_static/release/version_5.12_updates/image1.png
   :width: 4.05208in
   :height: 2.60417in
  
.. image:: /_static/release/version_5.12_updates/image2.png
   :width: 3.20833in
   :height: 2.60417in
  
.. image:: /_static/release/version_5.12_updates/image3.png
   :width: 3.20833in
   :height: 2.60417in


**Cross Section:**

-  allow the plotting of horizontal wind as arrows/flags along transect
   plane via the setting::
      
      wind_unprojected = "on"

   See new gallery example :ref:`here <gallery_cross_section_wind_unprojected>` 

**Plotting:**

-  new option in the PNG and PDF output drivers: output_font_scale -
   takes a floating point number, default=1. To double the size of all
   text generated in the plots, for example, set it to 2.0 in the call
   to setoutput, or from the GUI.

**Regrid:**

-  new interpolation methods and slight renaming of parameters -
   see :ref:`Regrid <regrid_icon>`

-  now accepts NetCDF files as input; will accept 'simple' grids in
   NetCDF files at least, we have not tried all types!

**Thermo Data:**

-  fixed issue where the result returned in Python was not complete




