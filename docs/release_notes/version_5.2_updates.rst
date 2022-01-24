.. _version_5.2_updates:

Version 5.2 updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 Version 5.2.4 `3 <#version-5.2.4>`__

2 Version 5.2.3 `4 <#version-5.2.3>`__

3 Version 5.2.2 `5 <#version-5.2.2>`__

4 Version 5.2.1 `6 <#version-5.2.1>`__

5 Version 5.2.0 `7 <#version-5.2.0>`__

6 Highlights `8 <#highlights>`__

7 Other features of Metview 5.2.0
`11 <#other-features-of-metview-5.2.0>`__

Version 5.2.4
=============

**Became metview/new at ECMWF on 2018-11-26 (Linux desktops, ecgate,
lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2018-11-26**

   -  Built
      with **Magics **\ `3.2.3 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.9.2 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.9.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000458 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

   -  Built with\ ** mir 1.0.1**

**Features:**

-  **Python/Macro**: added a function, examine(data) to bring up a data
   examiner from a script. Works with fieldset, geopoints, netcdf, bufr
   and odb data.

-  **MARS:** the default interpolation package used for MARS-based
   gridded interpolations (retrieve/read) can now be set via an
   environment variable. By default, emoslib will be used, but the
   following command, run before startup, will cause Metview to use mir
   instead:

   -  export METVIEW_MARS_INTERP=MIR

Version 5.2.3
=============

**Became metview/new at ECMWF on 2018-11-14 (Linux desktops, ecgate,
lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2018-11-14**

   -  Built
      with **Magics **\ `3.2.2 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.9.2 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.9.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000458 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

   -  Built with\ ** mir 1.0.0**

**Features:**

-  **Python**: fixed issue where values(table, number) returned the
   wrong column (it used 1-based indexing instead of 0-based indexing
   even though it was called from Python)

-  **Thermodynamic diagrams**: fixed issue where wind flags were not
   plotted in the :ref:`Thermo
   View <thermoview_icon>`
   (tephigram, emagram, skew-t)

-  **FLEXTRA**: fixed issue when retrieving etadot data from MARS

Version 5.2.2
=============

**Became metview/new at ECMWF on 2018-11-07 (Linux desktops, ecgate,
lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2018-11-07**

   -  Built
      with **Magics **\ `3.2.1 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.9.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.9.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000457 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

   -  Built with **mir 1.0.0**

**Features:**

-  **mir**: this Metview build is identical to the 5.2.1 version, except
   that it is built with version 1.0.0 of mir and the latest Mars client
   code

   -  *since version 5.1.0, Metview has included mir-based versions of
      various module - see *\ `Version 5.1
      Updates <https://confluence.ecmwf.int/display/METV/Version+5.1+Updates>`__

Version 5.2.1
=============

**Externally **\ `released <https://confluence.ecmwf.int/display/METV/Releases>`__\ ** on
2018-10-23**

**Became metview/new at ECMWF on 2018-10-23 (Linux desktops, ecgate,
lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2018-10-23**

   -  Built
      with **Magics **\ `3.2.1 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.9.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.9.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000457 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

**Features:**

-  **UI**: improved the layout of the style selection widged in
   the :ref:`Contouring <mcont_icon>`
   icon (see screenshot below)

-  **Plotting**: changed the default value of **Subpage Background
   Colour** in the View icons to **None**, now that Magics supports the
   parameter; in Metview 5.2.0, a plot generated with multiple plot
   commands might have ended up showing only the last one

-  **Met3D**: fixed issue where :ref:`Met3D
   Prepare <met3d_prepare_icon>`
   could not retrieve lnsp data

-  **Python**: added the **execute** action to Python scripts, allowing
   them to be executed directly from the context menu

-  **Python**: checked all Macro functions that take or return indexes
   to ensure that they are context-sensitive to whether they are being
   run from Macro or Python

-  **BUFR examiner**: improved speed for BUFR filter

-  **BUFR examiner**: improved speed for generating data dump for
   messages

-  **BUFR examine**\ r: added option to filter by RDB type

-  **BUFR examiner**: fixed issue where BUFR filter hung for tropical
   cyclone data

-  **Code Editor**: fixed issue where dropping an icon into the editor
   could produce unindented code

-  **FLEXTRA**: fixed crash on exiting a Macro/Python script that calls
   flextra_group_get()

-  **Build**: ensure that the style preview images are part of the
   source tarball so that the binary installation packages contain them

-  **Build**: ensure that the palette and style browsers work fully when
   Metview is installed from a bundle

.. image:: /_static/release/version_5.2_updates/image1.png
   :width: 4.16667in
   :height: 1.63854in

*Improved style browser in the Contouring icon*

Version 5.2.0
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2018-09-28
Became metview/new at ECMWF on 2018-09-27 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2018-09-27**

   -  Built
      with **Magics **\ `3.2.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.9.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.9.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.18.0 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000457 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

Highlights
==========

**New parameters in the Contouring icon for using ecCharts styles**

The **CONTOUR AUTOMATIC SETTING** parameter in the
:ref:`Contouring <mcont_icon>`
icon now makes the style selection quick and straightforward. Users can
choose from these three options:

-  Off: manual contouring settings will be used 

-  Ecmwf: the default ecCharts style associated with the field to be
   visualised will be automatically applied

-  Style name: the ecCharts style defined in the **CONTOUR STYLE NAME**
   parameter will be used. When this parameter is active the editor
   features a style browser to help select the appropriate style.

+---------------+--------+--------------------------------------------+
| Icon editor   | Plot   | Macro                                      |
+===============+========+============================================+
| |\_scr        | |\_s   | +---------------------------------------+  |
| oll_external/ | croll_ | |    # Metview Macro                    |  |
| attachments/i | extern | |                                       |  |
| mage2018-9-27 | al/att | |    # \***************************\*   |  |
| _9-29-40-ce56 | achmen | |    LICENSE START                      |  |
| 62c29a214fc5c | ts/ima | |                                       |  |
| c9343c35b4e9a | ge2018 | | \**********************************\* |  |
| b4d2bed8a61c2 | -9-27_ | |                                       |  |
| 6a4e19851b41c | 10-54- | |    #                                  |  |
| 2ad40d03.png| | 45-e56 | |                                       |  |
|               | 2e7394 | |    # Copyright 2018 ECMWF. This       |  |
|               | b3c98d | |    software is distributed under the  |  |
|               | c67fcc | |    terms                              |  |
|               | 02861a | |                                       |  |
|               | 52069c | |    # of the Apache License version    |  |
|               | 28eb9a | |    2.0. In applying this license,     |  |
|               | 53e6a7 | |    ECMWF does not                     |  |
|               | fb4fac | |                                       |  |
|               | e0628b | |    # waive the privileges and         |  |
|               | 5e1157 | |    immunities granted to it by virtue |  |
|               | 1.png| | |    of its status as                   |  |
|               |        | |                                       |  |
|               |        | |    # an Intergovernmental             |  |
|               |        | |    Organization or submit itself to   |  |
|               |        | |    any jurisdiction.                  |  |
|               |        | |                                       |  |
|               |        | |    #                                  |  |
|               |        | |                                       |  |
|               |        | |    # \****************************\*  |  |
|               |        | |    LICENSE END                        |  |
|               |        | |    \                                  |  |
|               |        | | ***********************************\* |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |    grib **=** retrieve(param:'2t',    |  |
|               |        | |    levtype: "surface", grid:[1,1])    |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |    cont **=**                         |  |
|               |        | |    mcont(contour_automatic_setting :  |  |
|               |        | |    "style_name",                      |  |
|               |        | |                                       |  |
|               |        | |    contour_style_name :               |  |
|               |        | |    "sh_all_fM52t48i4_light",          |  |
|               |        | |                                       |  |
|               |        | |    legend : "on"                      |  |
|               |        | |                                       |  |
|               |        | |    )                                  |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |                                       |  |
|               |        | |    plot(grib, cont)                   |  |
|               |        | +=======================================+  |
|               |        | +---------------------------------------+  |
|               |        |                                            |
|               |        | Code Block 1 Macro to plot fields with an  |
|               |        | eccharts style                             |
+---------------+--------+--------------------------------------------+

**New palette-selection helper in
the **\ :ref:`Contouring <mcont_icon>`\ ** icon for
when Contour Shade Colour Method is Palette**

.. image:: /_static/release/version_5.2_updates/image4.png
   :width: 3.13542in
   :height: 2.71605in

**Added option to hide disabled parameters in icon editors**

There is a new option in all icon editors to hide the disabled
parameters instead of greying them out (hiding the parameters is the
default behaviour, a button at the top allows to toggle the behaviour).
This feature can be particularly useful for editors with a very large
number of parameters (e.g. Contouring icon) **.**


.. image:: /_static/release/version_5.2_updates/image5.png
   :width: 2.23584in
   :height: 2.60417in
\ 
.. image:: /_static/release/version_5.2_updates/image6.png
   :width: 2.20921in
   :height: 2.60417in


**Added support for **\ `tilted perspective
projection <https://proj4.org/operations/projections/tpers.html>`__\ ** in
the Geographic View icon**


.. image:: /_static/release/version_5.2_updates/image7.png
   :width: 2.62548in
   :height: 2.60417in
\ **  **\ 
.. image:: /_static/release/version_5.2_updates/image8.png
   :width: 2.5in
   :height: 2.49381in


Other features of Metview 5.2.0
===============================

-  **Plotting**:

   -  allow the newpage() command to take no parameters and to be
      included directly in a plot() command like this:

      -  | setoutput(ps_output(output_name : "foom"))
         | plot(dw,my_view,my_coast,mtext(text_font_size:0.5,text_lines:["aaaa"]),
         | newpage(),
         | dw,my_view,my_coast,mtext(text_font_size:0.5,text_lines:["bbbb"]))

   -  added **Monthly** and **Climate** axis types (possible values of
      **Axis Date Type**)

   -  fixed an issue where dropping a GeoView into a plot window on Mac
      OSX did not work

-  **Python**:

   -  new quick-access Desktop menu item to create a new Python script

   -  on startup in interactive mode, Metview loads the
      metview-python/new module if it is not already loaded

   -  updated
      the `Gallery <https://confluence.ecmwf.int/display/METV/Gallery>`__
      so that all examples have Python code

   -  the Macro Editor now uses better syntax highlighting for Python
      when different colour schemes are used

   -  functions that return indexes (e.g. find) are now aware of whether
      they are running under Macro or Python, and return either 1-based
      (Macro) or 0-based (Python) indexes accordingly

   -  now supports the passing of 32-bit floating point vectors/numPy
      arrays (previously only 64-bit floats were accepted)

   -  fixed an issue where passing the result of filtering a fieldset
      using the mv.read() function returned the original fieldset not
      the filtered one

   -  now allows the setting of sub-elements of a Fieldset object, e.g.

      -  | g = read('gribfile.grib')
         | g[3] = g[3] + 100

-  **Data examiners**:

   -  the BUFR Examiner now offers autocomplete suggestions for keys
      from all the messages selected so far (the previous behaviour was
      to offer only the keys present in the first message)

   -  filtering compressed BUFR messages has been significantly sped up

   -  the BUFR Examiner's initial scan of messages is now
      multi-threaded, enabling a more responsive interface when it
      starts up

   -  fixed issue when filtering BUFR messages with multiple (nested)
      coordinates did not work

-  **GRIB**:

   -  fixed issue where the ECCODES_DEFINITION_PATH environment variable
      could disrupt Metview's operations on GRIB data. Please
      set METVIEW_EXTRA_GRIB_DEFINITION_PATH if you need to override the
      definition path.

-  **BUFR Picker**:

   -  fixed issue where selection on multiple coordinates did not work

-  **GRIB To Geopoints**:

   -  added an option to :ref:`Grib To
      Geopoints <grib_to_geo_icon>`
      called **Missing Data**, with possible values of **Include**
      (default)/**Ignore** in order to reduce the volume of data
      returned when there are missing values

-  **Stations**:

   -  updated the list of WMO stations

-  **Macro**:

   -  improved error message when function not found or arguments are of
      incorrect type

   -  documented the
      :ref:`sort_indices() <macro_vector_fn>`
      function

   -  added new colour themes to the macro editor

-  **Macro editor**

   -  The Macro Editor has\ ** **\ introduced four new colour schemes on
      top of the existing ones: **blueish, borland classic, solarized**
      and **solarized dark (light comment)**. The colour scheme can be
      selected from the Settings -> Colour Scheme menu.
      
.. image:: /_static/release/version_5.2_updates/image9.png
   :width: 2.70066in
   :height: 1.5625in
\ 
.. image:: /_static/release/version_5.2_updates/image10.png
   :width: 2.75696in
   :height: 1.5625in
\ 
.. image:: /_static/release/version_5.2_updates/image11.png
   :width: 2.71295in
   :height: 1.5625in
\ 
.. image:: /_static/release/version_5.2_updates/image12.png
   :width: 2.7112in
   :height: 1.5625in


-  **Met.3D**:

   -  the :ref:`Met3D
      Prepare <met3d_prepare_icon>`
      module uses a more efficient means of retrieving data from MARS by
      avoiding tape access if possible

-  **SCM**:

   -  in the Single Column Model `profile
      editor <https://confluence.ecmwf.int/display/METV/The+SCM+Interface+in+Metview+-+Tutorial>`__,
      fixed issue where if consistency mode is enabled and we change
      temperature, relative humidity is not adjusted even if all the
      necessary variables are present (t, p, r, q)

-  **FLEXTRA/FLEXPART**:

   -  fixed issue where
      :ref:`FLEXTRA <the_flextra_interface>`
      output files read via a relative path could not be found

   -  added the ability for :ref:`Flextra
      Prepare <flextra_prepare_icon>`
      and :ref:`Flexpart
      Prepare <flexpart_prepare_icon>`
      to take their input directly from GRIB data

-  **User Interface**:

   -  in
      the :ref:`Contouring <mcont_icon>`
      icon, the parameter Contour Shade Colour Table now has a proper
      colour list editor

-  **Build**:

   -  fixed problem finding RPC libraries on newer systems that have
      these separated from the system libraries

   -  fixed problem building the `Metview
      Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`__
      on Ubuntu 16.04











