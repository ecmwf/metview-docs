smooth_gaussian
================

.. py:function:: smooth_gaussian(fs, sigma=1, repeat=1, **kwargs)

   *New in metview-python version 1.13.0*.

   Performs spatial smoothing using a Gaussian filter for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param sigma: standard deviation for Gaussian kernel
   :type sigma: number
   :param repeat: specifies how many times the smoothing should be applied to ``fs``
   :type repeat: number
   :param **kwargs: these arguments are directly passed to :py:func:`scipy.ndimage.gaussian_filter` (see below)
   :rtype: :class:`Fieldset`  
   
   The computations are performed by calling :py:func:`scipy.ndimage.gaussian_filter` and the extra ``**kwargs`` are directly passed to this function. 

   .. warning::
   
      :func:`smooth_gaussian` has some limitations:

       * it only works for regular latitude-longitude grids
       * for global grids in longitudinal (East-West) direction the resulting field is not smoothed properly along the periodic border

   
   .. note::
      
      See also :func:`smooth_n_point`, :func:`convolve` and :func:`q_vector`.


.. mv-minigallery:: smooth_gaussian
