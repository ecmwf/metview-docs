.. _version_5.23_updates:

Version 5.26 Updates
////////////////////

Version 5.26.1
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2025-10-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2025.10.1.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2025-10-14**

   -  Built
      with **Magics** `4.16.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.44.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.42.0+released>`__

   -  Built with **ODC** version **1.6.0**


**Fixes**

- :func:`read`: fixed issue where it was not possible to filter individual ensemble members from GRIB

Version 5.26.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2025-10-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2025.10.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2025-10-07**

   -  Built
      with **Magics** `4.16.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.44.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.44.0+released>`__

   -  Built with **ODC** version **1.6.0**


**MARS Client**

- Metview's MARS client, when installed at ECMWF, now simply invokes the command-line based
  Mars client instead of using its own built-in one. This is in order to be able to take advantage
  of the recent configuration advances in the command-line MARS client, which is adopting a flexible,
  dynamic system of migrating to the new C++ based client. Note that this change applies to both MARS
  retrievals and GRIB filtering - Macro/Python commands :func:`retrieve` and :func:`read`
  are affected.

  By default, the command-line invoked will be `mars <request>`. However, it is possible to modify
  this by setting the environment variable `METVIEW_MARS_COMMAND`. An example of this would be:

      .. code-block:: bash

         export METVIEW_MARS_COMMAND="/usr/local/mars -p"


**Fixes**  

- The tests now download their data from sites.ecmwf.int instead of get.ecmwf.int.

