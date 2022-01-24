.. _version_5.0_updates:

Version 5.0 Updates
///////////////////

Metview

Exported on Jan 24, 2022

Table of Contents
=================

1 Version 5.0.3 `3 <#version-5.0.3>`__

2 Version 5.0.2 `4 <#version-5.0.2>`__

3 Version 5.0.1 `5 <#version-5.0.1>`__

4 Version 5.0.0 Beta `6 <#version-5.0.0-beta>`__

5 Highlights `7 <#highlights>`__

5.1 New interactive layer management inside the plot window, allowing
for faster plot revisions
`7 <#new-interactive-layer-management-inside-the-plot-window-allowing-for-faster-plot-revisions>`__

5.2 Per-colour transparency `7 <#per-colour-transparency>`__

5.3 New colour gradients shading option
`10 <#new-colour-gradients-shading-option>`__

5.4 FLEXPART support added `15 <#flexpart-support-added>`__

6 Macro Editor has new colour schemes
`18 <#macro-editor-has-new-colour-schemes>`__

7 Other features of Metview 5 `19 <#other-features-of-metview-5>`__

Version 5.0.3
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2018-05-xx
Became metview/new at ECMWF on 2018-05-16 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2018-05-16**

   -  Built
      with **Magics **\ `3.0.4 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.7.3 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.7.3+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.17.6 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000455 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__\ ** **

-  **Macro**:

   -  added
      new :ref:`function <macro_geopoints_fn>` to
      return the subtype of a geopoints variable

-  **MARS:**

   -  **rebuilt MARS client with ODB support**

-  **Hovmoeller**:

   -  fixed issue where
      the `Hovmoeller <https://confluence.ecmwf.int/display/METV/Hovmoeller+View>`__ module
      crashed when processing monthly average analysis data

-  **Plotting**: 

   -  Fixed issue where the wind barbs were not plotted in
      a :ref:`Tephigram <thermoview_icon>` (netCDF
      issue, fixed with Magics 3.0.4)

   -  Fixed issue where the SCM Visualiser crashed (netCDF issue, fixed
      with Magics 3.0.4)

   -  Portugal is now on the list of countries with administrative
      borders

   -  fixed crash which occurred in very specific circumstances - if the
      data is GRIB read from a read() command with a source parameter
      with a relative path, and the plot() command contains a view
      definition

-  **Macro Editor**:

   -  fixed keyboard shortcuts which had broken: 'enlarge font' and
      'indent code'

   -  fixed the status line which indicates the time taken for the macro
      to run

-  **Installation**:

   -  built with Qt4 while we investigate crashes on closedown with Qt5

Version 5.0.2 
=============

