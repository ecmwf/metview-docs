.. _version_5.23_updates:

Version 5.25 Updates
////////////////////

Version 5.25.1
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2025-06-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2025.06.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2025-06-xx**

   -  Built
      with **Magics** `4.16.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.42.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.42.0+released>`__

   -  Built with **ODC** version **1.6.0**


**Fixes**

- STVL: allow the use of a list in the `sources` parameter
- Fixed issue when configuring with CMake version 4.0
- Reverted change in results in regridding U/V data to align with results from current ECMWF production systems

Version 5.25.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2025-04-10
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2024.09.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2025-04-10**

   -  Built
      with **Magics** `4.16.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.41.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.41.0+released>`__

   -  Built with **ODC** version **1.6.0**


**BUFR Examiner**

- The BUFR Examiner now has a context menu option to save the selected message to a file.

   .. image:: /_static/ui/bufr_examiner_save_message.png
      :width: 250px


- The BUFR Examiner now has a new tab displaying a 'flat dump' of the tree.

   .. image:: /_static/ui/bufr_examiner_flat_dump.png
      :width: 250px

**Fixes**  

- Fixed issue when building Metview with GNU 14 compilers

