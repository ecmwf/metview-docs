.. _version_5.8_updates:

Version 5.8 Updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 Version 5.8.3 `3 <#version-5.8.3>`__

2 Version 5.8.2 `4 <#version-5.8.2>`__

3 Version 5.8.1 `5 <#version-5.8.1>`__

Version 5.8.3
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2020-04-30
Became metview/new at ECMWF on 2020-04-30 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2020-04-30**

   -  Built
      with **Magics **\ `4.3.3 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.17.1 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.17.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.19.4 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Includes
      version `1.4.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Geopoints:**

-  when reading a line of a geopoints file that has an error in it,
   Metview will now fail and return an empty geopoints rather than risk
   returning wrong values

**Macro/Python:**

-  fixed issue where file handles were not being closed after simple
   operations on netCDF data, such as 'a = nc + 1'

-  fixed issue where valid_date() function did not correctly interpret
   steps whose units are minutes

-  fixed issue where first_derivative_y() function crashed when
   processing GRIB encoded from South to North (also affected the
   vorticity() function)

-  fixed issue where saturation_vapour_pressure() used mixed phase; now
   it uses water phase by default and is controllable by passing a
   second parameter to the function:

   -  saturation_vapour_pressure(t, phase)

   -  where phase can be one of "water", "ice" or "mixed"

**Build:**

-  now uses the standard CMake way of putting the project version number
   directly into the CMakeLists.txt file

Version 5.8.2
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2020-04-01
Became metview/new at ECMWF on 2020-04-01 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2020-04-01**

   -  Built
      with **Magics **\ `4.3.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.17.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.17.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.19.3 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Includes
      version `1.4.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Plotting:**

-  when built with Magics 4.3.1, a crash in the interactive plotting
   window has been fixed (triggered when visualising a GRIB file with
   multiple fields)

**Macro/Python:**

-  fixed issue when creating an empty NCOLS-formatted geopoints with the
   create_geo() function

-  fixed issue when using a numpy array of indexes into a Fieldset

Version 5.8.1
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2020-03-10
Became metview/new at ECMWF on 2020-03-10 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2020-03-10**

   -  Built
      with **Magics **\ `4.3.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.17.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.17.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.19.3 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Includes
      version `1.4.0 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Plotting:**

-  simplified the switching  between layer and data tabs in the
   interactive plot window

   -  the Data tab is no longer required in the side panel

   -  to access the metadata and statistics for a given layer, just
      double-click on its thumbnail in the sidebar

   -  | to get back to the list of layers, click the Layer List button
      | 
.. image:: /_static/release/version_5.8_updates/image1.png
   :width: 2.44792in
   :height: 2.60417in
 
           
          
.. image:: /_static/release/version_5.8_updates/image2.png
   :width: 2.44792in
   :height: 2.60417in


-  the :ref:`Geographical
   View <geoview_icon>`
   icon has new parameters to enable the selection of predefined areas
   and projections by setting **Area Mode** to **Name** and then
   selecting from the drop-down list of areas to set the **Area Name**
   parameter:

   .. image:: /_static/release/version_5.8_updates/image3.png
      :width: 3.56338in
      :height: 2.60417in

-  new parameter in
   the :ref:`Legend <mlegend_icon>`
   icon to control the size of the main legend box

   -  legend_automatic_box_margin is a percentage of the width/length of
      the main plot area (the subpage) that will not be taken up by the
      main legend box. The default is to leave a 5% gap on either end -
      to make the legend the same size as the plot area, set this
      parameter to 0 (zero).

-  with Magics 4.3.0, the Cursor Data now works with NetCDF files where
   netcdf_position_type is 'matrix'

-  the :ref:`ECCHARTS <eccharts_icon>`
   icon has changed the behaviour of the **Step** parameter so that it
   behaves the same way as in the :ref:`MARS
   Retrieval <retrieve_icon>`
   icon

-  the :ref:`ECCHARTS <eccharts_icon>`
   icon has a new parameter, **Title**, which can be used to select a
   formatting style for the title; options are **Default** and **Style
   1**

**GRIB:**

