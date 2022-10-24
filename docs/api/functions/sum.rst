sum
======

.. py:function:: sum(fs, missing=False, dim=None, preserve_dims=None)

   Computes the point-wise sum of the values in ``fs``. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param missing: controls what happens when missing values are present in ``fs``. When it is ``False``, a missing value in any of the fields at a given gridpoint will result in a missing value in the corresponding gridpoint in the output. If it is ``True`` all the non-missing values across the fields at a given grid point will be used to compute the sum. *This parameter is new in Metview version 5.16.0*. In earlier versions the computations are carried out as if ``missing`` was set to ``False``.
   :type missing: bool
   :param dim: restrict the computations to a single dimension of the data - see main text below.  *New in metview-python version 1.13.0*.
   :type dim: str
   :param preserve_dims: may be used in conjunction with parameter ``dim`` - see main text below.  *New in metview-python version 1.13.0*.
   :type preserve_dims: list
   :rtype: :class:`Fieldset`

   The output is a :class:`Fieldset` with one field only. 
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`x_{i}^{k}` the output values can be written as:

   .. math:: 
      
         s_{i} = \sum_{k}^{N} x_{i}^{k}

   To understand how to perform computations over a single 'dimension' of the data, see the
   documentation for the :func:`mean` function.

   .. note::
      
      See also :func:`mean`.


.. py:function:: sum(gpt)

    Computes the sum of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: number
    
    Missing values are bypassed in this calculation. If there are no valid values None is returned.

.. mv-minigallery:: sum
