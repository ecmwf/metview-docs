.. _version_5.16_updates:

Version 5.16 Updates
////////////////////


Version 5.16.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-05-18
* Became metview/new at ECMWF on 2022-05-18 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-05-18**

   -  Built
      with **Magics** `4.12.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.26.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.26.0+released>`__

   -  Built with **ODC** version **1.4.5**

   -  Includes
      version `1.12.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface

  
**Cross Section**

* Improved data sampling near orography when using model level data and height vertical axis in :ref:`Cross Section Data <mcross_sect_icon>` and :ref:`Cross Section View <mxsectview_icon>`. Implemented by the following changes:

   * The "count" and "level_list" options for the ``level_selection`` parameter were made available for user defined vertical coordinates too (when ``vertical_coordinates`` is "user")
   * Added new parameter ``vertical_coordinate_extrapolate_mode``:  controls the extrapolation at the top and bottom of the coordinate range for user defined vertical coordinates (when ``vertical_coordinate`` is "user"). The possible options are "constant" and "linear".
   * Added new parameter ``vertical_coordinate_extrapolate_fixed_sign``: for the "linear" extrapolation mode it controls whether the extrapolated values can differ in sign from the values on the nearest input levels. When it is “on” it prevents e.g. wind components to change sign due to extrapolation.
   * Fixed issue when 3D wind way displayed at incorrect levels when using model level data and height vertical axis.

   See the new gallery examples (:ref:`example1 <gallery_cross_section_wind3d_height_ml_orog>` and :ref:`example2 <gallery_cross_section_wind3d_height_ml_with_valleys>`) showcasing some of these options:

   .. image:: /_static/gallery/cross_section_wind3d_height_ml_orog.png
      :width: 250px
      :target: ../gen_files/gallery/cross_section_wind3d_height_ml_orog.html

   .. image:: /_static/gallery/cross_section_wind3d_height_ml_with_valleys.png
      :width: 250px
      :target: ../gen_files/gallery/cross_section_wind3d_height_ml_with_valleys.html

* In wind mode it is now mandatory to have the same number of input levels for all the required wind components

**Vertical Hovmoeller**

* Several improvements were made to the **vertical Hovmoeller** diagrams in :func:`mhovmoeller_vertical` and :func:`mhovmoellerview`:

   * To display model level input with pressure vertical axis the input now **must contain** an LNSP (Logarithm of Surface Pressure) field. Previously it was not required but a fixed surface pressure value was used instead (internally), which led to incorrectly computed pressure levels.
   * Added new parameter ``input_mode`` to control how the input data is extracted. The possible values are "area", "point" and "nearest_gridpoint". To specify the location for "point" or  "nearest_gridpoint" the ``point`` parameter was added.
   * Added a new mode "user" to ``vertical_level_type`` to enable the usage of arbitrary vertical coordinate fields. These fields are identified by the ecCodes paramId specified in ``vertical_coordinate_param``.
   * Added new parameter ``vertical_coordinate_extrapolate`` to control the extrapolation at the top and bottom when ``vertical_level_type`` is "user".
   * Added new parameter ``vertical_coordinate_extrapolate_mode`` to control the extrapolation. The possible options are "constant" and "linear".
   * Added new parameter ``vertical_coordinate_extrapolate_fixed_sign``: for the "linear" extrapolation mode it controls whether the extrapolated values can differ in sign from the values on the nearest input levels. When it is “on” it prevents e.g. wind components to change sign due to extrapolation.

   See the new gallery examples for displaying :ref:`model levels with pressure axis <gallery_vert_hovm_ml_in_pressure>` and :ref:`model levels with height axis <gallery_vert_hovm_ml_in_height>`: 

   .. image:: /_static/gallery/vert_hovm_ml_in_pressure.png
      :width: 250px
      :target: ../gen_files/gallery/vert_hovm_ml_in_pressure.html

   .. image:: /_static/gallery/vert_hovm_ml_in_height.png
      :width: 250px
      :target: ../gen_files/gallery/vert_hovm_ml_in_height.html

**Macro/Python**

* Added new function :func:`poly_mask` to mask GRIB fields using arbitrary polygons. See the new gallery examples with polygons :ref:`defined by user points <gallery_polygon_masking>` and :ref:`extracted from a shapefile <gallery_shapefile_masking>`:

   .. image:: /_static/gallery/polygon_masking.png   
      :width: 200px
      :target: ../gen_files/gallery/gallery_polygon_masking.html

   .. image:: /_static/gallery/shapefile_masking.png
      :width: 200px
      :target: ../gen_files/gallery/shapefile_masking.html

* :func:`mean` and :func:`sum` now have an option called ``missing`` to control how to handle missing values during the computations. By default ``missing`` is False, which means that if at a gridpoint there is a missing value in any of the input fields the output will contain a missing value at that gridpoint. However, when ``missing`` is True all the non-missing values are used to form the mean/sum at a given gridpoint. See the :ref:`gallery example <gallery_sst_mean_with_missing_value>`:

   .. image:: /_static/gallery/sst_mean_with_missing_value.png
      :width: 350px
      :target: ../gen_files/gallery/sst_mean_with_missing_value.html

* :func:`mvl_ml2hPa`, :func:`ml_to_hl`, :func:`mvl_geopotential_on_ml`: these functions were re-implemented to improve performance by using less GRIB encoding-decoding and storing intermediate results in memory. The speed-up is quite significant: it is about x20 for :func:`mvl_ml2hPa`, x6 for :func:`ml_to_hl` and x3 for :func:`mvl_geopotential_on_ml`. This was achieved by only a 30% increase in memory usage for :func:`mvl_ml2hPa`, while the other two functions now use significantly less memory.
* :func:`mvl_ml2hPa`: fixed issue when incorrect results were produced when called from Python
* :func:`mvl_geopotential_on_ml`: fixed issue when crashed during reporting certain errors
* NetCDF variables with uint values are now supported
* NetCDF variables with int64 attributes are now supported
* fixed issue where two newly-created NCOLS-formatted geopoints could not be merged after one had been written to disk


**UI/uPlot**

* Added new projection 'EPSG:3035' to :func:`geoview`, see the :ref:`gallery example <gallery_epsg_3035>`:

   .. image:: /_static/gallery/epsg_3035.png
      :width: 250px
      :target: ../gen_files/gallery/epsg_3035.html

* Added new **Preferences** option called ``Default Folder For File Dialogs`` to control what folder the Save/Export dialogs show when they are opened up. The possible values are "current" and "previous".
* Fixed issue when the Metview interface exited with error code 1 on normal exit


**Miscellaneous**

* the environment variable ECCODES_DEBUG is now preserved when running at ECMWF
* if RPC libraries are not found when building Metview, the build will stop at CMake time with a relevant error message


**New Gallery Examples**


   .. image:: /_static/gallery/windrose.png
      :width: 250px
      :target: ../gen_files/gallery/windrose.html

   .. image:: /_static/gallery/ship_track_era5.png
      :width: 250px
      :target: ../gen_files/gallery/ship_track_era5.html

   .. image:: /_static/gallery/frame_masking.png
      :width: 250px
      :target: ../gen_files/gallery/frame_masking.html