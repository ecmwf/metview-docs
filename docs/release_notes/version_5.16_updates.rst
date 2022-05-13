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

* Improved data sampling near orography when using model level data and height vertical axis in :ref:`Cross Section Data <mcross_sect_icon>` and :ref:`Cross Section View <mxsectview_icon>`. Implemented by the following changes:

   * The "count" and "level_list" options for the ``level_selection`` parameter were made available for user defined vertical coordinates too (when ``vertical_coordinates`` is "user")
   * Added new parameter ``vertical_coordinate_extrapolate_mode``:  controls the extrapolation at the top and bottom of the coordinate range for user defined vertical coordinates (when ``vertical_coordinate`` is "user"). The possible options are "constant" and "linear".
   * Added new parameter ``vertical_coordinate_extrapolate_fixed_sign``: for the "linear" extrapolation mode it controls whether the extrapolated values can differ in sign from the values on the nearest input levels. When it is “on” it prevents e.g. wind components to change sign due to extrapolation.
   * Fixed issue when 3D wind way displayed at incorrect levels when using model level data and height vertical axis

   See the :ref:`gallery example <gallery_cross_section_wind3d_height_ml_orog>`.

* In wind mode it is now mandatory to have the same number of input levels for all the required wind components

**Hovmoeller**

* Several improvements were made to the vertical Hovmeller diagrams in :func:`mhovmoeller_vertical` and :func:`mhovmoellerview`:

   * To display model level input with pressure vertical axis the input now **must contain** an LNSP (Logarithm of Surface Pressure) field. Previously it was not required but a fixed surface pressure value was used instead (internally), which led to incorrectly computed pressure levels.
   * Added new parameter ``input_mode`` to control how the input data is extracted. The possible values are "area", "point" and "nearest_gridpoint". To specify the location for the last two modes the ``point`` parameter was added.
   * Added a new mode "user" to ``vertical_level_type`` to enable the usage of arbitrary vertical coordinate fields. These fields are identified by the ecCodes paramId specified in ``vertical_coordinate_param``.
   * Added new parameter ``vertical_coordinate_extrapolate`` to control the extrapolation at the top and bottom when ``vertical_level_type`` is "user".
   * Added new parameter ``vertical_coordinate_extrapolate_mode`` to controls the extrapolation. The possible options are "constant" and "linear".
   * Added new parameter ``vertical_coordinate_extrapolate_fixed_sign``: for the "linear" extrapolation mode it controls whether the extrapolated values can differ in sign from the values on the nearest input levels. When it is “on” it prevents e.g. wind components to change sign due to extrapolation.

   See the :ref:`gallery example <gallery_vert_hovm_ml_in_pressure>`.  
   See the :ref:`gallery example <gallery_vert_hovm_ml_in_height>`. 


**Macro/Python**

* :func:`mean` and :func:`sum` now have an option called ``missing`` to control how to handle missing values during the computations. By default ``missing`` is False, which means that if at a gridpoint there is a missing value in any of the input fields the output will contain a missing value at that gridpoint. However, when ``missing`` is True all the non-missing values are used to form the mean/sum at a given gridpoint. 

See the :ref:`gallery example <gallery_sst_mean_with_missing_value>`.
