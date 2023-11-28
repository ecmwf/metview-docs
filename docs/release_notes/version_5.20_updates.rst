.. _version_5.20_updates:

Version 5.20 Updates
////////////////////

Version 5.20.0
==============

* Externally `released <https://confluence.ecmwf.int//display/METV/Releases>`__\  on 2023-10-04
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.10.0.0 (Atos HPC)

-  **At ECMWF:**

   -  Installed **2023-10-03**

   -  Built
      with **Magics** `4.14.2 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.32.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.32.0+released>`__

   -  Built with **ODC** version **1.4.6**


**HEALPix support**

- with the latest versions of ecCodes, MIR and Atlas, Metview now supports the HEALPix grid, including:

  + conversion to Geopoints (:func:`grib_to_geo`)
  + regridding from HEALPix to other grids (:func:`regrid`)
  + extraction of latitudes and longitudes (:func:`latitudes`, :func:`longitudes`)
  + :func:`nearest_gridpoint`

In order to plot a GRIB file with data in HEALPix grid, it is suggested to convert to Geopoints, and plot the result with Symbol Plotting (:func:`msymb`).


**Fixes:**

- :func:`regrid`: fixed issue when regridding wind components (e.g. U/V) to a regular lat/lon grid; the values at the poles now vary as if in a ring, in conformance with the WMO standard
- :func:`regrid`: fixed performance issue when processing ORCA grids from GRIB
- :func:`nearest_gridpoint`: fixed issue when the input is one of: Lambert Azimuthal Equal Area, Mercator, HEALPix
- :func:`flextra_run`: fixed issue where it could pick up the definition files of a different ecCodes from the one that FLEXTRA was built with
