.. _version_4.5_updates:

Version 4.5 Updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 Export Version 4.5.7 `3 <#export-version-4.5.7>`__

2 Test Version 4.5.7 `4 <#test-version-4.5.7>`__

3 Test Version 4.5.6 `6 <#test-version-4.5.6>`__

4 Export Version 4.5.6 `7 <#export-version-4.5.6>`__

5 Default Version upgraded to 4.5.5
`8 <#default-version-upgraded-to-4.5.5>`__

6 Export Version 4.5.5 `9 <#export-version-4.5.5>`__

7 Test Version 4.5.5 `10 <#test-version-4.5.5>`__

8 Export Version 4.5.4 `11 <#export-version-4.5.4>`__

9 Test Version 4.5.4 `12 <#test-version-4.5.4>`__

10 Export Version 4.5.3 `13 <#export-version-4.5.3>`__

11 Test Version 4.5.3 `14 <#test-version-4.5.3>`__

12 Export Version 4.5.2 `15 <#export-version-4.5.2>`__

13 Test Version 4.5.2 `16 <#test-version-4.5.2>`__

14 Export Version 4.5.1 `17 <#export-version-4.5.1>`__

15 Test Version 4.5.0 `18 <#test-version-4.5.0>`__

Export Version 4.5.7
====================

**External release 2015-10-16**

`Version 4.5.7-export became available. See
the  <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ `Releases <https://confluence.ecmwf.int/display/METV/Releases>`__
page for download.

Test Version 4.5.7
==================

`Introduced 2015-10-07 (Linux desktops, lxab and lxc clusters,
ecgb) <#export-version-4.5.7>`__

-  `Installed as metview4_new <#export-version-4.5.7>`__

-  `Built with Magics 2.25.2. See the Magics <#export-version-4.5.7>`__
   `Latest
   News <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__.

-  Built with **GRIB_API** 1.14.1

-  Built with **ODB_API** version 0.10.5

-  Built with **emoslib** 000411. See the `Change
   History <https://software.ecmwf.int/wiki/display/EMOS/Changes+in+version+000411>`__.

-  **Tephigrams**: added `Thermo
   Grid <https://software.ecmwf.int/wiki/display/METV/Thermo+Grid>`__
   and `Thermo
   Plotting <https://software.ecmwf.int/wiki/display/METV/Thermo+Plotting>`__
   icons for controlling the plotting of the background and curves of a
   tephigram. Plotting of wind arrows is still controlled by the `Wind
   Plotting <https://software.ecmwf.int/wiki/display/METV/Wind+Plotting>`__
   icon. Full drag and drop support is now implemented between the
   various "Thermo" icons.

-  **Cross Section**: added support for plotting cross sections of wind
   vectors. Users are now able to customise the scaling of the vertical
   wind if desired.

-  **Cross Section**: added new parameter to the `Cross Section
   View <https://software.ecmwf.int/wiki/display/METV/Cross+Section+View>`__
   and `Cross Section
   Data <https://software.ecmwf.int/wiki/display/METV/Cross+Section+Data>`__
   icons: **Horizontal Point Mode**, which now allows the points along
   the transect line to be computed either via interpolation of the
   surrounding grid points (the default behaviour) or using the nearest
   grid point (the new option).

-  **Cross Section**: revised method to determine which pressure levels
   to interpolate onto when converting from model level data. The new
   scheme ensures that the plot continues down to the bottom even in
   cases where there is extreme orography.

-  **Cross Section**: added parameters to allow a user-defined list of
   pressure levels to interpolate onto when converting from model level
   data. See `Cross Section
   Data <https://software.ecmwf.int/wiki/display/METV/Cross+Section+Data>`__
   and `Cross Section
   View <https://software.ecmwf.int/wiki/display/METV/Cross+Section+View>`__.

-  **Plotting**: parameter **Symbol Text Blanking** in the :ref:`Symbol
   Plotting <msymb_icon>`
   icon is now available in the table modes

