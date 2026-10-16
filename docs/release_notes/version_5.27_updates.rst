.. _version_5.27_updates:

Version 5.27 Updates
////////////////////

Version 5.27.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2026-10-16
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2026.10.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2026-10-7**

   -  Built
      with **Magics** `4.17.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.50.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.50.0+released>`__

   -  Built with **ODC** version **1.6.3**


**Plotting**

- Metview now supports an additional plotting projection supported by Magics 4.17.0: EPSG:8857, also known as "Equal Earth".

  This can be accessed via the GeoView icon or Python/Macro function, for example:

      .. code-block:: python

         view = mv.geoview(map_projection = "epsg:8857")
         mv.plot(view)


