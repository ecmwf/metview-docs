.. _version_4.1_updates:

Version 4.1 Updates
///////////////////

Test Version 4.1.5
==================

Introduced 2012-02-01 (Linux desktops, lxab cluster; not ecgate)

-  Installed as *metview4_new*

-  Rebuilt with GRIB_API 1.10.0, odb_api 0.9.9, latest Mars client and
   Magics 2.14.10

Introduced 2012-02-20 (Linux desktops, lxab cluster; not ecgate)

-  Rebuilt Mars client with latest GRIB_API 1.10.0

User Version 4.1.3
==================

**Upgrade 2011-11-28 (Linux desktops, lxab cluster; not ecgate)**

Version 4.1.3 became *User Version* at ECMWF

Test Version 4.1.3
==================

**Update 2011-11-24**

Rebuilt with Magics 2.14.7

Export Version 4.1.3
====================

**External release 2011-11-21**

Version 4.1.3-export became available

.. _test-version-4.1.3-1:

Test Version 4.1.3
==================

Introduced 2011-11-23 (Linux desktops, lxab cluster; not ecgate)

-  Installed as *metview4_new*

-  Data histogram available in the Display Window's 'Data Layer' tab

-  Cursor data in the Display Window shows both scaled and unscaled grid
   point values

-  The standard Mars client has been updated to the version which can
   handle ODB data. This makes the specialised Mars/ODB client redundant
   (it is still available for now though)

-  Fixed BUFR code to work with non-compressed multisubset BUFR messages

-  Enhanced BUFR code to work with NCEP "PrepBUFR" files

-  Fixes in ASCII table-reading code

-  Fix in setoutput() Macro function


Export Version 4.1.2
====================

**External release 2011-11-04**

Version 4.1.2-export became available

User Version 4.1.2
==================

**Upgrade 2011-10-26 (Linux desktops, lxab cluster; not ecgate)**

Version 4.1.2 became *User Version* at ECMWF


Test Version 4.1.2
==================

Introduced 2011-10-19 (Linux desktops, lxab cluster; not ecgate)

Installed as *metview4_new*

Major update, including the following changes:

-  **Plotting**

   -  Added basic page layout to Macro (multiple plots on a single page)

   -  Exporting a plot now allows a user-selected range of pages

   -  New set of Visualiser icons available from the 'Modules
      (Plotting)' icon drawer. These replace the 'Manager' icons which
      were in an earlier development release. The purpose of these icons
      is to enable the visualisation of certain data types which do not
      normally carry enough meta-information to plot them, or which can
      be plotted in various ways (e.g. in geographical or Cartesian
      space, as a matrix or as points). The supported data types are:

      - NetCDF - NetCDF files
      - ODB - ODB databases
      - Table - ASCII tables (e.g. CSV files)
      - Input - lists of coordinates and values

-  **WMS**

   When zooming in a plot with a WMS layer, a new WMS request is issued
   in order to ensure optimal image quality for the new area

-  **Other**

   -  On-screen font size issue fixed

   -  Uses latest Magics++ features including updated coastlines and new
      legend mode: histogram

-  **Display Window**

   -  Plots can be resized using controls in the toolbar. Note that this
      is a purely graphical scaling; plots are not recomputed.

   -  Redesigned cursor data which now works with GRIB fields, NetCDF
      fields and ODB data

   -  Faster interactive graphics rendering, noticeable mainly in the
      magnifier

   -  New "Layer Data" tab for layer meta-data

-  **ODB**

   -  Complete change to ODB interface in Metview for improved usability
      - old ODB icons will not be visible. Please see the revised ODB
      tutorial for information on the new icons.

   -  Macro: odb_filter() and retrieve_odb() return 'nil' if no data was
      found

   -  See also the relevant entries in "Data Examiners"

   -  MARS-ODB client available

