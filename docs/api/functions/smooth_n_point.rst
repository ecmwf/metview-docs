smooth_n_point
================

.. py:function:: smooth_n_point(fs, n=9, repeat=1, **kwargs)

   *New in metview-python version 1.13.0*.

   Performs spatial smoothing using a 5 or 9 point technique for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param n: specifies the type of smoothing (n=5 or n=9)
   :type n: number
   :param repeat: specifies how many times the smoothing should be applied to ``fs``
   :type repeat: number
   :param **kwargs: these arguments are directly passed to :py:func:`scipy.ndimage.convolve` (see below)
   :rtype: :class:`Fieldset`  
   
   The computations are performed as a 2D convolution by calling :py:func:`scipy.ndimage.convolve` and the extra ``**kwargs`` are directly passed to this function. The convolution matrices (``weights`` in the :py:func:`scipy.ndimage.convolve` terminology) are defined as follows:

   * with n=5:
   
      .. math::

         \frac{1}{8} \begin{bmatrix}0 & 1 & 0\\1 & 4 & 1\\0 & 1 &0\end{bmatrix}

   * with n=9:

      .. math::
   
         \frac{1}{16} \begin{bmatrix}1 & 2 & 1\\2 & 4 & 2\\1 & 2 &1\end{bmatrix}

   .. warning::
   
      :func:`smooth_n_points` has some limitations:

       * it only works for regular latitude-longitude grids
       * for global grids in longitudinal (East-West) direction the resulting field is not smoothed properly along the periodic border

   .. note::
      
      See also :func:`smooth_gaussian`, :func:`convolve` and :func:`q_vector`.


.. mv-minigallery:: smooth_n_point
