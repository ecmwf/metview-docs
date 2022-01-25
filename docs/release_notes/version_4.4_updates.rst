.. _version_4.4_updates:

Version 4.4 Updates
///////////////////


Change of default Metview versions on ecgate
============================================

**Done on 2014-11-26** (ecgate only)

-  Command *metview* now launches *metview4*

-  Commands *metview_new* and *metview_test* now launch *metview4_new*

-  Command *metview_old* now launches *metview4_old*

-  Commands *metview3*, *metview3_test* and *metview3_old* are still
   available for running Metview 3

-  See `Metview at
   ECMWF <https://software.ecmwf.int/wiki/display/METV/Metview+at+ECMWF>`__
   for details of the version names

User Version 4.4.10
===================

**Upgrade 2014-10-08** (Linux desktops, lxab cluster, ecgate)

-  Version 4.4.10 became *User Version* (command metview or metview4 on
   ecgate) at ECMWF

Export Version 4.4.10
=====================

**External release 2014-10-01**

Version 4.4.10-export became available. See the
`Releases <https://software.ecmwf.int/wiki/display/METV/Releases>`__
page for download.

Test Version 4.4.10
===================

**Introduced 2014-10-01** (Linux desktops, lxab cluster, ecgb)

* At ECMWF:

  -  Installed as *metview4_new*

  -  Built with **Magics 2.23.1.**

  -  Built with **GRIB_API** 1.12.3

  -  Built with **ODB_API** version 0.9.31

  -  Built with **emoslib** 000396

-  **Cross Section and Average**: parameter **Interpolate Values** is no
   longer available in the user interface, as Metview will always
   compute the result on the actual vertical levels of the input data,
   without applying any vertical interpolation. The only exception is
   when there is a need to convert model level to pressure level data.
   In this case, model level and LNSP data are required and the
   algorithm to compute the set of target pressure level values has been
   changed. Previously, these levels were computed by taking a fixed
   number of evenly spaced intervals between the top and bottom
   pressure. This led to a lack of detail in the upper atmosphere. The
   new scheme computes the set of target pressure level values as
   follows: for each input model level, compute the average pressure
   from all points on that level.

-  **Cross Section and Average**: better handling of missing values from
   the input data

-  **Hovmoeller**: better handling of missing values from the input data

-  **Build**: fixed issue which could cause the Metview build to fail on
   Fedora 20 (and maybe other) systems; the symptom is the following
   error message during the last stage of compilation:

   -  convert: unrecognized color \`snow1' @
      warning/color.c/GetColorCompliance/947.

Test Version 4.4.9
==================

**Introduced 2014-09-08** (Linux desktops, lxab cluster, ecgb)

* At ECMWF:

  -  Installed as *metview4_new*

  -  Built with **Magics 2.23.1.**

  -  Built with **GRIB_API** 1.12.3

  -  Built with **ODB_API** version 0.9.31

  -  Built with **emoslib** 000396

-  **Reprojection**: now copies more meta-data (e.g. satellite and
   channel ID) from input to output GRIB

-  **Grib Examiner**: now works on MARS icons which return satellite
   imagery

-  **User Interface**: now recognises JPEG, GIF and TIFF as icon types

-  **Desktop**: improvements in Metview's :ref:`new user interface <mv_desktop_overview>` (invoked by adding -desktop to the Metview command line)

   -  Right-click \| 'Save result' now works on MARS icons which return
      satellite imagery

   -  Icon editors: colour list editor now displays correctly when
      disabled

Export Version 4.4.8
====================

**External release 2014-08-13**

Version 4.4.8-export became available.

-  **Spectra**: the
   `Spectra <https://software.ecmwf.int/wiki/display/METV/Spectra>`__
   module has been re-instated in Metview 4, providing the same level of
   functionality as Metview 3 (it is intended to expand this in the
   future)

-  **Weather Room**: added facilities for analysts to `send plots to the
   Weather Room video
   wall <https://software.ecmwf.int/wiki/display/METV/Exporting+Metview+plots+to+the+Weather+Room+Wall>`__
   and to synchronise plots between Metview and the wall (ECMWF only)

