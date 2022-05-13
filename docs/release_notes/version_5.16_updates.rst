.. _version_5.16_updates:

Version 5.16 Updates
////////////////////


Version 5.16.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-05-xx
* Became metview/new at ECMWF on 2022-05-xx (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-05-xx**

   -  Built
      with **Magics** `4.11.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.25.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.25.0+released>`__

   -  Built with **ODC** version **1.4.4**

   -  Includes
      version `1.11.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface

  
**Cross Section**

* Improved data sampling near orography when using model level data and height vertical axis by implementing the following changes for :ref:`Cross Section Data <mcross_sect_icon>` and :ref:`Cross Section view <mxsectview_icon>`:

   * the "count" and "level_list" options for the ``level_selection`` parameter were made available for user defined vertical coordinates too (when ``vertical_coordinates`` is "user")
   * new parameter ``vertical_coordinate_extrapolate_mode``:  controls the extrapolation at the top and bottom of the coordinate range for user defined vertical coordinates (when ``vertical_coordinate`` is "user"). The possible options are "constant" and "linear".
   * new parameter ``vertical_coordinate_extrapolate_fixed_sign``: for the "linear" extrapolation mode it controls whether the extrapolated values can differ in sign from the values on the nearest input levels. When it is “on” it prevents e.g. wind components to change sign due to extrapolation.
   * fixed issue when 3D wind way displayed at incorrect levels when using model level data and height vertical axis

   See the :ref:`gallery example <gallery_cross_section_wind3d_height_ml_orog>`.

* In wind mode it is now mandatory to have the same number of input levels for all the required wind components

**Vertical Computations**