-  **Macro**

   -  Can now read ASCII table files: use the Table Reader icon to help
      define how the file is read. Available functions are:

      * read_table() - read a file into a 'table' variable
      * count() - return the number of columns
      * name() - returns the name of the indexed column
      * values() - returns a vector or a list of strings for the column
      * specified by index or name

   - Renamed various Macro functions for consistency when extracting or setting arrays of values in various data types. The original versions still work, but issue a warning. All these functions work with vectors for efficiency. The list of deprecated functions and the new versions is:

      * *fieldset functions*: gridvals->values, gridlats->latitudes, gridlons->longitudes,set_gridvals->set_values.
      * *geopoint functions*: date->dates, level->levels, latitude->latitudes,longitude->longitudes, value->values, value2->value2s, set_latitude->set_latitudes,set_longitude->set_longitudes, set_level->set_levels, set_date->set_dates,set_time->set_times, set_value->set_values, set_value2->set_value2s.
      * *table functions*: value->values.
      * *odb functions*: value->values.

   -  New Macro function: number(string) - converts a string into a
      number; if a string cannot be converted into a number, then  zero
      is returned. Example: a = number('123.4')

   -  Temporary files are now cleaned more effectively for ODB,
      geopoints and BUFR data

   -  New function waitmode(), mainly useful for debugging: determines
      whether Macro waits immediately for asynchronous (icon-function)
      function calls (1) or not (0 = default). Returns the mode's
      previous value.

   -  New Macro library function mvl_create_netcdf_2d()

- **Macro Editor**

   -  Program > Run Options... for more debugging options:

      -  highlight current execution line

      -  pause between line executions

      -  wait for asynchronous function calls

      -  choose a different run mode

   -  Now detects and warns if a file has been externally modified

- **Data Examiners**

   -  New NetCDF data examiner (right-click > examine)

   -  New geopoints data examiner (right-click > examine)

   -  Added sorting to the Data tab of the ODB Examiner. Sorting can be
      enabled by clicking on any of the data column headers but it is
      only available if no data blocks are used by the ODB Examiner. By
      default for more than 10,000,000 data items to show, the ODB
      Examiner splits the data into individual blocks each having less
      than 10,000,000 items - this limit is configurable from the
      'Settings' menu.

   -  Fixed issue when displaying int values in the Odb Examiner

   -  Added search facilities to all data examiners

-  **New Module 'BUFR Picker'**

   -  Provides users with better access to BUFR satellite data. Users
      can define several coordinate descriptors (with given coordinate
      values), thus providing access to parameters within the given
      coordinates.

   -  Temporary documentation can be found in
      /home/graphics/cgx/docs/mvug-bufr-picker.pdf

-  **Geo To Grib Module**

   -  Added new interpolation methods to determine how points are
      weighted according to their distance from the target point:

      -  Reciprocal - default, and the same as in previous versions:

         .. code-block:: C++

            if( dist == 0 )
               return grid_value(); //Here the point is on the Grid
            weight = 1/dist;

      -  Exponential Mean - note the special case where Tolerance is zero:

         .. code-block:: C++

            if ( Tolerance != 0 )
               weight = exp(-(dist/(pow(Tolerance,2))));
            else
               weight = dist ? 1 : 0;


      -  Exponential Sum - same as Exponential Mean, but the final value is
         not divided by the total weight; when Tolerance is zero, this mode
         will compute the number of source points located at each target
         point.

- **WMS**

   -  Added preview to the plain editor mode of the WMS Client

   -  WMS client editor now only accepts CRSs with a valid bounding box
      for WMS 1.3.0

   -  Added proper handling for percent encoding in URLs

   -  The WMS Client can now handle fractional ISO8601 dates (e.g.
      1991-01) appearing in the TIME dimension

   -  See also the relevant entries in "Plotting"

-  **Other**

   -  Re-introduced VelStr icon (Velocity Potential / Stream Function)

   -  Area selection dialog can now be used to select a single point

- **Support libraries**

   -  The latest Mars client, emoslib 000390 and GRIB_API 1.9.10

   -  Magics 2.14.1