-  **Thermo View**: `new
   icon <https://software.ecmwf.int/wiki/display/METV/Thermo+View>`__
   for handling the view parameters of thermodynamic diagrams (the
   ability to drag and drop data into this view has yet to be
   implemented)

-  **Fonts**: updated the visual definition icons to provide the full
   list of Magics fonts (was Serif and SansSerif, is now Arial, Courier,
   Helvetica, Times, Serif, SansSerif and Symbol). The icons affected
   are `Axis
   Plotting <https://software.ecmwf.int/wiki/display/METV/Axis+Plotting>`__, `Coastlines <https://software.ecmwf.int/wiki/display/METV/Coastlines>`__,
   `Contouring <https://software.ecmwf.int/wiki/display/METV/Contouring>`__,
   `Legend <https://software.ecmwf.int/wiki/display/METV/Legend>`__,
   `Symbol
   Plotting <https://software.ecmwf.int/wiki/display/METV/Symbol+Plotting>`__
   and `Text
   Plotting <https://software.ecmwf.int/wiki/display/METV/Text+Plotting>`__.
   **Please note**: in line with a change in Magics, parameter **Symbol
   Text Font Name** has been changed to **Symbol Text Font**. This might
   affect macros or icons which set the old parameter.

-  **Macro**: extended the nearest_gridpoint_info() Macro function to
   include the distance of the found point from the target point

-  **Cross Section**: it was not possible to create a cross section (or
   some other types of derived data) from an experimental GRIB where the
   parameter's shortName is not alpha-numeric, e.g. "~" or is missing;
   this has been fixed

-  **Cross Section**: now properly handles missing values when
   converting from model levels to pressure levels

-  **Reprojection**: now takes missing values in the input GRIB file
   into account

-  **Reprojection**: now copies meta-data (e.g. date, time, paramId)
   from input to output GRIB

-  **Grib To Geopoints**: fixed issue where some GRIB 2 files could not
   be converted because of differences in GRIB_API keys between GRIB 1
   and 2

-  **Lambert**: fixed issue where Lambert grids stored in GRIB 2 could
   not be interpreted because of differences in GRIB_API keys between
   GRIB 1 and 2

-  **Grib Examiner**: fixed issue where occasionally the last-used
   profile was not remembered between sessions

-  **Desktop**: many improvements in Metview's :ref:`new user interface <mv_desktop_overview>` (invoked by adding -desktop to the Metview command line)

   -  added an advanced icon search dialogue

   -  fixed issue where the editing of a floating-point number in an
      icon editor caused the decimal point to disappear (still to be
      fixed when editing a list of numbers)

   -  improvement in layout of icons on the first visit to a given
      folder

   -  fixed issue where icon drop boxes in editors were not greyed out
      when not needed

   -  the e-mailing of icons is now more robust when the message
      contains special characters

   -  the icon output log no longer misinterprets certain characters as
      HTML codes

   -  bookmarks are now saved as soon as they are modified

   -  colour-selection helper improved when choosing a colour from the
      colour grid

   -  fixed issue where the text cursor did sometimes not appear when
      renaming an icon (only when built with Qt 4.8)

   -  fixed issue where some 'family editor' icons could not be edited

   -  relaxed a case-sensitive check when switching the icon editor back
      from text mode

   -  the Display Window icon editor now correctly displays the page
      size (e.g. A3/A4)

   -  improved file scanning when figuring out an icon's type

   -  useful graphical icons are displayed in the host system's task bar

   -  implemented the *Empty Wastebasket* action

   -  in icon editors, the 'clear text' button is now highlighted when
      the mouse cursor hovers over it

   -  we would like as much feedback as possible on the new interface
      before we make it the default version!

