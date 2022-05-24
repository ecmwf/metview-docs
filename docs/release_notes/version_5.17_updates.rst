.. _version_5.17_updates:

Version 5.17 Updates
////////////////////


Version 5.17.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-xx-xx
* Became metview/new at ECMWF on 2022-xx-xx (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-xx-xx**

   -  Built
      with **Magics** `4.12.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.26.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.26.0+released>`__

   -  Built with **ODC** version **1.4.5**

   -  Includes
      version `1.12.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface

  
* :func:`lifted_condensation_level`: improved speed by using [DaviesJones1983]_ instead of an iterative process to compute the :math:`t_{LCL}`. Works now with ndarrays and :class:`Fieldset` as input (previously only numbers were accepted).