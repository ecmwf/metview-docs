.. _version_4.9_updates:

Version 4.9 Updates
///////////////////

2 Version 4.9.0 `4 <#version-4.9.0>`__

Version 4.9.1 
=============

Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-10-10

-  **Tarball:** fixed issue that prevented the 4.9.0 tarball from
   building

Version 4.9.0 
=============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__ on 2017-10-03
* Became metview/new at ECMWF on 2017-10-03 (Linux desktops, ecgate, lxc, lxg, lxop)

-  **At ECMWF:**

   -  Installed **2017-10-03**
   -  Built with
      **Magics** `2.34.3 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__
   -  Built with
      **ecCodes** `2.5.0 <https://software.ecmwf.int/wiki/display/ECC/ecCodes+version+2.5.0+released>`__
   -  Built with **ODB_API** version **0.17.3**
   -  Built with **emoslib** `000452 <https://confluence.ecmwf.int/display/EMOS/Changes+in+version+000452>`__

-  **Hovmoeller**: added new parameter to the `Hovmoeller
   View <https://software.ecmwf.int/wiki/display/METV/Hovmoeller+View>`__
   icon: **Time Axis Mode**, which can be **Automatic Forwards**,
   **Automatic Backwards** or **User**.

-  **Cross Section**: added the ability to define a cross section line
   that goes directly over a pole. As an example, to define a line that
   goes South from lat=0, lon=-8 over the South pole and round to lat=0,
   lon=172, supply a line definition like this:  [0, -8, -180, -8] 
   (N,W,S,E). They key points in telling Metview to use a line that goes
   over a pole are that the longitude remains the same and that the
   second latitude is described as either greater than 90 or less than
   -90. The direction of the line is implicit: here, to go from 0 to
   "-180" involves travelling South.

-  **Text Plotting**: added new parameter to the `Text
   Plotting <https://software.ecmwf.int/wiki/display/METV/Text+Plotting>`__
   icon: **Text Orientation**, which can take the values **Horizontal**
   (default), **Top Bottom** and **Bottom Top**.

-  **Stations**: use the latest WMO stations database

-  **Stations**: improved the way that station names are matched in the
   station lookup widget in the Stations editor

-  **Macro**: new Macro function called :func:`percentile` was added to compute percentiles from a list of
   vectors