-  **Documentation**: documented the following icons: `Cross Section
   Data <https://software.ecmwf.int/wiki/display/METV/Cross+Section+Data>`__,
   `Cross Section
   View <https://software.ecmwf.int/wiki/display/METV/Cross+Section+View>`__,
   `Average
   Data <https://software.ecmwf.int/wiki/display/METV/Average+Data>`__,
   `Average
   View <https://software.ecmwf.int/wiki/display/METV/Average+View>`__,
   `Vertical Profile
   Data <https://software.ecmwf.int/wiki/display/METV/Vertical+Profile+Data>`__,
   `Vertical Profile
   View <https://software.ecmwf.int/wiki/display/METV/Vertical+Profile+View>`__,
   `Hovmoeller
   Data <https://software.ecmwf.int/wiki/display/METV/Hovmoeller+Data>`__,
   `Hovmoeller
   View <https://software.ecmwf.int/wiki/display/METV/Hovmoeller+View>`__

-  **Wind**: removed the Streamlines options from the `Wind
   Plotting <https://software.ecmwf.int/wiki/display/METV/Wind+Plotting>`__
   icon until this feature is fully implemented

-  **Build**: fixed configure option --with-wmo-code

Export Version 4.4.7
====================

**External release 2014-05-13**

Version 4.4.7-export became available.

Test Version 4.4.7
==================

**Introduced 2014-05-13** (Linux desktops, lxab cluster, ecgb)

* At ECMWF:

  -  Installed as *metview4_new*

  -  Built with **Magics 2.23.0.**

  -  Built with **GRIB_API** 1.12.1

  -  Built with **ODB_API** version 0.9.31

  -  Built with **emoslib** 000394

-  **Desktop**: Metview's :ref:`experimental new user interface <mv_desktop_overview>` (enabled with -desktop on the command line) has had many small fixes

-  **Macro**: function nearest_gridpoint_info() returns an additional
   member: index, which gives the (1-based) index of the found point in
   the data array

-  **Grib Examiner**: now correctly displays the messages in a GRIB file
   which is the result of enabling **sorting** in the *Grib Filter* icon

-  **Grib Examiner**: for convenience, now creates a user-writeable copy
   of the default key profile on startup

-  **WMS**: fixed an issue where wrong proxy settings were enabled when
   built outside ECMWF

-  **MARS**: creation of new *Mars Retrieval* icons is now enabled
   outside ECMWF when the `Mars Web
   API <https://software.ecmwf.int/wiki/display/METV/Using+the+MARS+Web+API+from+Metview>`__
   access is available

Export Version 4.4.6
====================

**External release 2014-04-29**

Version 4.4.6-export became available. 

Test Version 4.4.6
==================

**Introduced 2014-04-29** (Linux desktops, lxab cluster, ecgb)

* At ECMWF:

  -  Installed as *metview4_new*

  -  Built with **Magics 2.23.0.**

  -  Built with **GRIB_API** 1.12.0

  -  Built with **ODB_API** version 0.9.31

  -  Built with **emoslib** 000394

-  **Tephigrams**: new module - `Thermo
   Data <https://software.ecmwf.int/wiki/display/METV/Thermo+Data>`__ -
   for generating thermodynamic diagrams; plot customisation will be
   available later, now it is possible only with some Macro code

-  **VAPOR**: new module (`VAPOR
   Prepare <https://software.ecmwf.int/wiki/display/METV/VAPOR+Prepare>`__)
   to prepare data for visualisation with the 3D package VAPOR. See `3D
   visualisation with
   VAPOR <https://software.ecmwf.int/wiki/display/METV/3D+visualisation+with+VAPOR>`__
   for more information, including a tutorial

-  **Geo View**: added Mercator projection

-  **NetCDF**: added the facility to plot *XY Vectors* in the `NetCDF
   Visualiser <https://software.ecmwf.int/wiki/display/METV/NetCDF+Visualiser>`__
   icon

-  **Grib Examiner**: added *statistics* to the list of namespaces for
   the *namespace dump* mode

-  **NetCDF**: fixed case where visualisation of netCDF geographical
   matrices caused a crash

-  **NetCDF**: at ECMWF, the *NetCDF Examiner* now uses the netCDF 4
   ncdump in its Ncdump panel (although Metview was already linked with
   the netCDF 4 library, it was calling the default version of ncdump
   for this purpose)

