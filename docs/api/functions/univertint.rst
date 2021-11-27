univertint
=============


.. py:function:: univertint(fs, [lnsp_code])
.. py:function:: univertint(lnsp, fs, [levels])
   :noindex:

   Performs a vertical integration for pressure levels or ECMWF (hybrid) model levels. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param lnsp: lnsp fieldset defined on model level 1
   :type lnsp: :class:`Fieldset`
   :param lnsp_code: ecCodes paramId for lnsp
   :type lnsp_code: number
   :param levels: level range as a list of [top, bottom]
   :type levels: list
   :rtype: :class:`Fieldset` containing one field only

   :func:`univertint` has to be called in a different way depending on the type of vertical levels in ``fs``.

   * Pressure levels: the function has to be called with the ``fs`` argument only.
   * Model levels: 

      * when no ``lnsp`` is specified ``fs`` must also contain an lnsp field. In this case the optional ``lnsp_code`` can specify the ecCodes **paramId** used to identify the **lnsp** field (by default the value of 152 is used.
      * when ``lnsp`` is specified it defines the **lnsp** field.
      * the optional ``levels`` parameter is a **list** with two numbers [top, bottom] to specify the level range for the integration. If ``levels`` is not specified the vertical integration is performed for all the model levels in ``fs``.
         
   A missing value in any field will result in a missing value in the corresponding place in the output fieldset.


Computations
++++++++++++++++

   The computations are based on the following formula:

   .. math::
      
      \int_{p_{top}}^{p_{bottom}} f \frac{dp}{g}

   where:

   * f: input fieldset
   * p: pressure
   * g: acceleration of gravity (9.80665 m/s2).

   The actual algorithm is slightly different on pressure and model levels.

   For **pressure levels** the data is first sorted by pressure in ascending numerical order resulting in :math:`f_{i}` fields on levels :math:`p_{i}` i=0,...,N (with :math:`p_{i+1} > p_{i}`). Then, to estimate the pressure differential we form N layers by using the pressures halfway between two levels. If we denote the halfway pressure between level i and i+1 by :math:`p^{*}_{i}` we can write the layer sizes as follows:

   .. math::

      \Delta p_{0} = p^{*}_{0} - p_{0}

      \Delta p_{i} = p{*}_{i+1} - p^{*}_{i}  

      \Delta p_{N} = p_{N} - p^{*}_{N-1}

   and estimate the integral like this:

   .. math::
      
      \sum_{i=0}^{N} f_{i} \frac{\Delta p_{i}}{g}
   
   For **model level** data the vertical coordinate system definition is stored in the **"pv" array** in the GRIB header. A model level is defined on a "full level", which lies in the layer between the two neighbouring "half levels". Using ``lnsp`` and the "pv" array we can determine the  :math:`\Delta p_{i}` layer size for each level individually. The integral is then estimated in the same way as was shown above for pressure levels. Please note that you can use :func:`unithickness` to compute the layer sizes (the "thickness" in the function name actually means "layer size"). For more details about the model level definitions please visit this `page <https://confluence.ecmwf.int/display/UDOC/Model+level+definitions>`_.


   :Example: 

      .. code-block:: python

         import metview as mv

         # Retrieve cloud liquid water content 
         clwc = mv.retrieve(
            levtype : "ml",
            levelist : [1,"to",137],
            param : "clwc",
            date : -1,
            grid : [2,2]
         )

         # Retrieve lnsp
         lnsp = mv.retrieve(
            levtype : "ml",
            levelist : 1,
            param : "lnsp",
            date : -1,
            grid : [2,2]
         )

         # Compute total amount of liquid water
         r = mv.univertint(lnsp,clwc)


.. mv-minigallery:: univertint