-  added a filter to the standard namespace dump for easier location of
   keys

   .. image:: /_static/release/version_5.8_updates/image4.png
      :width: 3.13542in
      :height: 1.375in

**BUFR:**

-  the BUFR Examiner now shows the possible minimum and maximum values
   for each descriptor based on  the available bits per value and its
   scaling factor

   .. image:: /_static/release/version_5.8_updates/image5.png
      :width: 3.13542in
      :height: 1.63542in

-  | the BUFR Examiner now shows the total number of subsets across all
     messages
   |  |\_scroll_external/other/74212_image-2020-01-09-10-25-45-379-0acc30772f27a37bed95e7288167cf32d7d63fcc53e614a9f03e2446e5d7a6f9.png|

-  improved performance when the BUFR Examiner is initially scanning the
   messages in the given BUFR file

-  improved performance when unpacking messages

**Desktop:**

-  new startup option '-fs' followed by a font size to specify the
   default font size for everything in the user interface; now you can
   start Metview like this for large fonts:

.. note::

 metview -fs 16                                                        

-  fixed issue where dropping a :ref:`MARS
   Retrieval <retrieve_icon>`
   icon into a Python code editor generated the parameter name 'cls'
   instead of the correct 'class_'

-  fixed issue where the data examiners and Code Editor did not work on
   macOS Catalina

**Macro/Python:**

-  new function to compute relative humidity from temperature and
   dewpoint: 

   -  relative_humidity_from_dewpoint(t, td)

   -  Works for numbers, vectors and fieldsets. Input values should be
      in K.

-  functions saturation_vapour_pressure(), mixing_ratio() and
   vapour_pressure() now work with vectors and fields

-  improved general performance of geopoints operations by keeping data
   in memory more often and only writing to disk when really necessary

-  the function metadata(geopoints) will now return an empty
   definition/dictionary if there is no metadata; previously nil/None
   was returned

-  in Python, allow indexed assignment using any type (e.g. strings) as
   an index; the particular case in mind was this:

.. note::

 gp =                                                              
 metview.cre                                                           
 ate_geo(type\ ='ncols',vals_0\ =\ numpy.array([10.,20.,30.])) 
                                                                       
 gp['vals_0'] = numpy.array([-\ 10.,\ -\ 20.,\ -\ 30]) 

-  new function purge_mem() to release unused memory; this can be called
   at any time

-  the nearest_gridpoint() function that takes a geopoints variable as
   the list of target points now has a new parameter, 'store_locs',
   which, if present, will ensure that the resulting geopoints will be
   of type NCOLS and will contain the additional
   columns nearest_latitude and nearest_longitude, which contain the
   co-ordinates of the nearest gridpoint in the field

   -  nearest_gridpoint(my_fieldset, my_geopoints, "store_locs")

-  improved the way that functions are exposed to the Python layer

-  changed slightly the behaviour of the nearest_gridpoint() function
   when providing a geopoints for the target points:

   -  The resulting geopoints will contain all the coordinate columns
      from the input geopoints (with date, time and level taken from the
      GRIB), and one value column only, taken from the GRIB. The value
      columns from the input geopoints are discarded. The metadata from
      the input geopoints is also discarded, as it is probably not valid
      for the GRIB data.

-  fixed an issue in the nearest_gridpoint() function whereby it did not
   preserve the stnid column from an input geopoints

-  fixed an issue in the surrounding_points_indexes() function when the
   input is a global regular lat/lon grid that does not start at the
   poles and the target point is outside the first/last latitude

-  fixed an issue in the surrounding_points_indexes() function for
   reduced lat/lon grids when the target point is outside the area
   (defined by zeros in the 'pl' array)

-  fixed issue where some temporary files were not cleaned up on exit of
   a Python script

-  fixed issue where a NetCDF file was not closed after being read

-  fixed issue where
   the :ref:`wmsclient <wmsclient_icon>`
   command did not work under Python



.. |\_scroll_external/other/74212_image-2020-01-09-10-25-45-379-0acc30772f27a37bed95e7288167cf32d7d63fcc53e614a9f03e2446e5d7a6f9.pn.. image:: /_static/release/version_5.8_updates/image6.png
   :width: 4.16667in
   :height: 0.34849in