-  **Plotting**:
   new `Coastlines <https://software.ecmwf.int/wiki/display/METV/Coastlines>`__
   parameters available: **Map Label Font**,  **Map Label Font Style**
   and **Map Label Blanking**

-  **Display Window**: the Cursor Data can now be significantly faster
   (e.g. 100x) with some large fields. Note that this requires Magics
   2.25.2.

-  **Display Window**: some options in the Export dialogue from the plot
   window were erroneously displayed as plain strings instead of a fixed
   list of possible values.

-  **User Interface**: now closes properly during a system shutdown

-  **GRIB**: ensured that Metview now works with negative forecast steps
   (when built with GRIB_API 1.15.0)

-  **GRIB**: Metview now uses higher-level GRIB_API keys for checking
   flags relating to grid interpretation. This does not fix any known
   bugs, but should be safer.

-  **Build**: installers can now specify a different path to install
   Metview's executables by supplying to CMake a path relative to the
   base install directory, for example:

   -  -DMETVIEW_INSTALL_EXE_BIN_DIR=lib/metview/bin

-  **Build**: fixed issue when building Metview's fortran modules with
   Intel compilers.

-  **Build**: Metview now builds with Qt5. There is an issue with the
   main menu on Mac OS X which seems to affect other applications; the
   menu becomes active only after switching context to and then from
   another application.

-  **Build**: added the ability to run post-installation tests for added
   confidence in the installation. From the build directory:

   -  | cd tests/macros
      | ./post_install_tests.sh

Test Version 4.5.6
==================

`Introduced 2015-06-17 (Linux desktops, lxab and lxc clusters,
ecgate) <#export-version-4.5.7>`__

-  `Installed as metview4_new (module swap
   metview/new) <#export-version-4.5.7>`__

-  `Built with Magics 2.25.1. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.13.1

-  Built with **ODB_API** version 0.10.2

-  Built with **emoslib** 000406

Export Version 4.5.6
====================

**External release 2015-06-16**

`Version 4.5.6-export became available. See
the  <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ `Releases <https://confluence.ecmwf.int/display/METV/Releases>`__
page for download.

-  **Plotting**: fixed issue where plotting of small details in PDF and
   PNG format gave a bad plot because of outline attributes which were
   too thick

-  **Plotting**: fixed rare issue where the plotting of a data file
   which is a symbolic link could fail

-  **GRIB**: fixed issue where Metview's internal GRIB navigation
   routines did not correctly compute the coordinates of the points on a
   GRIB field which is a sub-area of a reduced Gaussian grid. This
   affects a number of functions and modules, including *Grib to
   Geopoints*, *Cross Section* and the Macro functions
   nearest_gridpoint() and interpolate().

-  **Grib Examiner**: fixed issue where the *Grib Examiner* could crash
   when switched to *Namespace* mode

-  **Examiners**: fixed issue where the data examiner applications (e.g.
   the *Grib Examiner*) could crash when closed; this was normally not
   visible, but could show up on the Mac OS X

-  **Stations**: the *Stations* module has been updated to use the
   latest list of WMO stations

-  **User Interface**: allow the dropping of Metview 3 (e.g. PCONT)
   icons into the icon editor of Metview 4 (e.g. MCONT) icons to aid
   migration

-  **Startup**: fixed the display of the Metview version when typing
   "metview -h"

Default Version upgraded to 4.5.5
=================================

**Upgrade 2015-06-09 (Linux desktops, lx\* clusters, ecgate)**

-  Version 4.5.5 became the *default version* (command metview) at ECMWF

-  To use another version, please use the modules system:

   -  module avail metview

-  

   -  module switch metview/x.x.x

Export Version 4.5.5
====================

**External release 2015-05-27**

`Version 4.5.5-export became available. See
the  <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ `Releases <https://confluence.ecmwf.int/display/METV/Releases>`__
page for download.

Test Version 4.5.5
==================

`Introduced 2015-05-27 (Linux desktops, lxab and lxc clusters,
ecgate) <#export-version-4.5.7>`__

