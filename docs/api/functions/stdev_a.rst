stdev_a
============

.. py:function:: stdev_a(fs,[area])

   Computes the area weighted standard deviation for each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: number or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`.

   .. note::
      
      The computations are implemented via :func:`integrate` and the following lines are equivalent:

      .. code-block:: python

         y = mv.stdev_a(x)
         y = mv.sqrt(mv.integrate(x*x) - mv.integrate(x)**2)

   .. note::

        See also :func:`integrate`, :func:`stdev`, :func:`rms_a` and :func:`var_a`.


.. mv-minigallery:: stdev_a
