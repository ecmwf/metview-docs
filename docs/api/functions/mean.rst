mean
==========

.. py:function:: mean(fs, missing=False)

   Computes the point-wise mean of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param missing: controls what happens when missing values are present in ``fs``. When it is ``False``, a missing value in any of the fields at a given gridpoint will result in a missing value in the corresponding gridpoint in the output. If it is ``True`` all the non-missing values across the fields at a given grid point will be used to compute the mean. *This parameter is new in Metview version 5.16.0*. In earlier versions the computations are carried out as if ``missing`` were set to ``False``.
   :type missing: bool
   :rtype: :class:`Fieldset`
   
   The result is a :class:`Fieldset` with a single field in each gridpoint containing the mean of all the values belonging to the same gridpoint throughout the fields in ``fs``
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`f_{i}^{k}` the output values can be written as:

   .. math::

         m_{i} = \frac {1}{N} \sum_{k}^{N}f_{i}^{k}


.. py:function:: mean(gpt)
    :noindex:

    Computes the mean of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: number or None
    
    Missing values are bypassed in this calculation. If there are no valid values, then None is returned.

.. mv-minigallery:: mean