-  `Installed as metview4_new (module swap
   metview/new) <#export-version-4.5.7>`__

-  `Built with Magics 2.24.7. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.13.1

-  Built with **ODB_API** version 0.10.2

-  Built with **emoslib** 000406

-  **MARS**: when building Metview outside ECMWF, `MARS access through
   the Web
   API <https://software.ecmwf.int/wiki/display/METV/Using+the+MARS+Web+API+from+Metview>`__
   is enabled by default without the need to specify a **Database**
   parameter in the requests.

-  **Plotting**: fixed rare issue where plots could fail when producing
   multiple PostScript pages

-  **Plotting**: fixed issue where plots could fail when producing large
   numbers (>1000) of output graphics files in batch mode

-  **ODB**: improved the finding of the odb_migrator executable when
   filtering ODB-1 data

Export Version 4.5.4
====================

**External release 2015-05-14**

`Version 4.5.4-export became available. See
the  <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ `Releases <https://confluence.ecmwf.int/display/METV/Releases>`__
page for download.

Note: it is recommended to use at least Magics 2.24.3 in order to build
with plotting enabled.

Test Version 4.5.4
==================

`Introduced 2015-05-12 (Linux desktops, lxab cluster,
ecgb) <#export-version-4.5.7>`__

-  `Installed as metview4_new <#export-version-4.5.7>`__

-  `Built with Magics 2.24.6. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.13.1

-  Built with **ODB_API** version 0.10.2

-  Built with **emoslib** 000402

-  **Legend**: added new parameter to the *Legend* icon - **Legend
   Automatic Position**. Can have one of two values: top (default) and
   right. This allows a legend to be automatically positioned to the
   right of the plot without the need to manually specify its
   coordinates

-  **Contouring**: now, when **Contour Shade Technique** is set to Grid
   Shading, all interpolation of the input GRIB field is automatically
   deactivated without the user having to set additional parameters,
   true to its original intention (e.g. **Contour Method** previously
   had to be set to Linear)

-  **Contouring**: parameter **Contour Reference Level** is now
   available even if **Contour Highlight** is Off

-  **Contouring**: allow access to the parameter **Contour Internal
   Reduction Factor** to allow fine-grain control over contouring of
   certain fields

-  **Plotting**: now the page_frame parameters from view icons are
   honoured

-  **NetCDF**: the **ncdump** panel of the NetCDF Examiner was not
   working on the new workstations at ECMWF; now it is

-  **Reprojection**: all the meta-data in the Product section of the
   input GRIB file is now transferred to the resulting GRIB file

-  **Macro**: it is now possible to specify that a coastlines definition
   be plotted on top of the data - just put the coastlines variable at
   the end of the plot command (or anywhere after the first data
   variable)

-  **Macro**: fixed issue where putting a visdef variable at the start
   of a plot() command could cause a crash

-  **Macro**: when supplying a relative path when using multiple output
   graphics file formats, the files will now be generated in relative to
   where the macro is located

-  **Macro**: improved printing of error messages from other modules

-  **Macro**: fixed an issue where the function nearest_gridpoint()
   could return the wrong point in a particular edge case where the
   longitude is beyond the last point, e.g. in a 1x1 degree grid, asking
   for the nearest gridpoint to (0, 359.1) returned the wrong result

-  **Stations**: a new parameter, **Fail on Error** was added. If this
   is set to **No**, then a macro can trap the condition where it does
   not find a matching station by checking whether the return result is
   nil.

-  **SCM**: fix to allow the running of SCM executables on the classroom
   machines

-  **SCM**: fixed occasional crash in SCM profile editor

-  **Mac OS X**: chosen better default viewers for image formats such as
   PNG and PostScript

-  **Mac OS X**: graphics are now crisper due to the choice of a
   different Qt rendering engine on this platform

Export Version 4.5.3
====================

**External release 2015-03-12**

`Version 4.5.3-export became available. See
the  <https://software.ecmwf.int/wiki/display/METV/Development+Snapshots>`__\ `Development
Snapshots <https://confluence.ecmwf.int/display/METV/Development+Snapshots>`__
page for download.

