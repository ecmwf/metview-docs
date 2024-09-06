pl_to_hl
============

.. py:function:: pl_to_hl(fs, z, zs, h, ref_level, method)

   *New in Metview version 5.23.0*

   Interpolate ``fs`` on pressure levels onto height levels (in m) above sea or ground level. 
   
   :param fs: fieldset to be interpolated. There is no restriction on the order or range of pressure levels in ``fs``.
   :type fs: :class:`Fieldset`
   :param z: geopotential fieldset on pressure levels (it must contain the same levels as ``fs`` but their order can be different) 
   :type z: :class:`Fieldset`
   :param zs: surface geopotential field (if ``ref_level`` is set to "sea" it should be set to None).
   :type zs: :class:`Fieldset` or None
   :param h: list of target height levels in **metres** above/below the ``ref_level`` (they can came in any given order)
   :type h: list or :class:`Fieldset`
   :param str ref_level: specify the reference level for the target heights. The possible values are "sea" and "ground". If it is "ground" a valid ``zs`` must be provided.
   :param str method: specify the interpolation method. The possible values are "linear" and "log". For target height levels very close to 0 always a "linear" interpolation is used.
   :rtype: :class:`Fieldset`
      
   The input data (``fs``) must contain one field per pressure level only. It means that e.g. data containing multiple timesteps cannot be used as an input.

   At gridpoints where the interpolation is not possible a missing value is returned. It happens where the target height level is below the bottom-most pressure level in ``fs``. It also happens where the target height is above the top-most pressure level in ``fs``.

   .. note::
       See also :func:`mvl_ml2hPa`, :func:`pl_to_hl`.

   :Example:
   
      This code illustrates how to use :func:`pl_to_hl` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv 

         # retrieve the data on model levels - surface geopotential (zs)
         # is taken from the analyis on level 1!
         ret_core = {
            "levtype": "pl", "date": 20191023, "time": 12 "grid": [2,2]}

         fs_pl = mv.retrieve(**ret_core, 
                  type="fc",
                  levelist=[1000,925,850,700,500,300,250,200,150,100],
                  step=12,
                  param=["t", "z"])

         t = mv.read(data=fs_ml, param="t")
         z = mv.read(data=fs_ml, param="z")
         
         zs = mv.retrieve(**ret_core,
               type="an",
               levelist="sfc",
               param="z")

         # interpolate the t field onto a list of height levels above sea level
         hlevs = [1000, 2000, 3000, 4000, 5000]
         th_sea = mv.pl_to_hl (t, z, None, hlevs, "sea", "linear")


         # interpolate the t field onto another list of height levels above ground
         hlevs = [100, 200, 300, 400, 500]
         th_ground = mv.pl_to_hl (t, z, zs, hlevs, "ground", "linear")

.. mv-minigallery:: pl_to_hl