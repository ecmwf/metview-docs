.. _version_4.2_updates:

Version 4.2 Updates
///////////////////


Test Version 4.2.3
==================

Introduced 2012-04-02 (Linux desktops, lxab cluster; not ecgate)

-  Installed as *metview4_new*

-  Rebuilt with latest Magics 2.15.1

-  Average View icon added

-  ODB Filter does not fail if the query runs correctly but returns no
   data

-  GRIB Examiner has a new tab to show the data values

Update 2012-04-04 Linux desktops, lxab cluster; not ecgate)

-  Fixed issue in stdev(fieldset) macro function (rebuilt with updated
   libMars). This was an issue which would only occur rarely and would
   produce a massive, obviously wrong, number as a result.

Test Version 4.2.2
==================

Introduced 2012-03-13 (Linux desktops, not lxab cluster yet; not ecgate)

-  Installed as *metview4_new*

-  Rebuilt with GRIB_API 1.10.1, odb_api 0.9.12, Magics 2.15.1 and the
   latest Mars client code.

-  Uses latest Magics++ projection code using proj4 to allow more
   projections

-  New icon: Geographical View. This is a replacement for the Map View
   icon and includes the new projections available in Magics. It also
   incorporates a simpler overlay control option. Map View is still
   available, but will not be developed further.

-  Added Vertical Profile Data module

-  Added Cross Section View and Vertical Profile View modules (still
   some development work to be done)

-  New FLEXTRA module for trajectories. See tutorial on the
   :ref:`Tutorials <tutorials>`
   page for more details.

-  Added NetCDF_XY_Points mode to NetCDF Visualiser icon

-  ASCII :ref:`Table Reader <read_table_icon>` can now parse meta-data if it is supplied as lines in the form PARAM1=VALUE1 PARAM2=VALUE2 PARAM3=VALUE3. New macro functions:

   -  **list metadata_keys(table)** returns a list of all the available meta-data keys (list of strings)

   -  **string metadata_value(table, string)**

   -  **list metadata_value(table, list)** given a key (or list of keys), returns the corresponding value(s) from the table's meta-data. For any key that does not exist in the meta-data, a 'nil' variable is returned. If there is no meta-data for the table, then 'nil' is returned.

-  New macro functions:

   -  **number or list find(list, any)** Searches the given list for an item and returns the index of the first occurrence of it. If an optional third argument is given as the string 'all', then a list of the indexes of all occurrences of the item is returned. In both cases, if the item is not contained in the list, nil is returned.

   -  **list unique(list)** Returns a list of the unique elements in the input list.

   -  **vector vector(list)** Returns a vector containing the numeric elements of the input list. Any 'nil' list elements are converted to vector_missing_value. Any other non-numeric elements will cause an error. If the input list is empty, the function returns nil.

   -  **global_attributes(netcdf)** Returns a definition variable holding the netcdf's global metadata

-  Macro function **values(netcdf)** has a new mode to allow more powerful access to data. New syntax: **values(netcdf, list)** where list is a list with the same number of elements as the number of dimensions of the current netCDF variable. The elements (except one) should be numbers, specifying the indexes (1-based) into the respective dimensions from where the value(s) are to be taken. If all elements are numbers, then they simply specify the coordinates for a single value (returned as a single-value vector). Optionally, one of the elements can be set to the string 'all'; in this case, all the values from that dimension are returned in a vector. For example, if the current netCDF variable is defined with 3 dimensions: Q(time, region, exp) then we can obtain the values for all times, for the second region and the fifth exp with this syntax::

      v = values(nc, ['all', 2, 5]).

- Added optional third parameter to **parse()** function. The Macro parse() function now accepts an optional third parameter which specifies the data type that the result should be in.Currently it only accepts 'string', which means that the result will be a list of strings, with no 'intelligent conversion' performed. This can be useful, for instance, when a string such as '4/05/6' is parsed and we wish to preserve the full string '05'.

-  List macro functions now work between dates and lists, e.g.::

      a = date + list # 'list' is a list of numbers

-  List-list macro operators now return nil if the two input lists have
   different numbers of elements. The previous behaviour was to issue an
   error message and stop the macro.

-  Macro function **values(netcdf)** can now handle 'ncChar' string
   variables

-  Layers tab now has 2 modes: 'Layers' and 'Meta-data'

-  Improved meta-data in Layers tab

-  Improved cursor data

-  Improved page layout

-  :ref:`Bufr
   Picker <bufr_picker_icon>` can
   now pick ALL values related to the innermost coordinate. The
   innermost coordinate value can now be given as "ALL" in order to pick
   all corresponding values.

-  Fix in ObsFilter to handle non-compressed multisubset msgs where
   delayed descriptor counts varied from subset to subset.