Note: it is recommended to use Magics 2.24.1 in order to build with
plotting enabled.

Test Version 4.5.3
==================

`Introduced 2015-03-12 (Linux desktops, lxab cluster,
ecgb) <#export-version-4.5.7>`__

-  `Installed as metview_new   (module swap metview/new ;
   metview) <#export-version-4.5.7>`__

-  `Built with Magics 2.24.1. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.13.0

-  Built with **ODB_API** version 0.10.2

-  Built with **emoslib** 000400

-  **WMS**: fixed issue where a configuration file required for correct
   operation of Metview's :ref:`Web Map
   Client <metview_wms_tutorial>`
   module was not installed

-  **Desktop**: it's now easier to create a new icon: from the **Create
   new Icon** dialogue, pressing **Return** will create an instance of
   the currently selected icon

-  **Desktop**: fixed issue where creation of a new icon could fail

-  **Plotting**: fixed issue where the MAGPLUS_HOME environment variable
   could interfere with the correct finding of Magics resource files

Export Version 4.5.2
====================

**External release 2015-03-09**

`Version 4.5.2-export became available. See
the  <#export-version-4.5.7>`__\ `Development
Snapshots <https://confluence.ecmwf.int/display/METV/Development+Snapshots>`__
page for download.

Note: it is recommended to use Magics 2.24.1 in order to build with
plotting enabled.

Test Version 4.5.2
==================

`Introduced 2015-03-05 (Linux desktops, lxab cluster,
ecgb) <#export-version-4.5.7>`__

-  `Installed as metview_new   (module swap metview/new ;
   metview) <#export-version-4.5.7>`__

-  `Built with Magics 2.24.1. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.13.0

-  Built with **ODB_API** version 0.10.2

-  Built with **emoslib** 000400

-  **Plot export**: when exporting a plot from the interactive display
   window, the available options for the selected file format are now
   presented in a dialogue if the user clicks on the spanner icon next
   to the output format

-  **Macro**: when supplying a relative path to an output graphics file,
   the file will now be generated in relative to where the macro is
   located

-  **Display Window**:

   -  dropping of
      `Legend <https://software.ecmwf.int/wiki/display/METV/Legend>`__
      and `Text
      Plotting <https://software.ecmwf.int/wiki/display/METV/Text+Plotting>`__
      icons now more consistent behaviour

   -  fixed an issue where using an old pcont icon or plotting BUFR data
      could result in an empty plot

   -  automatic generation of Macro from *Simple Formula* icon could
      result in incorrect code - fixed

   -  upload to Weather Room screen updated to work with new framework

-  **Display Window icon:** more flexibility when designing page layouts

-  **Desktop improvements**:

   -  the status bar now shows information about a link's target when
      the mouse hovers over an icon which is a symbolic link

   -  the mouse wheel behaves more nicely when scrolling through an icon
      editor which contains comboboxes

Export Version 4.5.1
====================

**External release 2015-02-11**

`Version 4.5.1-export became available. See
the  <#export-version-4.5.7>`__\ `Development
Snapshots <https://confluence.ecmwf.int/display/METV/Development+Snapshots>`__
page for download.

Note: this version requires Magics 2.24.0 in order to build with
plotting enabled.

-  **Contouring**: added new Magics parameters for more control over the
   rainbow contouring:

   -  contour_line_thickess_rainbow_list,
      contour_line_thickness_rainbow_list_policy,
      contour_line_style_rainbow_list and
      contour_line_style_rainbow_list_policy

   -  added an example to the
      `Gallery <https://confluence.ecmwf.int/display/METV/Gallery>`__
      illustrating how rainbow contouring can replace Metview 3's split
      contours - see :ref:`Rainbow Isolines
      Example <gallery_rainbow_contour_diffs>`

-  **PostScript output**: uses the new Magics default of RGB colour
   space (was CMYK) when producing PostScript output in order to
   maintain consistency between versions of GhostScript installed on
   different platforms

