.. _version_5.15_updates:

Version 5.15 Updates
////////////////////


Version 5.15.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-03-03
* Became metview/new at ECMWF on 2022-03-03 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-03-03**

   -  Built
      with **Magics** `4.11.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.25.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.25.0+released>`__

   -  Built with **ODC** version **1.4.4**

   -  Includes
      version `1.11.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface


**Weather Symbol Objects**

There were several improvements for the :ref:`Weather Symbol Objects <weather_symbols>`.

* Each Weather Symbol Object is now represented by a **Metview icon** (see the full 
  list of icons :ref:`here <toc_plot_ws>`). These icons can be directly visualised or dragged into the plot window. Plotting from a script (Python or Macro) is possible with some restrictions as described :ref:`here <ws_plotting>`.
  
  .. image:: /_static/release/version_5.15_updates/ws_editor.png
      :width: 250px
      
* Using the icons the symbols :ref:`can be saved <ws_saving_and_loading>` from the Metview plot window for later reuse. To help the Weather Symbol management the :ref:`User Library <ws_user_library>` sidebar was added to the plot window:

  .. image:: /_static/ug/ws_saving_and_loading/user_library_sidebar.png
    :width: 210px

* The whole scene of Weather Symbols (i.e. all the Weather Symbols in a plot view) can be saved as a :ref:`collection <ws_saving_collection>`. 
* The way to add user defined images was refined and improved (see :ref:`here <ws_add_your_symbol>`).
* The **geolocked** parameter was added to all the symbols to prevent accidental move when on screen editing.
* The **tooltip** parameter was added to all the symbols to display a tooltip when the object is hovered over on screen.

  .. image:: /_static/release/version_5.15_updates/ws_tooltip.png
      :width: 210px


**Macro/Python**

- :func:`create_geo` now supports a list containing numpy.nan values as input

- :doc:`Geopoints </data_types/geopoints>` now supports missing values in the elevations column

- fixed failure when extracting a subset of a float32 vector in Macro when
  the default type is float64 - and vice-versa

- fixed issue where extracting latitudes and longitudes of a GRIB on a reduced
  Gaussian grid sub-area caused a crash

- fixed issue where calling the WmsClient in a batch script caused
  a failure due to a bad _PATH parameter


**Plotting**

- added new paramteter `map_user_layer_land_colour` to :func:`mcoast` to enable and control the shading of user-supplied shapefiles as part of the coastlines

  .. image:: /_static/release/version_5.15_updates/user_land_shade.png
      :width: 400px

- added EPSG:32661 and EPSG:32761 to list of available projections

- updated list of built-in areas to match the latest defined in Magics


**Regrid**

- added :doc:`Geopoints </data_types/geopoints>` as possible input data type
- added TARGET parameter in order to directly specify where the output file should go
- added new interpolation methods DETAILS REQUIRED


**Meteogram**

- The :func:`meteogram` module now uses the new infrastructure to retrieve its plots


**Display Window**

- fixed issue where a long filename in a GRIB (or other data) file could
  cause problems when resizing the sidebar in the Display Window
- fixed issue where the sidebar in the Display Window took up too much space on first startup
- fixed issue where the Display Window could crash if loading a key profile
  containing unsupported key names

**GRIB and BUFR Examiners**

- GRIB Examiner now displays both the native value and the string value in the namespace dumps
- the BUFR Examiner now displays "missing" for missing string values
- the BUFR Examiner now uses the first two columns for searching in the Descriptors tab
- fixed issue where the GRIB Examiner message list did not update correctly when the key profile is changed

**Desktop UI**

- fixed an issue where the Desktop main user interface could crash if a user deleted a non-empty folder