-  **SCM**: fixed an issue where calling the *Scm Run* icon could cause
   later problems in the Metview user interface

-  **SCM**: fixed an issue in the *SCM profile editor* where the
   corresponding table column was not selected when switching between
   parameters

-  **Geo View**: fixed issue where the geographical area was restricted
   to be 360° at the right-hand edge

-  **Geo View**: fixed issue where replacing a *Map View* with a
   *Geographical View* (or vice-versa) was disallowed

-  **Macro**: fixed an issue where calling values(geopoints) returned a
   vector of values even if the geopoints values were of type string; it
   now returns a list of strings in this case

-  **Macro**: fixed issue where the Observation Filter did not work if a
   Display Window had been defined beforehand

-  **Macro**: fixed issue where automatic generation of a Macro from a
   plot derived from a *Simple Formula* icon failed

-  **Macro Editor**: background has been slightly dimmed to help prevent
   eyestrain; this should be user-configurable in the future

-  **Desktop**: Metview's experimental new user interface (enabled with
   -desktop on the command line) has seen many improvements

Export Version 4.4.5
====================

**External release 2014-03-04**

Version 4.4.5-export became available.

Test Version 4.4.5
==================

**Introduced 2014-03-03** (Linux desktops, lxab cluster, ecgb)

* At ECMWF:
  
  -  Installed as *metview4_new*

  -  Built with **Magics 2.23.0.**

  -  Built with **GRIB_API** 1.11.0

  -  Built with **ODB_API** version 0.9.31

  -  Built with **emoslib** 000394

-  **Display Window**: fixed issue where plotting a map with Coastlines
   switched off could cause a crash

-  **Display Window**: now recognises 100u/100v as wind vector
   components and will automatically plot as wind vectors

-  **Observation Plotting**: a new *Observation Plotting* icon has been
   created directly from the available Magics++ parameters. This
   replaces the Metview 3 *Observation Plotting* icon, as many of the
   parameters are different. The macro function is mobs().

-  **Cartesian View**: fixed error when setting both parameters
   X_AUTOMATIC = on and X_AXIS_TYPE = date

-  **Cross Section**: problem with the orography curve has been fixed

-  **Vertical Profile**: internal update to how the resulting netCDF
   variables are named

-  **Examiners**: the data examiners have been updated so that they can
   once again be invoked from the command line with the -e option

-  **SCM**: the Single Column Model interface has been updated so that
   invoking the SCM with two icons simultaneously works without a clash

-  **RTTOV**: the default channel files are now somewhere safe, and not
   stored in a volatile location

-  **MARS**: added latest definition files

-  **MARS**: improvements for accessing ECMWF's MARS  archive from a
   Metview built outside ECMWF

-  **MARS**: improvements for accessing ECMWF's MARS archive via the Web
   API - the Dataset parameter is now visible in the *Mars Retrieval*
   icon (see also `A guide for new
   users <https://software.ecmwf.int/wiki/display/WEBAPI/A+guide+for+new+users>`__)

-  **Macro**: mvl_geopotential_on_ml has been updated to avoid the use
   of deprecated functions

Export Version 4.4.4
====================

**External release 2014-02-06**

Version 4.4.4-export became available. 

Test Version 4.4.4
==================

**Introduced 2014-01-22 (Linux desktops, lxab cluster, ecgb)**

* At ECMWF:

  -  **Installed as metview4_new**

  -  **Built with Magics 2.23.0.**

  -  **Built with GRIB_API 1.11.0**

  -  **Built with ODB_API version 0.9.31**

  -  **Built with emoslib 000394**

-  **Display Window:** fixed issue where the Cursor Data panel was not
   updated when the displayed frame was changed

-  **FLEXTRA:** fixed issue where running in CET mode failed

-  **Meteogram:** local meteogram generation now enabled on all platforms
   (internal to ECMWF)

-  **Cross Section:** can now plot the result of a Cross Section Data
   macro call in a Cross Section View (similarly for Average Data,
   Vertical Profile Data and Hovmoeller Data)