**Became metview/new at ECMWF on 2018-04-18 (Linux desktops, ecgate,
lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2018-04-018**

   -  Built
      with **Magics **\ `3.0. <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__\ **\ 3**

   -  Built
      with **ecCodes **\ `2.7.3 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.7.3+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.17.6 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000455 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__\ ** **

-  **Macro**: fixes for inline C/Fortran

-  **Build**: Take into consideration the ENABLE_MEMFS option in ecCodes
   when computing paths to definition files (when built as the `Metview
   Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`__)

Version 5.0.1 
=============

**Externally **\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ ** on
2018-03-01
Became metview/new at ECMWF on 2018-03-05 (Linux desktops, ecgate, lxc,
lxop)**

-  **At ECMWF:**

   -  Installed **2018-03-01**

   -  Built
      with **Magics **\ `3.0.1 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes **\ `2.7.0 <https://software.ecmwf.int/wiki/display/ECC/ecCodes+version+2.7.0+released>`__\ ** **

   -  Built
      with **ODB_API** version `0.17.6 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib **\ `000454 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__\ ** **

-  **Plotting**:

   -  added new parameter to
      the :ref:`Contouring <mcont_icon>`
      icon to control the number of threads used when computing isolines
      - can be 1, 4 (default) or 9

   -  it is now possible to drop a Taylor Grid icon into the plot window

-  **Macro**:

   -  added new function to return the indexes of the four points
      surrounding the given location - see the description
      of **surrounding_points_indexes** in :ref:`Fieldset
      Functions <macro_fieldset_fn>`

   -  the `vector <https://confluence.ecmwf.int/display/METV/Vectors>`__
      data type can now be of zero length

   -  new information function is_feature_available() to dynamically
      test for features available in the current Metview build -
      see `Information
      Functions <https://confluence.ecmwf.int/display/METV/Information+Functions>`__

   -  newly created macros now have a .mv extension

   -  fixed issue in the Macro Editor where it did not show output until
      the end of the macro

-  **Stations**:

   -  updated the list of WMO stations used by the Stations module

-  **Installation**:

   -  fixed linking problems on Ubuntu

   -  new CMake option -DENABLE_FORTRAN=OFF (default is ON)

   -  environment variable METVIEW_LOCALHOST is now set by default (set
      to 0 to disable)

   -  startup from the build directory now directly starts Metview
      without the xserv bar; to invoke the xserv bar, start Metview as
      "metview -xserv"

   -  optionally, Metview can now be built with ninja instead of make
      (give the -GNinja option to CMake)

Version 5.0.0 Beta 
==================

**Externally**\ `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\ **on
2017-12-20
Available internally ECMWF via the command "module swap metview/5b"
on 2017-12-20 (Linux desktops, ecgate, lxc, lxop)**

-  **At ECMWF:**

   -  Installed **2017-12-20**

   -  Built with
      **Magics**\ `3.0.0 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built with
      **ecCodes**\ `2.6.0 <https://software.ecmwf.int/wiki/display/ECC/ecCodes+version+2.6.0+released>`__

   -  Built with **ODB_API** version
      `0.17.6 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built with
      **emoslib**\ `000453 <https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56669028>`__\ ** **

.. note::

    Welcome to the beta release of Metview 5.0! This is very close to  
    what we'd like to release in early 2017, so we'd appreciate        
    testing and feedback. Note that this version requires Magics       
    version 3.0.0.                                                     

Highlights
==========

New interactive layer management inside the plot window, allowing for faster plot revisions
-------------------------------------------------------------------------------------------

Visual definitions can now be dropped directly onto specific layers in
the plot window's sidebar, or even edited directly from within the
sidebar! See `Layer
Management <https://confluence.ecmwf.int/display/METV/Layer+Management>`__
for more.


.. image:: /_static/release/version_5.0_updates/image1.png
   :width: 3.52083in
   :height: 4.16667in
\ e

Per-colour transparency
-----------------------

The colour picker in the icon editors now has support for alpha
(opacity) values, and the interactive Display Window now also supports
alpha values per colour. In Macro, these are specified as RGBA, e.g.
"RGBA(1, 0, 0, 0.8)" for a red colour with 80% opacity (0 is invisible,
1 is full opacity). Note that PostScript output does not support
transparency.

+----------+--------+-------------------------------------------------+
| Editor   | Plot   | Macro                                           |
+==========+========+=================================================+
| |\_scrol | |\_sc  | +--------------------------------------------+  |
| l_extern | roll_e | |    # Metview Macro                         |  |
| al/attac | xterna | |                                            |  |
| hments/m | l/atta | |                                            |  |
| etview-t | chment | |                                            |  |
| ranspare | s/tran | |    # \***************************\*        |  |
| ncy-edit | sparen | |    LICENSE START                           |  |
| or-8f66a | t-sat- | |    \**********************************\*   |  |
| 683faf97 | precip | |                                            |  |
| dc1e3564 | -2-e77 | |    #                                       |  |
| 0f91e03d | 310bd7 | |                                            |  |
| 445e78c4 | b9ae1b | |    # Copyright 2017 ECMWF. This software   |  |
| 395745ec | 2af014 | |    is distributed under the terms          |  |
| 426979cf | 51250a | |                                            |  |
| 732848a3 | 545afc | |    # of the Apache License version 2.0. In |  |
| c55.png| | 66c7af | |    applying this license, ECMWF does not   |  |
|          | 7c6d61 | |                                            |  |
|          | 1d8815 | |    # waive the privileges and immunities   |  |
|          | 4577f9 | |    granted to it by virtue of its status   |  |
|          | d3d4f2 | |    as                                      |  |
|          | b.png| | |                                            |  |
|          |        | |    # an Intergovernmental Organization or  |  |
|          |        | |    submit itself to any jurisdiction.      |  |
|          |        | |                                            |  |
|          |        | |    #                                       |  |
|          |        | |                                            |  |
|          |        | |    # \****************************\*       |  |
|          |        | |    LICENSE END                             |  |
|          |        | |    \***********************************\*  |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    # retrieve simulated satellite image    |  |
|          |        | |                                            |  |
|          |        | |    simsat **=** retrieve(                  |  |
|          |        | |                                            |  |
|          |        | |    type : "ssd",                           |  |
|          |        | |                                            |  |
|          |        | |    expver : 0001,                          |  |
|          |        | |                                            |  |
|          |        | |    param : 260510,                         |  |
|          |        | |                                            |  |
|          |        | |    date : **-**\ 3,                        |  |
|          |        | |                                            |  |
|          |        | |    step : 0,                               |  |
|          |        | |                                            |  |
|          |        | |    channel : 9,                            |  |
|          |        | |                                            |  |
|          |        | |    ident : 57,                             |  |
|          |        | |                                            |  |
|          |        | |    instrument : 207                        |  |
|          |        | |                                            |  |
|          |        | |    )                                       |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    # retrieve precipitation                |  |
|          |        | |                                            |  |
|          |        | |    tp **=** retrieve(                      |  |
|          |        | |                                            |  |
|          |        | |    type : "pf",                            |  |
|          |        | |                                            |  |
|          |        | |    stream : "ef",                          |  |
|          |        | |                                            |  |
|          |        | |    levtype : "sfc",                        |  |
|          |        | |                                            |  |
|          |        | |    param : "tp",                           |  |
|          |        | |                                            |  |
|          |        | |    date : **-**\ 3,                        |  |
|          |        | |                                            |  |
|          |        | |    step : 6,                               |  |
|          |        | |                                            |  |
|          |        | |    number : "all",                         |  |
|          |        | |                                            |  |
|          |        | |    grid : [0.5,0.5]                        |  |
|          |        | |                                            |  |
|          |        | |    )                                       |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    prob_tp **=** mean(tp > 0.005) **\***   |  |
|          |        | |    100 # probability of > 5mm of           |  |
|          |        | |    precipitation                           |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    sat_shade **=** mcont(                  |  |
|          |        | |                                            |  |
|          |        | |    legend : "on",                          |  |
|          |        | |                                            |  |
|          |        | |    contour : "off",                        |  |
|          |        | |                                            |  |
|          |        | |    contour_level_count : 20,               |  |
|          |        | |                                            |  |
|          |        | |    contour_label : "off",                  |  |
|          |        | |                                            |  |
|          |        | |    contour_shade : "on",                   |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_technique :               |  |
|          |        | |    "cell_shading",                         |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_cell_resolution : 40,     |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_cell_method :             |  |
|          |        | |    "interpolate",                          |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_max_level_colour :        |  |
|          |        | |    "black",                                |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_min_level_colour :        |  |
|          |        | |    "white",                                |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_colour_direction :        |  |
|          |        | |    "clockwise"                             |  |
|          |        | |                                            |  |
|          |        | |    )                                       |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    tp_prob_shade **=** mcont(              |  |
|          |        | |                                            |  |
|          |        | |    legend : "on",                          |  |
|          |        | |                                            |  |
|          |        | |    contour : "off",                        |  |
|          |        | |                                            |  |
|          |        | |    contour_level_selection_type :          |  |
|          |        | |    "level_list",                           |  |
|          |        | |                                            |  |
|          |        | |    contour_level_list :                    |  |
|          |        | |    [5,20,40,60,80,95,105],                 |  |
|          |        | |                                            |  |
|          |        | |    contour_label : "off",                  |  |
|          |        | |                                            |  |
|          |        | |    contour_shade : "on",                   |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_colour_method : "list",   |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_method : "area_fill",     |  |
|          |        | |                                            |  |
|          |        | |    contour_shade_colour_list :             |  |
|          |        | |    ["RGBA(0.48,0.82,0.78,0.38)",           |  |
|          |        | |                                            |  |
|          |        | |    "RGBA(0.42,0.79,0.27,0.38)",            |  |
|          |        | |                                            |  |
|          |        | |    "RGBA(0.83,0.85,0.2,0.38)",             |  |
|          |        | |                                            |  |
|          |        | |    "RGBA(0.9,0.64,0.23,0.38)",             |  |
|          |        | |                                            |  |
|          |        | |    "RGBA(0.97,0.43,0.43,0.38)",            |  |
|          |        | |                                            |  |
|          |        | |    "RGBA(1,0.0039,1,0.38)"]                |  |
|          |        | |                                            |  |
|          |        | |    )                                       |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    coastlines **=** mcoast(                |  |
|          |        | |                                            |  |
|          |        | |    map_coastline_colour :                  |  |
|          |        | |    "RGB(0.97,0.94,0.41)",                  |  |
|          |        | |                                            |  |
|          |        | |    map_coastline_thickness : 2,            |  |
|          |        | |                                            |  |
|          |        | |    map_grid_colour : "RGB(0.95,0.92,0.69)" |  |
|          |        | |                                            |  |
|          |        | |    )                                       |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |                                            |  |
|          |        | |    plot(simsat, sat_shade, prob_tp,        |  |
|          |        | |    tp_prob_shade, coastlines)              |  |
|          |        | +============================================+  |
|          |        | +--------------------------------------------+  |
+----------+--------+-------------------------------------------------+

New colour gradients shading option
-----------------------------------

New options were added to
the :ref:`Contouring <mcont_icon>` icon,
facilitating more powerful colour scales within a single Contouring
definition. Please see :ref:`How to use the colour gradient
editor <how_to_use_the_colour_gradient_editor>`
for more information on this feature. More examples will be added to
the `Gallery <https://confluence.ecmwf.int/display/METV/Gallery>`__!

+------+--------+-------------------------------------------+----------+
| Plot | Editor | Code                                      | Data     |
+======+========+===========================================+==========+
| |\_  | |\     | +--------------------------------------+  | `visibil |
| scro | _scrol | |    # Metview Macro                   |  | ity.grib |
| ll_e | l_exte | |                                      |  |  <https: |
| xter | rnal/a | |                                      |  | //conflu |
| nal/ | ttachm | |                                      |  | ence.ecm |
| atta | ents/g | |    # \***************************\*  |  | wf.int/d |
| chme | radien | |    LICENSE START                     |  | ownload/ |
| nts/ | ts-edi | |    \                                 |  | attachme |
| grad | tor-ex | | **********************************\* |  | nts/9231 |
| ient | -1-d5b | |                                      |  | 0567/vis |
| s-ex | 7cc5b9 | |    #                                 |  | ibility. |
| -1-a | 654e69 | |                                      |  | grib?api |
| bffe | 286342 | |    # Copyright 2017 ECMWF. This      |  | =v2&modi |
| f343 | 7150e0 | |    software is distributed under the |  | fication |
| 89b7 | fc8594 | |    terms                             |  | Date=151 |
| 5171 | f8018f | |                                      |  | 37831866 |
| 5e1f | 1d3997 | |    # of the Apache License version   |  | 19&versi |
| 3dee | f186f0 | |    2.0. In applying this license,    |  | on=1>`__ |
| caff | 1a20ff | |    ECMWF does not                    |  |          |
| 93d4 | 30d506 | |                                      |  |          |
| d672 | c.png| | |    # waive the privileges and        |  |          |
| 19bc |        | |    immunities granted to it by       |  |          |
| e573 |        | |    virtue of its status as           |  |          |
| 165a |        | |                                      |  |          |
| 4613 |        | |    # an Intergovernmental            |  |          |
| 7e27 |        | |    Organization or submit itself to  |  |          |
| ba61 |        | |    any jurisdiction.                 |  |          |
| 42c. |        | |                                      |  |          |
| png| |        | |    #                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |    # \****************************\* |  |          |
|      |        | |    LICENSE END                       |  |          |
|      |        | |    \*                                |  |          |
|      |        | | **********************************\* |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # read the input grib file        |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_data **=**                     |  |          |
|      |        | |    read('visibility.grib')           |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    #set up the contours              |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_contour **=** mcont(           |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend : "on",                    |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour : "off",                  |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_level_selection_type :    |  |          |
|      |        | |    "level_list",                     |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_level_list :              |  |          |
|      |        | |    [0,500,2000,6000,10000,40000],    |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_label : "off",            |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade : "on",             |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade_colour_method :     |  |          |
|      |        | |    "gradients",                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade_method :            |  |          |
|      |        | |    "area_fill",                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_colour_list :   |  |          |
|      |        | |    ["magenta                         |  |          |
|      |        | | ","yellow","yellowish_green","ecmwf_ |  |          |
|      |        | | blue","RGB(0.74,0.8,0.92)","white"], |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_waypoint_method |  |          |
|      |        | |    : "left",                         |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_technique :     |  |          |
|      |        | |    "hsl",                            |  |          |
|      |        | |                                      |  |          |
|      |        | |    c                                 |  |          |
|      |        | | ontour_gradients_technique_direction |  |          |
|      |        | |    : "anti_clockwise",               |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_step_list :     |  |          |
|      |        | |    [5,3,4,2,3]                       |  |          |
|      |        | |                                      |  |          |
|      |        | |    )                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up the coastlines           |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_coast **=**                    |  |          |
|      |        | |    mcoast(map_coastline_colour :     |  |          |
|      |        | |    "charcoal",                       |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_resolution :        |  |          |
|      |        | |    "medium",                         |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_thickness : 2,      |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_land_shade : "off", |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_sea_shade : "off",  |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_grid_line_style : "dash",     |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_label_height : 0.4,           |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_grid_colour : "charcoal"      |  |          |
|      |        | |                                      |  |          |
|      |        | |    )                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up the geographical view    |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_view **=**                     |  |          |
|      |        | |    geoview(map_area_definition :     |  |          |
|      |        | |    "corners",                        |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_projection : "cylindrical",   |  |          |
|      |        | |                                      |  |          |
|      |        | |    area :                            |  |          |
|      |        | |                                      |  |          |
|      |        | |  [20.00,\ **-**\ 20.00,70.00,50.00], |  |          |
|      |        | |                                      |  |          |
|      |        | |    coastlines : my_coast)            |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set-up the title                |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_title **=**                    |  |          |
|      |        | |    mtext(text_font_size : 0.6,       |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_lines : ["Visibility -       |  |          |
|      |        | |    Gradients method for shading",    |  |          |
|      |        | |                                      |  |          |
|      |        | |    "Computing a range of colours     |  |          |
|      |        | |    with 6 waypoints which are given  |  |          |
|      |        | |    as level list",                   |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font                            |  |          |
|      |        | |    c                                 |  |          |
|      |        | | olour='evergreen'>contour_level_list |  |          |
|      |        | |    : [0, 500, 2000, 6000, 10000,     |  |          |
|      |        | |    40000]</font>",                   |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font                            |  |          |
|      |        | |    colour='ev                        |  |          |
|      |        | | ergreen'>contour_gradients_step_list |  |          |
|      |        | |    : [5, 3, 4, 2, 3]</font>",        |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font colour='red'>5</font>      |  |          |
|      |        | |    colours between <font             |  |          |
|      |        | |    colour='red'>0</font> and <font   |  |          |
|      |        | |    colour='red'>500</font>, "        |  |          |
|      |        | |                                      |  |          |
|      |        | |    & "<font colour='red'>3</font>    |  |          |
|      |        | |    between <font                     |  |          |
|      |        | |    colour='red'>500</font> and <font |  |          |
|      |        | |    colour='red'>2000</font>, "       |  |          |
|      |        | |                                      |  |          |
|      |        | |    & "<font colour='red'>4</font>    |  |          |
|      |        | |    between <font                     |  |          |
|      |        | |    colour='red'>2000</font> and      |  |          |
|      |        | |    <font                             |  |          |
|      |        | |    colour='red'>6000</font>..."],    |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_justification : "left",      |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_colour : "charcoal")         |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up a legend for the field   |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_legend **=**                   |  |          |
|      |        | |    mlegend(legend_text_colour :      |  |          |
|      |        | |    "charcoal",                       |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_text_font_size : 0.4,      |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_display_type :             |  |          |
|      |        | |    "continuous",                     |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_mode : "positional",   |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_x_position : 25.00,    |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_y_position : 0.2,      |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_x_length : 3.00,       |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_y_length : 17.50)      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    plot(my_view, my_data,            |  |          |
|      |        | |    my_contour, my_legend, my_title)  |  |          |
|      |        | +======================================+  |          |
|      |        | +--------------------------------------+  |          |
+------+--------+-------------------------------------------+----------+
| |\_  | |\     | +--------------------------------------+  | `t       |
| scro | _scrol | |    # Metview Macro                   |  | 850.grb  |
| ll_e | l_exte | |                                      |  | <https:/ |
| xter | rnal/a | |                                      |  | /conflue |
| nal/ | ttachm | |                                      |  | nce.ecmw |
| atta | ents/g | |    # \***************************\*  |  | f.int/do |
| chme | radien | |    LICENSE START                     |  | wnload/a |
| nts/ | ts-edi | |    \                                 |  | ttachmen |
| grad | tor-ex | | **********************************\* |  | ts/92310 |
| ient | -2-6b6 | |                                      |  | 567/t850 |
| s-ex | 1102ea | |    #                                 |  | .grb?api |
| -2-1 | 3f77ea | |                                      |  | =v2&modi |
| e29b | d20888 | |    # Copyright 2015 ECMWF. This      |  | fication |
| 47c1 | 1baa38 | |    software is distributed under the |  | Date=151 |
| 192a | 24e6cf | |    terms                             |  | 37831865 |
| de8c | 3cda6f | |                                      |  | 93&versi |
| 0192 | 87ef9e | |    # of the Apache License version   |  | on=1>`__ |
| 0d3a | 82ae4e | |    2.0. In applying this license,    |  |          |
| c98c | f5d5ec | |    ECMWF does not                    |  |          |
| 45e3 | 1fd30b | |                                      |  |          |
| 7cb6 | 1.png| | |    # waive the privileges and        |  |          |
| 8b13 |        | |    immunities granted to it by       |  |          |
| 07ba |        | |    virtue of its status as           |  |          |
| 0378 |        | |                                      |  |          |
| 74b1 |        | |    # an Intergovernmental            |  |          |
| 2244 |        | |    Organization or submit itself to  |  |          |
| daf0 |        | |    any jurisdiction.                 |  |          |
| e6c. |        | |                                      |  |          |
| png| |        | |    #                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |    # \****************************\* |  |          |
|      |        | |    LICENSE END                       |  |          |
|      |        | |    \*                                |  |          |
|      |        | | **********************************\* |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # read the input grib file        |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_data **=** read("t850.grb")    |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    #set up the contours              |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_contour **=** mcont(           |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend : "on",                    |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour : "off",                  |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_level_selection_type :    |  |          |
|      |        | |    "level_list",                     |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_level_list :              |  |          |
|      |        | |    [**-**\ 40,\ **-**\ 20,0,20,40],  |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_step_list : 10, |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_label : "off",            |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade : "on",             |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade_colour_method :     |  |          |
|      |        | |    "gradients",                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_technique :     |  |          |
|      |        | |    "rgb",                            |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_shade_method :            |  |          |
|      |        | |    "area_fill",                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_colour_list :   |  |          |
|      |        | |    ["RGB(0.01961,0.251,0.4157)       |  |          |
|      |        | | ","greenish_blue","white","orangish_ |  |          |
|      |        | | red","RGB(0.3756,0.06648,0.05582)"], |  |          |
|      |        | |                                      |  |          |
|      |        | |    contour_gradients_waypoint_method |  |          |
|      |        | |    : "ignore"                        |  |          |
|      |        | |                                      |  |          |
|      |        | |    )                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up the coastlines           |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_coast **=**                    |  |          |
|      |        | |    mcoast(map_coastline_colour :     |  |          |
|      |        | |    "charcoal",                       |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_resolution :        |  |          |
|      |        | |    "medium",                         |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_thickness : 2,      |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_land_shade : "off", |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_land_shade_colour : |  |          |
|      |        | |    "RGB(0.25,0.25,0.25)",            |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_coastline_sea_shade : "off",  |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_grid_line_style : "dash",     |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_grid_colour : "charcoal"      |  |          |
|      |        | |                                      |  |          |
|      |        | |    )                                 |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up the geographical view    |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_view **=**                     |  |          |
|      |        | |    geoview(map_area_definition :     |  |          |
|      |        | |    "corners",                        |  |          |
|      |        | |                                      |  |          |
|      |        | |    map_projection : "cylindrical",   |  |          |
|      |        | |                                      |  |          |
|      |        | |    area :                            |  |          |
|      |        | |                                      |  |          |
|      |        | |  [20.00,\ **-**\ 20.00,70.00,50.00], |  |          |
|      |        | |                                      |  |          |
|      |        | |    coastlines : my_coast)            |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set-up the title                |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_title **=**                    |  |          |
|      |        | |    mtext(text_font_size : 0.6,       |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_lines : ["Gradients          |  |          |
|      |        | |    technique for shading",           |  |          |
|      |        | |                                      |  |          |
|      |        | |    "Computing a range of colours     |  |          |
|      |        | |    with 5 waypoints given as level   |  |          |
|      |        | |    list",                            |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font                            |  |          |
|      |        | |    c                                 |  |          |
|      |        | | olour='evergreen'>contour_level_list |  |          |
|      |        | |    : [-40,-20,0,20,40]</font>",      |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font                            |  |          |
|      |        | |    colour='ev                        |  |          |
|      |        | | ergreen'>contour_gradients_step_list |  |          |
|      |        | |    : 10 </font>",                    |  |          |
|      |        | |                                      |  |          |
|      |        | |    "<font colour='red'>10</font>     |  |          |
|      |        | |    colours between each 2            |  |          |
|      |        | |    waypoints"],                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_justification : "left",      |  |          |
|      |        | |                                      |  |          |
|      |        | |    text_colour : "charcoal")         |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # set up a legend for the field   |  |          |
|      |        | |                                      |  |          |
|      |        | |    my_legend **=**                   |  |          |
|      |        | |    mlegend(legend_text_colour :      |  |          |
|      |        | |    "charcoal",                       |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_text_font_size : 0.35,     |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_display_type :             |  |          |
|      |        | |    "continuous",                     |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_mode : "positional",   |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_x_position : 25.00,    |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_y_position :           |  |          |
|      |        | |    **-**\ 1.00,                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_x_length : 3.00,       |  |          |
|      |        | |                                      |  |          |
|      |        | |    legend_box_y_length : 17.50)      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |                                      |  |          |
|      |        | |    # plot the data onto the map      |  |          |
|      |        | |                                      |  |          |
|      |        | |    plot(my_view, my_data,            |  |          |
|      |        | |    my_contour, my_legend, my_title)  |  |          |
|      |        | +======================================+  |          |
|      |        | +--------------------------------------+  |          |
+------+--------+-------------------------------------------+----------+

FLEXPART support added
----------------------

| A new interface was developed for the\ ** FLEXPART** Lagrangian
  particle dispersion model. The `FLEXPART interface
  page <https://confluence.ecmwf.int/display/METV/The+FLEXPART+interface>`__ gives
  an overview about the installation and setup of FLEXPART and also
  serves as a hub to access the icon documentation and the :ref:`FLEXPART
  tutorial <using_flexpart_with_metview>`.
|   |\_scroll_external/remote/image2017-10-31_14-2-43-373a32fb6f3e25f2f190ff575e49f5888a2e88897c0dfbf0c4e05e3a1845faec.png|\ |\_scroll_external/remote/image2017-11-9_10-59-5-2bca01d7f920c46d32f33b0282536eba44e8650d0c7c37dd96011b2ac275926e.png|\ |\_scroll_external/remote/image2017-10-31_15-6-34-a168bd0583f319911f91669e282d633e5da9ac829521c5b6ee599820e6cc98d9.png|

Macro Editor has new colour schemes
===================================

The Macro Editor has\ ** **\ introduced two new colour
schemes: **solarized dark** and **solarized light**. The colour scheme
can be selected from the Settings -> Colour Scheme menu. The original
colour scheme is called **Metview** and is kept as default. 


.. image:: /_static/release/version_5.0_updates/image9.png
   :width: 3.14583in
   :height: 1.80009in
\ 
.. image:: /_static/release/version_5.0_updates/image10.png
   :width: 3.14583in
   :height: 1.80626in


Other features of Metview 5
===========================

-  **Plotting**:

   -  added MImport icon for adding image files to a plot (this only
      partially worked in the past)

   -  enabled line and symbol properties to be changed when in **AREA**
      mode in the :ref:`Graph
      Plotting <mgraph_icon>`
      icon

   -  added new parameter **Map Cities Text Blanking** to
      the :ref:`Coastlines <mcoast_icon>`
      icon

   -  added new parameters to draw a frame around the edge of the grid
      in
      the :ref:`Coastlines <mcoast_icon>`
      icon, for selected projections that do not fill the page

   -  added the ability to plot horizontal bar charts via the
      new **Graph** **Bar** **Orientation** parameter in the :ref:`Graph
      Plotting <mgraph_icon>`
      icon

   -  fixed issue where plotting a curve via the :ref:`Table
      Visualiser <table_visualiser_icon>`
      did not work when the output was to file

   -  fixed issue where the Macro code generated by the **Generate
      Macro** function in the Display Window produced incorrect code for
      the Simple Formula icon

   -  the default output file format has been changed from PostScript to
      PDF

   -  the behaviour of :ref:`Text
      Plotting <mtext_icon>`
      icons (mtext() in Macro) has changed slighly - see the `Metview
      FAQ -
      old <https://confluence.ecmwf.int/display/SUPINF/Metview+FAQ+-+old>`__
      for details of this and how to compensate for it

-  **Macro**:

   -  improved handling of netCDF data when the current variable is
      time-based -
      see `NetCDF <https://confluence.ecmwf.int/display/METV/NetCDF>`__.
      **Note that this is a change in behaviour**, and existing macros
      may have to be revised.

   -  improved handling of netCDF data where a computation could lead to
      the overflow of the storage data type -
      see `NetCDF <https://confluence.ecmwf.int/display/METV/NetCDF>`__. **Note
      that this is a change in behaviour**, and existing macros may have
      to be revised.

   -  improved handling of netCDF data where the current variable
      has **scale_factor** and **add_offset** attributes - these are now
      automatically applied -
      see `NetCDF <https://confluence.ecmwf.int/display/METV/NetCDF>`__. **Note
      that this is a change in behaviour**, and existing macros may have
      to be revised.

   -  added a macro library function to draw a circle with a given
      radius in km onto a
      map - `mvl_geocircle <https://confluence.ecmwf.int/display/METV/mvl_geocircle>`__\ ()

   -  fixed problem where
      the :ref:`valid_date() <macro_fieldset_fn>` function
      could give the wrong result given data with a very large step

   -  fixed problem where a Macro operation on a netCDF variable could
      overwrite the original file if it is a symbolic link

   -  change in behaviour: the grib_get_xxx() functions now
      return nil if the given key is not found

   -  change in behaviour: when indexing a vector like this: v[a,a],
      i.e. two indexes the same, the result will be a single-element
      vector; the previous behaviour was to return a number

   -  ensure that an incorrect indexing of a fieldset variable returns
      an error

   -  ensure that an incorrect indexing of a geopoints variable returns
      an error

-  **Vertical Profile**: removed the redundant option **Area 2** from
   **Input Mode**; please use **Area** instead, as it is identical

-  **FLEXTRA**:

   -  the default value for the **FLEXTRA Area** parameter changed in
      the `FLEXTRA Prepare -
      old <https://confluence.ecmwf.int/display/METV/FLEXTRA+Prepare+-+old>`__
      icon. The new default is: -90/-179/90/180.

   -  fixed issue where FLEXTRA did not properly handle global GRIB 2
      fields

   -  it is now possible to specify a relative path for **FLEXTRA Input
      Path** in the FLEXTRA Run icon

   -  a new  :ref:`FLEXTRA
      page <the_flextra_interface>`
      was created in confluence providing an overview about the
      installation, setup and use of the FLEXTRA interface.

   -  the :ref:`FLEXTRA
      tutorial <flextra_tutorial>`
      has been moved to Confluence

-  **Macro Editor**:

   -  revised which actions are available via the toolbar, providing a
      cleaner interface

   -  settings are now saved immediately (font size, show line numbers,
      theme)

-  **GRIB**:

   -  it is now possible, with care, to handle and plot very large GRIB
      fields (e.g. 1km global) - see `Visualising large data files with
      Metview <https://confluence.ecmwf.int/display/METV/Visualising+large+data+files+with+Metview>`__

   -  GRIB Examiner now correctly displays the sections of a GRIB 3 file

-  **Desktop**: 

   -  new icon context menu action called "Delete" (shortcut
      is *Shift+Delete*). With this action the icon is deleted
      permanently (not moved to the wastebasket).

   -  new icon context menu action called "Copy filesystem path" to copy
      an icon's path to the clipboard

   -  selecting **Log** from the menu raises the existing log window if
      it is open

   -  added action in the **Go** menu to navigate to
      the **Defaults** folder

   -  Metview no longer asks for confirmation when closing down, unless
      there are multiple windows

   -  the **Log** window now uses a monospaced font for easier reading
      of aligned text

   -  improved the process of renaming icons from the user interface
      (when we edit the icon name the whole text is automatically
      selected; pressing enter in the text editor or clicking outside
      the icon confirms the renaming)

   -  fixed issue where the **Desktop** could get into a bad state if an
      opened folder is moved, or if Metview is started on a system that
      cannot see a folder that was open when Metview was last closed

-  **Startup**: fixed issue when starting Metview for the first time on
   a system where there is a pre-existing directory called metview

-  **Qt**: Metview now looks for Qt5 by default. To build with Qt4
   (still supported for the time being, please build with
   -DENABLE_QT5=OFF)

-  **Motif**: completely removed the old Motif-based user interface from
   Metview's source code








.. |\_scroll_external/remote/image2017-10-31_14-2-43-373a32fb6f3e25f2f190ff575e49f5888a2e88897c0dfbf0c4e05e3a1845faec.pn.. image:: /_static/release/version_5.0_updates/image8.png
   :width: 3.125in
   :height: 3.34821in
.. |\_scroll_external/remote/image2017-11-9_10-59-5-2bca01d7f920c46d32f33b0282536eba44e8650d0c7c37dd96011b2ac275926e.pn.. image:: /_static/release/version_5.0_updates/image8.png
   :width: 3.125in
   :height: 3.34821in
.. |\_scroll_external/remote/image2017-10-31_15-6-34-a168bd0583f319911f91669e282d633e5da9ac829521c5b6ee599820e6cc98d9.pn.. image:: /_static/release/version_5.0_updates/image8.png
   :width: 3.125in
   :height: 3.34821in


