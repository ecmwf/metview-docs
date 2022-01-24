.. _version_5.5_updates:

Version 5.5 Updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 Version 5.5.4 `3 <#version-5.5.4>`__

2 Version 5.5.3 `4 <#version-5.5.3>`__

3 Version 5.5.2 `5 <#version-5.5.2>`__

4 Version 5.5.1 `6 <#version-5.5.1>`__

5 Version 5.5.0 `7 <#version-5.5.0>`__

Version 5.5.4
=============

**Became metview/new and metview/default at ECMWF on 2019-06-13** (Linux
desktops, ecgate, lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-06-13**

   -  Built
      with **Magics** `4.0.3 <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__

   -  Built
      with **ecCodes** `2.12.5 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.12.5+released>`__

   -  Built
      with **ODB_API** version `0.19.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000461 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=131391857>`__

   -  Built with **mir 1.2.5**

**Bug fixes:**

-  **MARS:** linked with latest MARS client to avoid unwanted repeated
   connections to incorrect server. The symptoms were lots of warning
   messages, and longer-than-usual MARS retrievals (issue only seemed to
   arise on 2019-06-12)

Version 5.5.3
=============

**Became metview/new at ECMWF on 2019-05-10** (Linux desktops, ecgate,
lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-05-09**

   -  Built
      with **Magics** `4.0.3 <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__

   -  Built
      with **ecCodes** `2.12.5 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.12.5+released>`__

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000461 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=131391857>`__

   -  Built with **mir 1.2.4**

**Bug fixes:**

-  **Macro and Python**: fixed a bug where the gradient() function
   returned its output fields in the wrong order if given  multi-field
   fieldset as input

-  **Macro and Python**: fixed a bug where the second_derivative()
   functions returned values that were too large

-  **Plotting**: fixed issue where 200u and 200v were not recognised as
   wind components for plotting

-  **Plotting**: fixed issue where antialiasing was not activated by
   default for new users

-  **Geopoints Examiner**: fixed issue where the values were shown as
   UNKNOWN

-  **Contouring Editor**: fixed issue where keyboard navigation did not
   work in the style and palette selections

Version 5.5.2
=============

**Became metview/new at ECMWF on 2019-04-11** (Linux desktops, ecgate,
lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-04-11**

   -  Built
      with **Magics** `4.0.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__

   -  Built
      with **ecCodes** `2.12.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.12.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000460 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=131391857>`__

   -  Built with **mir 1.2.0**

**Bug fixes:**

-  ** **\ Fixed a bug where contouring of a global Gaussian grid encoded
   in GRIB 1 produced isolines and shading positioned one grid point
   down from where they should be. This bug was introduced in Metview
   5.3.0 (Magics 3.3.1).

Version 5.5.1
=============

**Externally** `released <https://confluence.ecmwf.int/display/METV/Releases>`__\ ** 2019-02-26**

**Became metview/new at ECMWF on 2019-02-26** (Linux desktops, ecgate,
lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-02-26**

   -  Built
      with **Magics** `4.0.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__

   -  Built
      with **ecCodes** `2.12.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.12.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000460 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=131391857>`__

   -  Built with **mir 1.2.0**

**Bug fixes:**

-  Fixed issue when retrieving U/V wind components from MARS (issue
   introduced in Metview 5.5.0)

Version 5.5.0
=============

**Externally**\ `released <https://confluence.ecmwf.int/display/METV/Releases>`__\ **2019-02-15**

**Became  metview/default and metview/new at ECMWF
on 2019-02-15** (Linux desktops, ecgate, lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-02-15**

   -  Built
      with **Magics**\ `4.0.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News+-+archive>`__

   -  Built
      with **ecCodes** `2.12.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.12.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000460 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=131391857>`__

   -  Built with **mir 1.2.0**

**Highlights:**

-  | **Macro and Python**: a new set of functions based on the
     horizontal derivatives of regular lat-lon fieldsets have been
     added. This is the complete list of the new methods:
   | first_derivative_x(), first_derivative_y(), second_derivative_x(),
     second_derivative_y(),
   | gradient(),  geostrophic_wind_pl(), divergence(), laplacian(),
     vorticity()
   | For details please check the :ref:`fieldset
     documentation <macro_fieldset_fn>`
     or see the new Gallery example to compute and plot humidity
     advection
     :ref:`here <gallery_advection>`.

..

   .. image:: /_static/release/version_5.5_updates/image1.png
      :width: 3.47222in
      :height: 2.60417in

-  **Macro and Python:** a new set of functions for :ref:`thermodynamic
   computations <macro_thermo_fn>` 
   have been added

-  **Macro and Python**: new function thermo_parcel_path(), to compute
   and plot a parcel path in a thermodynamic diagram - please see a
   Gallery example
   :ref:`here <gallery_parcel_path_skewt_grib>`
   and for more details check the
   :ref:`documentation <macro_thermo_fn>`

   .. image:: /_static/release/version_5.5_updates/image2.png
      :alt: image-2019-02-05-11-23-12-878.png
      :width: 3.50949in
      :height: 2.60417in

   Figure 1 image-2019-02-05-11-23-12-878.png

-  **Macro and Python**: new function bearing(), to compute the bearing
   between a point and all points in a GRIB field

-  **Macro and Python**: new function edit(), to bring up an interactive
   editor on the given data or file

-  **Macro and Python**: the
   :ref:`gfind() <macro_fieldset_fn>`
   function now puts date, time and level into its resulting geopoints
   variable

-  **Macro Editor**: apply the chosen colour theme to the output area

-  **Tephigram**: fixed issue when using non-ECMWF BUFR data

-  **Thermo View**: new parameter - SUBPAGE_CLIPPING = ON/OFF

-  **Cross Section**: fixed issue when plotting a cross section through
   wind fields

-  **Geopoints**:

   -  introduced a new format of geopoints file, which can contain an
      arbitrary number of named value columns - see
      `Geopoints <https://confluence.ecmwf.int/display/METV/Geopoints>`__ for
      more information

   -  geopoints columns can now be extracted and assigned to using
      direct indexing, e.g. gpt['value'] = gpt['value'] - 273.15

   -  much more efficient way of creating a complete geopoints variable
      from scratch using the new form of the create_geo() function

   -  new
      :ref:`functions <macro_geopoints_fn>`,
      columns() and value_columns() to return a list of column names

   -  the filter()
      :ref:`function <macro_geopoints_fn>`
      can now filter geopoints using a vector as the filter criteria,
      e.g. new = filter(gpts, gpts['precip'] > 5)

   -  improved the display of values in the Geopoints Examiner

-  **Observation Filter and Bufr Picker**: added a new mode where
   multiple parameters can be extracted into the new multi-column
   geopoints format, essentially meaning that several queries may be
   made in one go for greater efficiency

-  **Observation Filter**: fixed issue when decoding string values from
   descriptors

-  **Odb Visualiser**: added new parameter: FAIL_ON_EMPTY_OUTPUT =
   YES/NO

-  **EcCharts**: new layers added to
   the :ref:`ECCHARTS <eccharts_icon>`
   icon: windgust, tmin, tmax, interval-based precipitation layers,
   precipitation rate layers, model climate layers

-  **EcCharts**: improved layer description to include some MARS
   retrieval information

-  **Stations**: updated WMO station list

-  **NetCDF Examiner**: fixed issue where the description of ncbyte
   variables was incorrect

-  **ODB data probe**: the ODB data probe in the Display Window now has
   a new mode (available via the
   
.. image:: /_static/release/version_5.5_updates/image3.png
   :width: 0.25in
   :height: 0.25in
\ icon)
   to only show the values belonging to the point selected by the probe.
   It was added for the easier inspection of multiple satellite channels
   available for the same pixel etc.

..

   .. image:: /_static/release/version_5.5_updates/image4.png
      :alt: image-2018-12-11-08-49-17-883.png
      :width: 2.90641in
      :height: 1.5625in

Figure 2 image-2018-12-11-08-49-17-883.png

-  **General**: improved error message handling between modules

-  **Interpolation**: the Metview source tarball now includes a new
   internal GRIB interpolation package (see `Version 5.4
   Updates <https://confluence.ecmwf.int/display/METV/Version+5.4+Updates>`__
   for more details); if linked additionally with libemos, both packages
   can also be used for comparison.

-  **Installation**: fixed some issues when running on Max OS X