-  **Cross Section:** small fixes. Now, if a model level to pressure level
   conversion is required, Interpolate Values is automatically set to
   Yes. The algorithm for finding an LNSP field to use has become less
   strict: try first to find a LNSP field with the same date/time/expver
   of the given ML fieldset. If not found, find the first LNSP field in
   the fieldset.

-  **Observations:** fixed unwanted pop-up message about observation
   grouping

-  **Macro:** unary functions such as sin and log have been added
   to netCDF processing, e.g. new_nc = sin(nc) . See: `NetCDF
   Functions <https://software.ecmwf.int/wiki/display/METV/NetCDF+Functions>`__

-  **Macro:** automatic generation of a macro from a Map View fixed
   (previously did not honour the geographic region selected)

-  **Macro:** macro library
   function `mvl_geoline <https://software.ecmwf.int/wiki/display/METV/mvl_geoline>`__ has
   been revised so that its input parameters are more sensible and so
   that it can work when given a line with the endpoints at the same
   longitude. Previously the input parameters were left_lon, right_lon,
   top_lat, bot_lat.

   Now they are lat1,lon1,lat2,lon2 - coordinates of the two end-points
   of the line in lat/lon. This means that existing macros which call
   this function will no longer give the correct result unless their
   code is changed!

-  **Macro:** the macro which is automatically-generated from the
   'Generate Macro' button in the Display Window is now saved to the
   expected directory

-  **Symbol Plotting:** the parameter symbol_format is now enabled when
   table mode is on

-  **Wind Plotting:** the wind calm threshold parameters are now enabled
   when the wind calm indicator is off

-  **GRIB:** fixed the behaviour of the environment variable
   METVIEW_EXTRA_GRIB_DEFINITION_PATH so that it adds the correct system
   path to the user's path for GRIB tables

-  **User Interface:** double-clicking on a PostScript icon now visualises
   the file rather than opening it in a text editor

-  **Build:** the configure script now checks whether emoslib has been
   built with GRIB_API support or not

-  **Build:** missing .qrc files now in the tarball

-  **Build:** compilation errors relating to QXmlQuery on Ubuntu fixed

Change of default Metview versions
==================================

**Done on 2013-12-03 (Linux desktops, lxab cluster only)**

-  Command metview now launches metview4

-  Commands metview_new and metview_test now launch metview4_new

-  Command metview_old now launches metview4_old

-  Commands metview3, metview3_test and metview3_old are still
   available for running Metview 3

-  See `Metview at ECMWF <https://confluence.ecmwf.int/display/METV/Metview+at+ECMWF>`__ for more details

Export Version 4.4.3
====================

**External release 2013-11-08**

Version 4.4.3-export became available.

User Version 4.4.3
==================

**Upgrade 2013-11-05 (Linux desktops, lxab cluster, ecgate)**

Version 4.4.3 became User Version (command **metview4**) atECMWF

Test Version 4.4.3
==================

**Introduced 2013-10-16 (Linux desktops, lxab cluster, ecgate)**

-  installed as metview4_new

-  **Macro:** in the case where an icon-function is given an input
   definition which contains either an invalid parameter or an invalid
   value for a parameter, Metview's behaviour was always to reset the
   definition to its defaults. As this causes unexpected results, the
   new behaviour is to stop with an error message in this situation.

-  **Graph Plotting:** changed the default value of Legend from On to Off.
   This once again allows a legend to be plotted when a Graph Plotting
   visual definition is used

Test Version 4.4.2
==================

**Introduced 2013-10-15 (Linux desktops, lxab cluster, ecgate)**

* At ECMWF:

  -  **Installed as metview4_new**

  -  **Built with Magics 2.20.2.**

  -  **Built with latest Mars client code**

  -  **Built with GRIB_API 1.11.0**

  -  **Built with ODB_API version 0.9.31**

  -  **Built with netCDF 4.1.2 libraries for HDF support**

