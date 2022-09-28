convolve
================

.. py:function:: convolve(fs, weights, repeat=1, **kwargs)

   *New in metview-python version 1.13.0*.
   
   Performs spatial convolution with the given kernel for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param weights: specifies the kernel as a matrix (2D array)
   :type weights: 2D ndarray
   :param repeat: specifies how many times the smoothing should be applied to ``fs``
   :type repeat: number
   :param **kwargs: these keyword arguments are directly passed to :py:func:`scipy.ndimage.convolve` (see below)
   :rtype: :class:`Fieldset`  
   
   The computations are performed by calling :py:func:`scipy.ndimage.convolve` and the extra ``**kwargs`` are directly passed to this function. 

   .. warning::
   
      :func:`convolve` has some limitations:

       * it only works for regular latitude-longitude grids
       * for global grids in longitudinal (East-West) direction the resulting field is not smoothed properly along the periodic border

   .. note::
      
      See also :func:`smooth_n_point` and :func:`smooth_gaussian`.


.. mv-minigallery:: convolve
