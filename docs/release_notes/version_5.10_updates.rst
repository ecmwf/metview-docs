.. _version_5.10_updates:

Version 5.10 Updates
////////////////////


Version 5.10.2
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2021-01-20
* Became metview/new at ECMWF on 2021-01-20 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2021-01-20**

   -  Built
      with **Magics** `4.5.3 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.20.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.20.0+released>`__

   -  Built with **ODC** version **1.2.0**

   -  Includes
      version `1.6.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Hovmoeller:**

-  fixed issue where the
   `Hovmoeller <https://confluence.ecmwf.int/display/METV/Hovmoeller+Data>`__
   module's 'expand' option did not work

**Plotting:**

-  fixed issue that caused a crash when plotting a
   :ref:`tephigram <thermoview_icon>`
   using the
   :ref:`Stations <stations_icon>`
   module for location input

**Macro:**

-  fixed issue where
   a `Geopointset <https://confluence.ecmwf.int/display/METV/Geopointset>`__
   could not be loaded if the format of the underlying Geopoints was
   NCOLS

-  fixed issue where a fieldset with one or more modified fields was
   added to a definition and could not then be plotted

-  performance optimisation in the lookup function - see :ref:`Fieldset
   Functions <macro_fieldset_fn>`

**Gallery:**

-  added examples using the :ref:`Cartesian
   View <cartesian_view_icon>`

   -  :ref:`Curve With Log Y Axis
      Example <gallery_cartesian_log_y_axis>`

   -  :ref:`Curves with Different Y Scales
      Example <gallery_double_axis_2>`

-  changed the default language to Python

**Build:**

-  fixed issue where Metview could not build with a curl library
   installed into a non-standard location

-  FORTRAN is now disabled by default

Built with Magics 4.5.3, the new palettes are available to browse and
use in
the :ref:`Contouring <mcont_icon>`
icon:


.. image:: /_static/release/version_5.10_updates/image1.png
   :width: 5.36458in
   :height: 2.60417in
  
.. image:: /_static/release/version_5.10_updates/image2.png
   :width: 1.66667in
   :height: 1.40625in


Version 5.10.1
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2020-11-09
* Became metview/new at ECMWF on 2020-11-09 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2020-11-09**

   -  Built
      with **Magics** `4.5.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes**\ `2.19.1 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.19.1+released>`__\

   -  Built with **ODC** version **1.1.0**

   -  Includes
      version `1.5.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Plotting:**

-  fixed issue where custom symbol images (:ref:`Symbol
   Plotting <msymb_icon>`
   - Symbol Marker Mode = 'image') were plotted at slightly different
   positions depending on the graphics driver - when producing a file
   such as PNG, PDF or PostScript the marker images were centred on the
   supplied locations; in the interactive plotting window, the locations
   were taken to be the South-West corner of the marker. Now the
   interactive window follows the same rule as the other drivers and
   centres the markers on the locations. Requires Magics 4.5.1.

   -  example: plot an image covering a 10x10 degree square at location
      (0, 0). Previously, the interactive plot would look like the one
      on the left, now it looks the one on the right, which is
      consistent with the other drivers:

      .. image:: /_static/release/version_5.10_updates/image3.png
         :width: 1.5625in
         :height: 1.2627in
        
      .. image:: /_static/release/version_5.10_updates/image4.png
         :width: 1.5625in
         :height: 1.15388in

      .. code-block:: python

            # Metview Macro
            
            ivis = input_visualiser(
               input_plot_type        : "geo_points",
               input_longitude_values : 0,
               input_latitude_values  : 0,
               input_values           : 10
               )
            
            symb = msymb(
               symbol_type         : "marker",
               symbol_height       : 0.6,
               symbol_marker_mode  : "image",
               symbol_image_path   : "./MSYMB.png",
               symbol_image_format : "png",
               symbol_image_width  : 10,
               symbol_image_height : 10
               )
            
            plot(ivis, symb)


-  benefits from a fix in Magics 4.5.1 where cross sections that cross a
   pole did not plot properly

-  fixed issue where the version of Magics was not displayed in the Help
   \| About box

**Geopoints:**

