mvl_ml2hPa
=============

.. py:function:: mvl_ml2hPa(lnsp, fs, pressures)

   Interpolates ``fs`` from ECMWF model levels onto a set of pressure levels defined by ``pressures``. 
   
   :param lnsp: logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param fs: fieldset to be interpolated (must contain model levels!). Does not have to be sorted by level.
   :type fs: :class:`Fieldset`
   :param pressures: target pressure levels in hPa. Does not have to be sorted. Note: it can be an ndarray only since *Metview version 5.17.0*.
   :type pressures: list or ndarray
   :rtype: :class:`Fieldset`
  
   The input data (``fs``) must contain one field per model level only. It means that e.g. data containing multiple timesteps cannot be used as an input.
   
   At gridpoints where the interpolation is not possible a missing value is returned. It happens where the target pressure is larger than the pressure on the bottom-most model level or less than the pressure at the top-most model level in ``fs``. 
    
   .. note::
      The actual ECMWF model level definition is stored in the **"pv" array** in the GRIB message metadata. You can figure out the total number of model levels in the given vertical coordinate system by using the **len(pv)/2-1** formula. The typical values are 137 and 91. This can be then used to look up details about actual the model level definitions (e.g. approximate pressure and height values) on this `page <https://confluence.ecmwf.int/display/UDOC/Model+level+definitions>`_.  

   :Example:
   
      This code illustrates how to use :func:`mvl_ml2hPa` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv

         # retrieve the data on model levels
         ret_core = {"type": "fc", "levtype": "ml", "step": 12, "grid": [1.5,1.5]}
         t_ml = mv.retrieve(**ret_core, param="t", levelist=[1, "to", 137])
         lnsp = mv.retrieve(**ret_core, param="lnsp", levelist=1)

         # interpolate onto a list of pressure levels
         p_levels = [1000, 900, 850, 500, 300, 100, 10, 1, 0.1]
         t_pres = mv.mvl_ml2hPa(lnsp, t_ml, p_levels)


.. mv-minigallery:: mvl_ml2hPa