-  **Cross Section, Average, Vertical Profile, Hovmoeller:** redesigned
   these icons so as to have a clearer separation between the
   responsibilities of the Data icons and the View icons. Possible
   action required: please see `New Cross Section, Average, Vertical
   Profile and Hovmoeller modules in Metview
   4.4 <https://software.ecmwf.int/wiki/display/METV/New+Cross+Section%2C+Average%2C+Vertical+Profile+and+Hovmoeller+modules+in+Metview+4.4>`__

-  **Cross Section, Average views:** fixed issues where running in batch
   mode did not work properly when try to generate multiple plots either
   within one PostScript file, or between multiple PostScript files.

-  **Hovmoeller View:** re-introduced Hovmoeller View icon. Added new
   parameter: Vertical Scaling (Linear or Log).

-  **Annotations:** new Annotation View icon available. This accepts a
   Text Plotting icon; in this case it mimics Metview 3's Text View
   icon. If no Text Plotting icon is passed to it, then it mimics
   Metview 3's Empty View icon. See `Migrating from Metview 3 to
   Metview
   4 <https://software.ecmwf.int/wiki/display/METV/Migrating+from+Metview+3+to+Metview+4>`__

-  **Relative Humidity:** re-introduced the Relative Humidity icon. When
   used in Macro, it has been simplified so that it only returns a
   fieldset, rather than the previous behaviour which was to return a
   list which included visual definitions. This may require user-changes
   to Macro code which does something with the result of this module
   call.

-  **Macro:** user-defined Macro functions now take precedence over
   built-in Macro functions of the same name if they are defined
   directly in the user's macro (not simply in their search path). The
   previous behaviour was that Metview's own Macro functions would
   always take precedence.

-  **Macro:** fixed issue where plotting the result of another module call
   could fail.

-  **Macro:** fixed issue where passing a merged fieldset to another
   module resulted in a temporary file not being deleted.

-  **Macro:** fixed issue where the function** global_attributes(netcdf)
   **was crashing if one of the global attributes was more than 1024
   characters.

-  **Macro:** fixed issue where a command-line call to Metview in batch
   mode (option **-b**) failed if the path to the macro script
   contained whitespace.

-  **Macro Editor:** indenting a block of text no longer indents empty
   lines.

-  **Visual definition icons:** updated all visdef icons to reflect the
   latest Magics parameters. This is now done automatically from the
   Magics resource files.

-  **Geopoints to Grib:** fixed issue where a temporary file generated by
   the Geopoints To Grib module was not being deleted.

-  **Geopoints to Grib:** fixed issue where supplying a small Threshold
   value (< 0.5 degrees) meant that some surrounding points outwith the
   threshold area, but within 0.5 degrees, were included in the
   calculations.

-  **Data Examiners:** fixed an issue where invoking one of Metview's data
   examiners from the command line (-e option) with a path that contains
   spaces in it did not work.

-  **ODB:** Metview's ODB tools can now handle 'double' type ODB
   columns.

-  **Plotting:** harmonised the subpage coordinates for the non-geographic
   views (Cartesian, Cross Section, Average, Vertical Profile). This
   means that some plots may be slightly shifted on the page.

-  **RTTOV:** added new functionality for running the RTTOV model from
   within Metview and visualising the results. We plan to release some
   documentation on this.

-  **Geo View:** added new Magics projections - Robinson and  Lambert
   North Atlantic.

-  **NetCDF:** enabled '-e netcdf' option on startup in order to
   start the netCDF examiner on startup, e.g. metview -e netcdf
   /path/to/netcdf/file

-  **Text Plotting:** it is now possible to provide finer-grained control
   over which fields are used in generating a user-defined title which
   accesses GRIB_API keys. see the Magics `Text
   Plotting <https://software.ecmwf.int/wiki/display/MAGP/Text+Plotting>`__ page
   for more details.

-  **Layout:** fixed issue where setting the page orientation to Portrait
   did not work; the workaround was to set up user-defined page
   dimensions - this may no longer work.

-  **MARS:** when installing Metview on a non-ECMWF machine which has
   access to a local MARS server, (configure option
   --enable-mars-access), it is now possible to tell Metview where
   the MARS configuration files are by setting the new configure
   option: --with-local-mars-home=/path/to/mars/home 

