.. _version_4.8_updates:

Version 4.8 Updates
///////////////////

Version 4.8.8 
=============

Became metview/new at ECMWF on 2017-07-19 (Linux desktops, ecgate, lxc)

-  **At ECMWF:**

   -  Installed **2017-07-19**

   -  Built with
      **Magics** `2.34.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.4.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.4.0+released>`__

   -  Built with **ODB_API** version `0.17.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__
      
   -  Built with **emoslib** `4.5.0 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

-  **Build**: this is the same as Metview 4.8.7, but relinked with emoslib 4.5.0

Version 4.8.7 
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-06-29
- Became metview/new at ECMWF on 2017-06-29 (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed **2017-07-29**

   -  Built with
      **Magics** `2.34.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.4.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.4.0+released>`__

   -  Built with **ODB_API** version
      `0.17.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000449 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **User Interface**: fixed problem with colour of tooltips that occurred on some desktops

-  **Display Window**: improved default settings for first-time users

   -  "Highlight Active Scene" is now OFF by default

   -  "Animate All Scenes" is now ON by default

-  **Gallery**: moved the examples up one level to make them easier to
   find - see the
   `Gallery <https://confluence.ecmwf.int/display/METV/Gallery>`__ page
   for example Metview plots and the macros that generate them

Version 4.8.6 
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-05-23
- Became metview/new at ECMWF on 2017-05-23 (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed **2017-05-2\ 2**

   -  Built with
      **Magics** `2.33.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.3.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.2.0+released>`__

   -  Built with **ODB_API** version
      `0.17.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000448 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **VAPOR**: the :ref:`VAPOR
   Prepare <vapor_prepare_icon>`
   module can now pass the date and time of the data to the files
   generated for VAPOR

-  **VAPOR**: fixed issue where the :ref:`VAPOR
   Prepare <vapor_prepare_icon>`
   module did not produce any output when run from a macro

-  **FLEXTRA**: fixed issue where FLEXTRA backward trajectories could
   not be plotted - see :ref:`The FLEXTRA
   interface <the_flextra_interface>`

Version 4.8.4
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-03-23
- Became metview/new at ECMWF on 2017-03-23 (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed **2017-03-23**

   -  Built with
      **Magics** `2.32.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.2.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.2.0+released>`__

   -  Built with **ODB_API** version
      `0.16.2 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000447 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **NetCDF**: added new parameter NETCDF_MATRIX_PRIMARY_INDEX (can be
   LATITUDE or LONGITUDE) for plotting geographic netCDF files with the
   coordinate variables specified as (lon, lat) instead of (lat, lon)

-  **Wind**: fixed issue where wind fields coloured by another parameter
   did not work. See the :ref:`Grib
   Vectors <grib_vectors_icon>`
   module for more information.

-  **GRIB**: improved support for Lambert azimuthal equal area GRIB
   fields; processing involving gridpoint computations will now work,
   including :ref:`Grib To
   Geopoints <grib_to_geo_icon>`,
   :ref:`nearest_gridpoint() <macro_fieldset_fn>`
   Macro function, cross sections, zonal means and Hovmoellers

-  **Macro Editor**: fixed issue where keyboard shortcuts for searching
   for text did not work on Leap42 workstations

Version 4.8.3
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-02-06
- Became metview/new at ECMWF on 2017-02-06 (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed **2017-02-06**

   -  Built with
      **Magics** `2.31.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.1.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.1.0+released>`__

   -  Built with **ODB_API** version
      `0.16.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000446 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **WMS**: fixed crash in the :ref:`WMS
   Client <metview_wms_tutorial>`
   editor when retrieving images from a WMS server that gives a
   redirection

-  **Build**: fixed compilation error with clang in the DivRot module
   (error was introduced with Metview 4.8.2, and will affect compilation
   on Mac OSX)

Version 4.8.2
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-02-01
- Became metview/new at ECMWF on 2017-02-01 (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed **2017-02-01**

   -  Built with
      **Magics** `2.31.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.1.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.1.0+released>`__

   -  Built with **ODB_API** version
      `0.16.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000446 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **ODB**: fixed problem introduced in 4.8.1 where the :func:`odb_visualiser` no longer worked

-  **DivRot**: fixed problem where the *Rotational and Divergent Wind*
   (DivRot) module no longer worked

-  **Build**: removed the cause of CMake warning message about
   METVIEW_INSTALL_BIN_DIR

Version 4.8.1
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-01-30
- Became metview/new at ECMWF on 2017-01-31 (Linux desktops, ecgate, lxc)

* **At ECMWF:**

   -  Installed **2017-01-30**

   -  Built with
      **Magics** `2.31.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.1.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.1.0+released>`__

   -  Built with **ODB_API** version
      `0.16.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000446 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

-  **Macro**: added new function to return the unique elements of a
   vector variable, e.g.

   .. code-block:: python

      a = |5, 7, 3, 3, 1, 3, 7|
      u = unique(a)  # u is now |5, 7, 3, 1|


See :ref:`Vector
Functions <macro_vector_fn>`.

-  **Macro**: the date() function now accepts a Julian date as an input
   number. Julian dates between 0001-01-01 and 4000-01-01 are accepted
   in Julian notation (1721426 to 3182030). Note that Metview treats
   Julian dates as starting from midnight, not noon. See :ref:`Date
   Functions <macro_date_fn>`.

-  **Legend**: added a new parameter, **Legend Symbol Height Factor**,
   to the :ref:`Legend <mlegend_icon>`
   icon. This is used when plotting small symbols on a chart, and you
   would like their representation in the legend to be larger - specify
   a scaling factor here, e.g. use "5" to see the symbols 5 times their
   chart size in the legend

-  **Tephigram**: the :ref:`Thermo
   View <thermoview_icon>` now
   accepts data of type :ref:`Input
   Visualiser <input_visualiser_icon>`

-  **GRIB**: added support for gridpoint calculations on GRIB data which
   is in "space view", i.e. satellite projection. This includes
   functionality of :ref:`Grib To
   Geopoints <grib_to_geo_icon>`
   for example. **Note**: this requires at least ecCodes 2.1.0.

-  **Synop**: New option in the *Observation Plotting* icon,
   OBS_WIND_PROJECTED, which controls whether the wind flag on a synop
   observation symbol is reprojected according to the map projection or
   not (default =ON). If OFF, then, for example, a wind flag pointing
   North will point upwards on the plot, regardless of the map
   projection - this was the behaviour in previous versions.

-  **Macro**: fixed issue where the nearest_gridpoint() function would
   not return a value when given a target point outside the Northern or
   Southern most latitude band of a grid that is global reduced Gaussian

-  **Geopoints to GRIB**: fixed issue where it could crash when given
   geopoints that were outside the Northern or Southern most latitude
   band of a target grid that is global reduced Gaussian

-  **Geopoints to GRIB**: fixed the handling of missing values in the
   `"nearest" interpolation
   modes <https://confluence.ecmwf.int/display/METV/Geopoints+To+Grib>`__
   - Nearest Gridpoint Mean and Nearest Gridpoint Sum now write missing
   values into the grid points which are not the nearest to any
   geopoints (previously they wrote zeros into these positions)

-  **Percentile**: the
   :ref:`Percentile <percentile_icon>`
   module has had its memory usage dramatically reduced

-  **Average Data/View**: fixed issue where the computation was very
   slow when working on GRIB data on a reduced Gaussian grid

-  **Average Data**: the resulting netCDF files from :ref:`this
   module <maverageview_icon>`
   always used **lon** as a variable dimension, even if the computation
   was for a zonal mean - now the variable uses **lat** as its dimension
   in this case

-  **Macro**: fixed problem in the macro
   `mvl_ml2hPa <https://confluence.ecmwf.int/display/METV/mvl_ml2hPa>`__,
   which did not work when computing pressure levels < 1hPa with GRIB 1
   data

-  **Single Column Model**: the *SCM Visualiser* icon had stopped
   working - it is fixed now

-  **NetCDF**: fixed issue where the ncdump panel of the NetCDF Examiner
   was not populated when run on the Leap42 workstations at ECMWF

-  **Meteograms**: updated settings for communication with ECMWF
   Meteogram server so that it works with the new firewall configuration

-  **ODB Filter**: added an option to determine behaviour when the
   returned dataset is empty. This new option, "FAIL_ON_EMPTY_OUTPUT"
   has a default of "Yes" and an option of "No", which can be used in a
   macro to catch this situation programatically

-  **Stations**: use the latest WMO stations database

-  **Macro Editor**: increased space available for text editing

-  **WMS**: made a small adjustment to the :ref:`WMS
   Client <metview_wms_tutorial>`
   to make more space for the **Extra Param** boxes

-  **Gallery**: updated the `Metview
   Gallery <https://confluence.ecmwf.int/display/METV/Gallery>`__ with
   examples of `Cross
   Section <https://confluence.ecmwf.int/display/METV/Cross+Section+Example>`__,
   :ref:`Hovmoeller <gallery_hovmoeller_area>`
   and  :ref:`page
   layout <gallery_layoutx3>`

Version 4.8.0
=============

- Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2016-11-23
- Became metview/new at ECMWF on 2016-11-?? (Linux desktops, ecgate, lxc)

*  **At ECMWF:**

   -  Installed as *metview/new*

   -  Built with
      **Magics** `2.30.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes** `2.0.2 <https://software.ecmwf.int/wiki/display/ECC/ecCodes+version+2.0.2+released>`__

   -  Built with **ODB_API** version
      `0.16.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib** `000445 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__

*  **Build**: the CMake option **ENABLE_ECCODES** is now **ON** by
   default. To build Metview with GRIB_API, please set
   **-DENABLE_ECCODES=OFF**

-  **GRIB support**: this is the first version of Metview installed at
   ECMWF with GRIB support powered by
   `ecCodes <https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home>`__
   instead of
   `GRIB_API <https://software.ecmwf.int/wiki/display/GRIB/Home>`__.

-  **Macro**: new function - find(vector, number), which returns the
   index(es) where a given number occurs in a vector. See `Vector
   Functions <https://software.ecmwf.int/wiki/display/METV/Vector+Functions>`__.

-  **Macro**: new vector indexing technique, where a vector may be used
   as an index into another vector. See
   `Vectors <https://software.ecmwf.int/wiki/display/METV/Vectors>`__.

-  **Macro**: updated the version_info() command so that, if built with
   ecCodes, it returns an eccodes_version member instead of
   grib_api_version

-  **Axis Plotting**: added new parameters for plotting minor grid lines

-  **Axis Plotting**: changed default axis grid line colour from yellow
   to black

-  **MARS**: removed message about "Ambiguous Verb" during MARS
   retrieve() and read() commands

-  **Icon editors**: fixed issue where the colour set in one custom
   colour widget could be mistakenly transferred to another colour
   parameter

-  **Icon editors**: fixed issue where a macro-generated user interface
   with multiple geography helper buttons could mistakenly transfer the
   settings from one parameter to another
