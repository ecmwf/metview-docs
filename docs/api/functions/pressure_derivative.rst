pressure_derivative
=========================

.. py:function:: pressure_derivative(f, [p])

   Computes the vertical pressure derivative.
   
   :param f: input data defined on a given set of pressure values
   :type f: list, ndarray, :class:`Fieldset`
   :param p: pressure (Pa)
   :type p: number, ndarray or :class:`Fieldset`
   :rtype: same type as ``f`` or None

   The result is the vertical pressure derivative in */Pa units. The following rules are applied when ``f`` is a :class:`Fieldset`:

   * if ``f`` is a pressure level :class:`Fieldset` no ``p`` is needed
   * if ``f`` is defined on ECMWF model levels (hybrid/eta) ``p`` must be either a single LNSP (logarithm of surface pressure, identified by paramId=152) field or a :class:`Fieldset` defining the pressure on the same levels as ``f`` (see :func:`pressure`)
   * for other level types ``p`` must be a :class:`Fieldset` defining the pressure on the same levels as ``f``.

   In the computations, first the values are sorted by pressure, then a non-uniform central difference scheme (one-sided difference at the bottom and top) is used to estimate the derivatives. The results are then re-sorted to appear in the same order as in ``f``. This allows for the following type of computations:

   .. code-block:: python

        import metview as mv
         
        # read fields defined on the same set of, potentially unsorted,
        # pressure levels. I.e. the fields in f1 and f2 are properly lined
        # up in terms of pressure. 
        f1 = mv.read("data1.grib")
        f2 = mv.read("data2.grib")
        
        # the fields are still lined up for computing r since
        # pressure_derivative() keeps the original field ordering
        r = f2 * mv.pressure_derivative(f1)


.. mv-minigallery:: pressure_derivative
