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


**Thermo parcel path**

The parcel computations have been revised and several new option were added. 

* :func:`lifted_condensation_level`: improved speed by using [DaviesJones1983]_ instead of an iterative process to compute the :math:`t_{LCL}`. Works now with ndarrays and :class:`Fieldset` as input (previously only numbers were accepted).
* :func:`thermo_parcel_path`: The computations can now use the virtual temperature correction, which is enabled by default. See the ``virtual`` key in the ``options`` argument. Other changes:

  * The Lifted Index (LI) was added to the output
  * The "most_unstable" mode was renamed "mucape". The old name is still supported for backward compatibility but is deprecated.
  * The "mean_layer" mode was renamed "ml". The old name is still supported for backward compatibility but is deprecated.
  * The "ml" start conditions are determined in a new way. Previously simply the mean values of temperature, dewpoint and pressure in the given layer were used. Now, the temperature is determined from the mean potential temperature, the dewpoint is the mean value in the layer and pressure is the surface pressure.
  * The size of the layer in "ml" and "mucape" mode can now be specified via the ``layer_depth`` parameter. With this it is possible to use e.g a 300 hPa wide layer just above the surface in the "mucape" mode without specifying the actual surface pressure:

      .. code-block:: python

         p = mv.thermo_parcel_path{prof, "mode": "mucape", "layer_depth": 300}


**Macro/Python**

* :func:`mvl_ml2hPa`: allowed to specify the target pressure levels as an ndarray
* added new function :func:`static_stability` to compute the static stability 
