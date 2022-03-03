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


**Weather Symbols**

- DETAILS REQUIRED


**Macro/Python**

- :func:`create_geo` now supports a list containing numpy.nan values as input

- Geopoints now supports missing values in the elevations column

- fixed failure when extracting a subset of a float32 vector in Macro when
  the default type is float64 - and vice-versa

- fixed issue where extracting latitudes and longitudes of a GRIB on a reduced
  Gaussian grid sub-area caused a crash

- fixed issue where calling the WmsClient in a batch script caused
  a failure due to a bad _PATH parameter


**Plotting**

- added new paramteter to :func:`mcoast` to enable and control the shading of user-supplied shapefiles as part of the coastlines

- added EPSG:32661 and EPSG:32761 to list of available projections

- updated list of built-in areas to match the latest defined in Magics


**Regrid**

- added Geopoints as possible input data type
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
