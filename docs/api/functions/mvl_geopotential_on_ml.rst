mvl_geopotential_on_ml
=========================

.. py:function:: mvl_geopotential_on_ml(t, q, lnsp, zs)

   Computes geopotential on model levels.

   :param t: temperature fields on model levels. For the required levels and their ordering please see details below.
   :type t: :class:`Fieldset`
   :param q: the specific humidity fields. on model levels. For the required levels and their ordering please see details below.
   :type q: :class:`Fieldset`
   :param lnsp: logarithm of surface pressure field (model level 1!).
   :type lnsp: :class:`Fieldset`
   :param zs: surface geopotential field (model level 1!)
   :type zs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   All fields must be **gridpoint** data - no spherical harmonics, and they must all be on the same grid, with the same number of points. :func:`mvl_geopotential_on_ml` assumes that there are no other dimensions contained in the data, e.g. all fields should have the same date and time. 
   
   The return value is a :class:`Fieldset` of geopotential defined on the model levels present in the input data sorted by ascending numeric level order.

   The computations are described on page 7-8 in [IFS-Dynamics]_ and based on the following hydrostatic formula:

    .. math::
      
      z_{ml} = - \int_{p_{surf}}^{p_{ml}} \frac{R_{d} T_{v}}{p} dp

   where:

   * :math:`R_{d}`` is the specific gas constant for dry air (287.058 J/(kg K))
   * :math:`T_{v}` is the virtual temperature (K)
   * p is the pressure

   The required levels and their ordering in ``t`` and ``q`` depend on the Metview version used:
   
   * from Metview version **5.14.0**: ``t`` and ``q`` must contain the same levels in the same order but there is no restriction on the actual level ordering. The model level range must be contiguous and must include the bottom-most level, but **not all the levels must be present**. E.g. if the current vertical coordinate system has 137 model levels using only a subset of levels between e.g. 137-96 is allowed.
   * in **previous** Metview versions: ``t`` and ``q`` must contain the full model level range in ascending numeric order. E.g. if the current vertical coordinate system has 137 model levels ``t`` and ``q`` must contain all the levels ordered as 1,..., 137.

   .. note::
      The actual ECMWF model level definition is stored in the **"pv" array** in the GRIB message metadata. You can figure out the total number of model levels in the given vertical coordinate system by using the **len(pv)/2-1** formula. The typical values are 137 and 91. This can then be used to look up details about actual the model level definitions (e.g. approximate pressure and height values) on this `page <https://confluence.ecmwf.int/display/UDOC/Model+level+definitions>`_.  

   .. note::
      **Surface geopotential** is defined on model level 1 in MARS at ECMWF. For most recent dates it is available for the 0 forecast step. However, generally it is only available as an **analysis** field.  
      
   .. note::
      See also :func:`ml_to_hl`. 

   :Example:
   
      This code illustrates how to use :func:`mvl_geopotential_on_ml` with data retrieved from MARS:

      .. code-block:: python

         import metview as mv
         
         # retrieve the data on model levels - surface geopotential (zs) is
         # only available in the analyis on level 1!
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

.. mv-minigallery:: mvl_geopotential_on_ml
