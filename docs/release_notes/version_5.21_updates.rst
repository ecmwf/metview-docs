.. _version_5.21_updates:

Version 5.21 Updates
////////////////////


Version 5.21.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2023-xx-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.xx.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2023-xx-xx**

   -  Built
      with **Magics** `4.15.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.33.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.33.0+released>`__

   -  Built with **ODC** version **1.5.0**


**User interface**

- Grib Examiner: added tab showing the details of the ``"pv"`` array when available in the message. The "pv" array contains the definition of the vertical coordinate system of ``hybrid`` model levels used by e.g. the IFS model at ECMWF.  
- Grib Examiner: added tab showing the details of the ``"pl"`` array when available in the message. The "pl" array contains the number of longitudes on a latitude band in various Gaussian grids.
- Grib Examiner: added tab showing the details of the "pl" array when available in the message. The "pl" array contains the number of longitudes on latitude band in various Gaussian grids.


.. **Macro to Python converter**

.. A main new feature in this release is the :ref:`Macro to Python converter <macro_to_python>`. It can be launched from the icon context menu in the :ref:`user interface <mv_desktop_overview>` and from the File menu of the Macro editor. The converter is able to generate fully functional Python code in most of the cases but some code structures have to be adjusted manually. Details about the adjustment process can be found :ref:`here <macro_to_python_adjustments>`.
