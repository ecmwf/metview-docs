.. _version_5.14_updates:

Version 5.14 Updates
////////////////////


Version 5.14.1
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-01-19
* Became metview/new at ECMWF on 2022-01-19 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-01-19**

   -  Built
      with **Magics** `4.10.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.24.2 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.24.2+released>`__

   -  Built with **ODC** version **1.4.3**

   -  Includes
      version `1.9.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Fixes:**

-  Fixed issue where passing data from Macro or Python to a separate
   Metview module could result in that data being kept permanently in
   memory - observed with Geopoints data

-  Fixed issue where clearing a Geopoints variable did not release all
   its memory

-  Fixed issue in
   the :ref:`geo_to_grib <geo_to_grib_icon>` module
   where it did not properly ignore missing input values when run in the
   'nearest' modes

-  Fixed issue in the new :ref:`weather symbol
   editor <weather_symbols>` where
   uPlot crashed if a line was added outside of the map area

-  Fixed issue in the new :ref:`weather symbol
   editor <weather_symbols>` where
   interactive resizing of a line's arrowheads did not take effect until
   the line was moved

Version 5.14.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2021-12-07
* Became metview/new at ECMWF on 2021-12-07 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2021-12-07**

   -  Built
      with **Magics** `4.10.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.24.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.24.0+released>`__

   -  Built with **ODC** version **1.4.3**

   -  Includes
      version `1.9.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Interactive plot annotations:**

-  Major new feature in the interactive plotting window

-  Annotation layer with:​

   -  Shapes, lines, markers, text  etc.​

   -  Surface analysis (fronts, ridge, ITCZ etc)​

   -  All the WMO Symbols

-  Accessible through the 'Symbols' tab on the sidebar​

-  See :ref:`How to use the Weather Symbol Editor in
   Metview <weather_symbols>` for
   more information on this new feature!

   .. image:: /_static/release/version_5.14_updates/image1.png
      :width: 5.20833in
      :height: 4.07292in


   .. image:: /_static/release/version_5.14_updates/image2.png
      :width: 5in
      :height: 4.0173in

**EFAS grids:**

-  with the latest support libraries (ecCodes, Magics, Mir), Metview now
   supports GRIB files encoded on a lambert azimuthal grid on an oblate
   spheroid Earth

-  supported functionality: regridding, plotting, Cursor Data,
   conversion to geopoints

-  .. image:: /_static/release/version_5.14_updates/image3.png
      :width: 3.19792in
      :height: 2.60417in

     

   .. image:: /_static/release/version_5.14_updates/image4.png
      :width: 5.40069in
      :height: 2.40673in

**STVL access:**

-  new module :func:`stvl` to retrieve data from the STVL on internal ECMWF
   machines (workstations, lxc, lxop)

-  .. image:: /_static/release/version_5.14_updates/image5.png
      :width: 3.17845in
      :height: 2.60417in

     

   .. image:: /_static/release/version_5.14_updates/image6.png
      :width: 4.79742in
      :height: 2.60417in

**Plotting:**

-  changes in Magics to improve vertical axis labelling and titles

-  small adjustment to Single Column Model plots that have two vertical
   axes in order to accommodate the better-positioned axis title

-  improved the highlighting of the currently active scene so that it
   shows a border rather than a filled rectangle, which could obscure
   the contents:

   -  .. image:: /_static/release/version_5.14_updates/image7.png
         :width: 3.71022in
         :height: 2.60417in

-  there is now a way to revert to sending plots to the interactive
   window:  setoutput("screen")

-  new :ref:`parameters <mcont_icon>` to
   further control the positioning of grid value
   plotting: 
   
      - contour_grid_value_position
      - contour_grid_value_justification,
      - contour_grid_value_vertical_align

-  fixed issue where the Zoom stack was not rendered correctly

-  requires Magics 4.10.0

**Macro/Python:**

-  new function: :func:`solar_zenith_angle`

-  new function to compute the :func:`speed` from U and V fieldsets::

      spd = speed(u, v)

-  new function: :func:`relative_humidity_from_specific_humidity`

-  new function: :func:`specific_humidity_from_relative_humidity`

-  the :func:`grib_get` function
   now allows to extract GRIB keys in their native type::

      a = grib_get(fs, ['level:n', 'centre:n'])

-  function :func:`saturation_mixing_ratio` now works with fieldsets

-  improved execution speed of :func:`ml_to_hl`

-  add option to :func:`ml_to_hl` to specify input data values on the surface

-  functions :func:`relative_humidity_from_dewpoint` and :func:`dewpoint_from_relative_humidity` now
   return their results as percentages rather than values in the
   range [0,1]

-  fixed crash in :func:`ml_to_hl` when target level is outside input z range

-  allow :func:`mvl_geopotential_on_ml` to use a subset of levels in arbitrary
   order, reducing the amount of input data required and therefore the
   processing requirements

-  fixed issue where the wind :func:`direction` function accumulated memory

**Main user interface:**

-  new user interface themes:

   -  light: similar to previous styling, with some changes for a
      cleaner look

   -  dark: suitable for 'dark' modes

      .. image:: /_static/release/version_5.14_updates/image8.png
         :width: 4.21288in
         :height: 2.60417in

      .. image:: /_static/release/version_5.14_updates/image9.png
         :width: 4.21288in
         :height: 2.60417in

   -  go to Tools \| Preferences to change the setting, or start Metview
      with -light or -dark command-line switches

-  improved helper for list parameters in icon editors; short names are
   now shown, and there is a filter:

      .. image:: /_static/release/version_5.14_updates/image10.png
         :width: 3.95833in
         :height: 2.33333in

-  fixed issue where the 'stop' button in the Code Editor did not
   actually terminate a Python process that was started from the editor

-  fixed issue where an icon sent via the mail tool did not appear as
   attachment in e-mail clients

-  fixed a crash when sending icons via the mail tool

**Data examiners:**

-  the Geopoints examiner now displays the metadata from the geopoints
   file:

      .. image:: /_static/release/version_5.14_updates/image11.png
         :width: 4.90069in
         :height: 1.02506in

-  the GRIB examiner now has a tab to show which tables were used to
   decode the current message

-  fixed issue in the BUFR examiner where it crashed when the locations
   tab was selected on an ill-formed message

**Regridding:**

-  Regridding via either :func:`regrid` or :func:`read` now supports space_view GRIB
   files as input

-  fixed an issue in
   the :ref:`Regrid <regrid_icon>` module
   where it crashed if a string is supplied to the **Template
   Data** parameter

**Other:**

-  improved filter speed for compressed subsets of BUFR data

-  updated the list of WMO stations as used by
   the :ref:`Stations <stations_icon>` module

-  new environment variable: set METVIEW_MARS_HOME to point to the
   location of non-default MARS config files

-  fixed a crash in the WMSClient editor when closing the log panel

-  fixed an issue where the Metview bundle did not work on macOS after
   being installed and configured without an install prefix
