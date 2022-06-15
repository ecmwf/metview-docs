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
* :func:`thermo_parcel_path`: 
  
  * ``options`` became a keyword argument (previously it was a positional one)
  * The computations can now use the **virtual temperature correction**, which is enabled by default. See the ``virtual`` key in the ``options`` argument.
  * The Lifted Index (LI) was added to the output
  * The "most_unstable" mode was renamed "mucape". The old name is still supported for backwards compatibility but is deprecated.
  * The "mean_layer" mode was renamed "ml". The old name is still supported for backwards compatibility but is deprecated.
  * The "ml" start conditions are determined in a new way. Previously simply the mean values of temperature, dewpoint and pressure in the given layer were used. Now, the temperature is determined from the mean potential temperature, the dewpoint is the mean value in the layer and pressure is the surface pressure.
  * The new start options were added: "m50" and "ml100". They are the variants of the "ml" mode with a fixed 50 hPa and 100 hPa bottom layer, respectively.
  * The size of the layer in "ml" and "mucape" mode can now be specified via the ``layer_depth`` parameter. 
  * The default start conditions were changed to 

      .. code-block:: python

        options={"mode": "mucape", "layer_depth": 300}

  * Added new keys ``compute_top`` and ``el_area`` to ``options`` to control the  computations and data extraction above the Equilibrium Level (EL)
   
      


**Hovmoller**

* Line Hovmoeller: fixed issue when North and South coordinates of lines going from SW to NE were automatically swapped
  

**Macro/Python**

* :func:`mvl_ml2hPa`: allowed to specify the target pressure levels as an ndarray
* added new function :func:`static_stability` to compute the static stability 