-  **Geo View**: allow MAP_VERTICAL_LONGITUDE to be set in Geos
   projection in order to simulate various geostationary satellites.
   Note that the coastlines have some stray lines when certain globe
   rotations are used.

-  **Hovmoeller**: fixed issue where an empty plot was obtain when the
   requested line was exactly vertical, i.e. if the longitudes at each
   end were the same

-  **Cross Section**: support for general height-based coordinate GRIB
   data

-  **Desktop**:

   -  fixed a crash which occurred when running a macro which generates
      its own user interface

   -  icons moved into a Folder icon now get a sensible position

   -  fixed issue where editing some specific Metview 3 icons caused a
      crash

   -  in the Contouring icon editor, parameter
      CONTOUR_LINE_COLOUR_RAINBOW_COLOUR_LIST now has a proper colour
      list helper tool

-  **Build**: like much other ECMWF software, Metview now uses CMake for
   its build system (see `Installation
   Guide <https://confluence.ecmwf.int/display/METV/Installation+Guide>`__)

   -  now supports Mac OS X - we welcome feedback on this, and are aware
      that there are some minor issues on retina displays

   -  Motif support disabled by default, but can be enabled

   -  parallel builds now supported on multi-core machines, e.g. make -j
      8

Test Version 4.5.0
==================

`Introduced 2015-01-06 (Linux desktops, lxab cluster,
ecgb) <#export-version-4.5.7>`__

-  `Installed as metview4_new <#export-version-4.5.7>`__

-  `Built with Magics 2.23.6. See the Magics <#export-version-4.5.7>`__
   `Change
   History <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__.

-  Built with **GRIB_API** 1.12.3

-  Built with **ODB_API** version 0.9.31

-  Built with **emoslib** 000400

-  **User Interface**: the new *Desktop* user interface (see `New
   Desktop user
   interface <https://software.ecmwf.int/wiki/display/METV/New+Desktop+user+interface>`__)
   is now the default

-  **Desktop**: various improvements, including:

   -  improvements in colour-selection helper in icon editors

   -  'rename' action added to icon context menus (shortcut: F2)

   -  icon filter is now case-insensitive

   -  fixed case-sensitivity issue in the *New Icon* dialogue

   -  fixed issue where when a folder tab was moved it became deselected

   -  fixed issue where creating a new icon could shift the position of
      existing icons

   -  icon bounding rectangle has been slightly enlarged

-  **Plotting**: fixed issue where the association of visdefs to data
   did not work in some cases with multiple data sets

-  **Macro**: fixed issue where the
   `distance() <https://software.ecmwf.int/wiki/display/METV/Geopoints+Functions>`__
   function returned an invalid result; this could happen when one of
   the geopoints was at exactly the same location as the target point

-  **Macro**: various gridpoint functions now support GRIBs which are on
   sub-areas of reduced lat/lon grids

-  **Wind**: Metview now recognises 10ua and10va as a wind vector pair

-  **Coastlines**: now have new value FULL for parameter
   MAP_COASTLINE_RESOLUTION

-  **BUFR Examiner**: masterTableVersion and localTableVersion have been
   added to the default profile

-  **Stations**: updated the *Stations* database with the latest WMO
   stations

-  **VAPOR**: the `VAPOR
   Prepare <https://software.ecmwf.int/wiki/display/METV/VAPOR+Prepare>`__
   icon now supports experimental GRIB fields with variable height
   coordinates

-  **Reprojection**: uses new code to convert from satellite to regular
   lat/lon projection; note, however, that this module is no longer
   required for the plotting of satellite images stored in GRIB -
   Metview can now plot them directly.

-  **Build**: like much other ECMWF software, Metview now uses CMake for
   its build system (see `Installation
   Guide <https://confluence.ecmwf.int/display/METV/Installation+Guide>`__)

   -  now supports Mac OS X - we welcome feedback on this, and are aware
      that there are some minor issues on retina displays; other small
      issues may be present

   -  Motif support disabled by default, but can be enabled
