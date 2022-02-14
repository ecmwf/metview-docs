deacc
===========

..  py:function:: deacc(fs, key=None, skip_first=False, mark_derived=True)
..  py:function:: Fieldset.deacc(key=None, skip_first=False, mark_derived=True)
    :noindex:

    *New in metview-python version 1.10.0*.

    De-accumulates the values in a :class:`Fieldset` by subtracting each field from the next one.

    :param fs: input fieldset
    :type fs: :class:`Fieldset` 
    :param key: if it is None or empty the de-accumulation is performed by subtracting each field from the next field in the input data. Otherwise ``key`` specifies the ecCodes key to group the fields by for de-accumulation. In this case the input data must contain the same number of fields for each ``key`` value and the subtraction is performed by subtracting each field in a given group from the corresponding field in the next group.
    :type by: str or None
    :param skip_first: when it is True the first field in ``fs`` will not be added to the output. Otherwise the first field of ``fs`` will be the first field of the output with all its values set to zero.
    :type skip_first: bool
    :param mark_derived: mark the resulting fields as "derived". This piece of information is used for value scaling in :class:`Fieldset` plotting. See the ``grib_scaling_of_derived_fields`` option in :func:`mcont`. 
    :type mark_derived: bool
    :rtype: :class:`Fieldset`
    
    :func:`deacc` performs no sorting at all and assumes that all the input fields are already in the required order. To sort the input data you can use :func:`sort`.
    

..  mv-minigallery:: deacc