-  fixed issue where geopoints station ids (:func:`stnids`) could
   return numbers instead of strings if the station ids were 'numeric'
   in nature, e.g. '12345'. Now they are always returned as strings.

**Macro:**

-  fixed issue where vector variables written to disk could not be read
   back into memory on some platforms

**Startup:**

-  fixed issue where directory permissions were not correctly set when
   starting Metview for the very first time, causing an ability to start
   Metview

**Build:**

-  fixed issue when building for macOS on conda

-  fixed issue where a data file used for tests was not available

Version 5.10.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2020-10-15
* Became metview/new at ECMWF on 2020-10-15 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2020-10-15**

   -  Built
      with **Magics** `4.5.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.19.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.19.0+released>`__

   -  Built with **ODC** version **1.1.0**

   -  Includes
      version `1.5.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**GRIB Regridding:**

-  new module
   - :ref:`Regrid <regrid_icon>` -
   providing powerful and flexible interpolation and processing methods
   on GRIB data. Supports many configurable interpolation methods,
   output to various grid types including rotated grids and Lambert
   variants, supports nabla operators, and processing such as spectral
   to gridpoint, sub-area extraction, frame carving and changing the
   bits-per-value. The module also allows a template GRIB to be
   supplied, circumventing the need to set any output grid parameters.
   The most common of these parameters are already available through
   the :ref:`MARS
   Retrieval <retrieve_icon>`
   and `GRIB
   Filter <https://confluence.ecmwf.int/display/METV/GRIB+Filter>`__
   icons - :ref:`Regrid <regrid_icon>`
   takes it to the next level! 
   
   .. note::
      
      In this release, the Regrig module is considered to be a beta release, meaning that we may make small changes to the interface in upcoming releases; we welcome feedback.

   .. image:: /_static/release/version_5.10_updates/image5.png
      :width: 4.78746in
      :height: 2.60417in
 
   .. image:: /_static/release/version_5.10_updates/image6.png
      :width: 3.33333in
      :height: 4.74679in

**User Interface:**

-  added a Preview panel in the main user interface:

   -  activated via the 'eye' icon in the toolbar: 

      .. image:: /_static/release/version_5.10_updates/image7.png
         :width: 1.0625in
         :height: 0.67708in

   -  now, when the mouse cursor is over an icon, you see some
      information about it in the Preview panel, e.g. for data icons you
      will see some meta-data,
      for :ref:`Coastlines <mcoast_icon>`
      and :ref:`Geographical
      View <geoview_icon>` icons,
      you will see a plot preview:

      .. image:: /_static/release/version_5.10_updates/image8.png
         :width: 2.1875in
         :height: 2.21788in
        
      .. image:: /_static/release/version_5.10_updates/image9.png
         :width: 2.14583in
         :height: 2.27281in
       
      .. image:: /_static/release/version_5.10_updates/image10.png
         :width: 1.97917in
         :height: 2.24934in


-  added a parameter filter to the icon editors to speed up the finding
   of parameters:

   .. image:: /_static/release/version_5.10_updates/image11.png
         :width: 3.16667in
         :height: 2.60417in

-  added a tab history navigation tool

   .. image:: /_static/release/version_5.10_updates/image12.png
         :width: 1.875in
         :height: 0.91255in

-  added a search capability to the getCapabilities view of the :ref:`WMS
   Client <wmsclient_icon>`
   editor

-  redesigned icons for graphical output types for clarity, e.g.

   .. figure:: /_static/release/version_5.10_updates/image13.png
      :width: 0.58333in
      :height: 0.57292in

      Old icon style
    
   .. figure:: /_static/release/version_5.10_updates/image14.png
      :width: 0.58333in
      :height: 0.57292in
      
      New icon style

-  fixed issue where the help sidebar in the Code Editor could not be
   restored after it had been collapsed using the splitter handle

-  fixed issue where an icon editor could be closed unintentionally when
   pressing a key

-  fixed issues on macOS 10.15 where no more than one instance of
   various modules (e.g. Code Editor, GRIB Examiner, batch plotting)
   could be run simultaneously

-  fixed issue on macOS where closing an icon editor's Help widget could
   cause a crash

**GRIB Examiner:**

