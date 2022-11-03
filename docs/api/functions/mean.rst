mean
==========

.. py:function:: mean(fs, missing=False, dim=None, preserve_dims=None)

   Computes the point-wise mean of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param missing: controls what happens when missing values are present in ``fs``. When it is ``False``, a missing value in any of the fields at a given gridpoint will result in a missing value in the corresponding gridpoint in the output. If it is ``True`` all the non-missing values across the fields at a given grid point will be used to compute the mean. *This parameter is new in Metview version 5.16.0*. In earlier versions the computations are carried out as if ``missing`` were set to ``False``.
   :type missing: bool
   :param dim: restrict the computations to a single dimension of the data - see main text below. *New in metview-python version 1.13.0*.
   :type dim: str
   :param preserve_dims: may be used in conjunction with parameter ``dim`` - see main text below. *New in metview-python version 1.13.0*.
   :type preserve_dims: list
   :rtype: :class:`Fieldset`
   
   The result is a :class:`Fieldset` with a single field in each gridpoint containing the mean of all the values belonging to the same gridpoint throughout the fields in ``fs``
   
   With N fields in ``fs`` by denoting the i-th value in the k-th field by :math:`f_{i}^{k}` the output values can be written as:

   .. math::

         m_{i} = \frac {1}{N} \sum_{k}^{N}f_{i}^{k}

   **Dimensions**
   
   *New in metview-python version 1.13.0*. 

   The ability to restrict the computations over a single dimension, such as time or ensemble member,
   is available via the ``dim`` and ``preserve_dims`` parameters, and only when this function is used as a method
   on a :class:`Fieldset` object rather than as a function. The ``dim`` parameter should contain the name
   of an ecCodes key over which the computation should be performed. For example, a :class:`Fieldset` that
   contains multiple parameters, vertical levels, forecast steps and ensemble members can be used to
   quickly generate an ensemble mean with the following call:

    .. code-block:: python

        data = mv.read("ens_data.grib")
        ens_mean = data.mean(dim="number") # "number" is the ecCodes key for ensemble member

   In order to perform this computation, Metview must be able to split the input :class:`Fieldset`
   by its other dimensions so that they are preserved - in the above example, each parameter, level
   and forecast step must be preserved, and only the ensemble members 'collapsed'. An ensemble mean
   will be generated for each unique combination of parameter, level and step. Metview uses
   a built-in list of keys that it ensures are preserved (unless specified as ``dim``). They are
   ``["shortName", "level", "step", "number", "date", "time"]``, but can be modifed by supplying
   a new list of keys via the ``preserve_dims`` parameter. An example of using this would be
   if the input data contains multiple experiment versions. In this case, Metview by default would
   not preserve them as a 'dimension', but would include them in the mean computation. The solution
   would be to supply a ``preserve_dims`` parameter that includes ``"experimentVersionNumber"``.

   .. note::
      
      See also :func:`sum`.


.. py:function:: mean(gpt)
    :noindex:

    Computes the mean of all the values in the values column of ``gpt``. 
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: number or None
    
    Missing values are bypassed in this calculation. If there are no valid values, then None is returned.

.. mv-minigallery:: mean