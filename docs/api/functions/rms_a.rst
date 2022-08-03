rms_a
==============

.. py:function:: rms_a(fs, [area])
 
   Computes the area weighted root mean square for each field in  ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the computations
   :rtype: number or list 
   
   If the ``area`` is not specified the whole field will be used in the calculation. The result is a number for a single field or a list for a multi-field :class:`Fieldset`. 
 
   .. note::
      
      The computations are implemented via :func:`integrate` and the following lines are equivalent:

      .. code-block:: python

         y = mv.rms_a(x)
         y = mv.sqrt(mv.integrate(x*x))

   .. note::

        See also :func:`integrate`, :func:`rms`, :func:`var_a` and :func:`stdev_a`.


.. mv-minigallery:: rms_a