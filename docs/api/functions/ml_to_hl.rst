ml_to_hl
============

.. py:function:: ml_to_hl(fs, z, zs, h, ref_level="sea", method="linear", fs_surf=None, height="geometric")

   Interpolate ``fs`` on model levels (i.e. on hybrid or eta levels used by the IFS) onto height levels (in m) above sea or ground level. 
   
   :param fs: fieldset to be interpolated. There is no restriction on the order or range of model levels in ``fs``.
   :type fs: :class:`Fieldset`
   :param z: geopotential fieldset on model levels (it must contain the same levels as ``fs`` but their order can be different) 
   :type z: :class:`Fieldset`
   :param zs: surface geopotential field (if ``ref_level`` is set to "sea" it should be set to None).
   :type zs: :class:`Fieldset` or None
   :param h: list of target height levels in **metres** above the ``ref_level`` (they can came in any given order). Values must be non-negative.
   :type h: list or :class:`Fieldset`
   :param str ref_level: specify the reference level for the target heights. The possible values are "sea" and "ground". If it is "ground" a valid ``zs`` must be provided.
   :param str method: specify the interpolation method. The possible values are "linear" and "log". For target height levels very close to 0 always a "linear" interpolation is used.
   :param fs_surf: specify the field values on the surface. With this it is possible to interpolate to target heights between the surface and the bottom-most model level. If ``fs_surf`` is a number it defines a constant :class:`Fieldset`. Only available when ``ref_level`` is "ground". *New in Metview version 5.14.0*.
   :type fs_surf: number or :class:`Fieldset`
   :param height: specify the height computation method. The possible values are as follows:

      - "geometric": the height is the geometric height and computed from the geopotential with :func:`height_from_geopotential`. This is the **default**.
      - "geopotential": the height is the geopotential height 
      *New in Metview version 5.23.0*. In earlier versions the geopotential height was used in the computations.
   :type height: str

   :rtype: :class:`Fieldset`
      
   The input data (``fs``) must contain one field per model level only. It means that e.g. data containing multiple timesteps cannot be used as an input.

   At gridpoints where the interpolation is not possible a missing value is returned. It happens where the target height level is below the bottom-most model level in ``fs`` or the surface when ``fs_surf`` is used. It also happens where the target height is above the top-most model level in ``fs``. Please note that the model levels we are dealing with in :func:`ml_to_hl` are "full-levels" and the lowest possible model level does match the surface but it is above it. If you need to interpolate to height levels close to the surface use ``fs_surf``. 

   .. note::
      The actual ECMWF model level definition is stored in the **"pv" array** in the GRIB message metadata. You can figure out the total number of model levels in the given vertical coordinate system by using the **len(pv)/2-1** formula. The typical values are 137 and 91. This can be then used to look up details about actual the model level definitions (e.g. approximate pressure and height values) on this `page <https://confluence.ecmwf.int/display/UDOC/Model+level+definitions>`_.  

   .. note::
      Geopotential is not archived operationally on model levels in MARS at ECMWF. You can compute it with :func:`mvl_geopotential_on_ml`. 
      
   .. warning::
      From *Metview version 5.23.0* the geometric height is used in the computations **by default**. In the previous versions the geopotential height was used. Use ``height="geopotential"`` to revert to the old behaviour. ``height`` is a new parameter introduced in *Metview version 5.23.0*.

   :Example:
   
      This code illustrates how to use :func:`ml_to_hl` together with :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv 

         # retrieve the data on model levels - surface geopotential (zs)
         # is taken from the analyis on level 1!
         ret_core = {
            "levtype": "ml", "date": 20191023, "time": 12 "grid": [2,2]}

         fs_ml = mv.retrieve(**ret_core, 
                  type="fc",
                  levelist=[1,"TO",137],
                  step=12,
                  param=["t", "q", "lnsp"])

         t = mv.read(data=fs_ml, param="t")
         q = mv.read(data=fs_ml, param="q")
         lnsp = mv.read(data=fs_ml, param="lnsp")

         zs = mv.retrieve(**ret_core,
               type="an",
               levelist=1,
               param="z")

         # compute geopotential on model levels
         z = mv.mvl_geopotential_on_ml(t, q, lnsp, zs)

         # interpolate the t field onto a list of height levels above sea level
         hlevs = [1000, 2000, 3000, 4000, 5000]
         th_sea = mv.ml_to_hl (t, z, None, hlevs, "sea", "linear")


         # interpolate the t field onto another list of height levels above ground
         hlevs = [100, 200, 300, 400, 500]
         th_ground = mv.ml_to_hl (t, z, zs, hlevs, "ground", "linear")

.. mv-minigallery:: ml_to_hl