-  added syntax highlighting to GRIB dump text

   .. image:: /_static/release/version_5.10_updates/image15.png
         :width: 3.34375in
         :height: 2.60417in

**Plotting:**

-  added option to render :ref:`Thermo
   Grid <mthermogrid_icon>` to
   background or foreground layer

-  fixed issue where the :ref:`Table
   Visualiser <table_visualiser_icon>` could
   plot "geo_vector" data at the wrong locations

-  fixed issue in
   the :ref:`Contouring <mcont_icon>`
   icon where parameter **contour_hilo_format** was not available if
   **contour_hilo_type** was set to **BOTH**

**Macro / Python:**

-  added function to compute xy components from polar components:
   :func:`xy_from_polar`

-  added function to generate orography polygon for cross section:
   :func:`xs_build_orog`

-  added function to generate curve from a field for cross section:
   :func:`xs_build_curve`

-  added function to extract data values from thermo data objects:
   :func:`thermo_data_values`

-  added function to create a geographic polyline
   object: :func:`mvl_geopolyline`

-  add convenience function to generate xy area plot objects: :func:`xy_area`

-  add function to compute vertical velocity from omega: :func:`w_from_omega`

-  added function to compute dewpoint from specific
   humidity: :func:`dewpoint_from_specific_humidity`

-  added function to compute dewpoint from relative
   humidity: :func:`dewpoint_from_relative_humidity`

-  added an option to the :func:`indexes` function to allow interpolation
   between indexes

-  enabled :func:`ml_to_hl` to work with target heights defined by fieldsets

-  enabled :func:`vapour_pressure` to work with model levels fields

-  renamed function :func:`geostrophic_wind_pl` to :func:`geostrophic_wind`

-  switched off unnecessary printouts when reading BUFR data through
   Python

-  fixed issue that Metview did not fail when dividing one field by
   another that contains zeros

-  fixed issue where the :func:`pressure` function did not set paramId to 54
   on output field

**Geopoints:**

-  handle the case where a station id contains internal spaces

-  fixed issue where invalid latlon values in geopoints would make the
   geopoints-grib operator crash

-  fixed issue where :ref:`Observation
   Filter <obsfilter_icon>` did
   not set missing values correctly for geopoints output

-  fixed issue where the Geopoints format string was not set for
   traditional type when loaded from file

**Cross section:**

-  added option to perform vertical extrapolation when
   vertical_coordinates="user".  The new option name is
   **VERTICAL_COORDINATE_EXTRAPOLATE.** The possible values are **on**
   and **off**. See :ref:`Cross Section
   Data <mcross_sect_icon>`

**Hovmoeller:**

-  fixed issue where parameter time_axis_mode was not respected when run
   from Macro/Python

**ODB support:**

-  Metview is now built with the **odc** library, which replaces
   ODB_API; functionality remains unchanged

**Startup:**

-  the 'examine' startup mode no longer requires the data type to be
   specified - see `Metview's Startup
   Options <https://confluence.ecmwf.int/display/METV/Metview%27s+Startup+Options>`__

-  Geopoints are now supported in Metview's 'examiner' startup mode

-  fixed an issue where a user's initial Metview directory was read-only

-  fixed an issue where macOS machines could not untar some system files
   needed for the users' initial directory, leading either to: untidy
   startup folder, or unable to untar and build the source

**Build:**

-  note that this version of Metview requires CMake 3.12.0+, ecCodes
   2.19.0+ and Magics 4.5.0+.

**Gallery:**

-  added a new example for ensemble data handling:

   -  :ref:`ENS Tephigram
      Example <gallery_ens_tephigram>`

-  added new examples for cross section:

   -  :ref:`Cross Section in Pressure with Orography and Boundary Layer
      Height
      Example <gallery_cross_section_orog_and_blh>`

   -  :ref:`Cross Section in Height for Model Level Data with Orography
      Example <gallery_cross_section_height_ml_orog>`

-  added a new example for plotting ODB data onto a tephigram:

   -  :ref:`Tephigram from ODB
      Example <gallery_tephigram_odb>`

-  added a new example for plotting polylines/polygons into arbitrary
   map projections:

   -  :ref:`Geopolyline on Map
      Example <gallery_geopolyline_on_map>`
