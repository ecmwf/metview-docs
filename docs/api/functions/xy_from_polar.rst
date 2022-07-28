xy_from_polar
====================

..  py:function:: xy_from_polar(magnitude,  direction)

    Converts vector data from meteorological polar representation to xy representation.

    :param magnitude: the speed/magnitude
    :type magnitude: number, ndarray or :class:`Fieldset`
    :param direction: the meteorological direction of the vector in degrees
    :type direction: number, ndarray or :class:`Fieldset`
    :rtype: list or :class:`Fieldset` or None

    In polar representation the data is specified by two components:

    * ``magnitude``: represents the speed/magnitude
    * ``direction``: represents the meteorological direction of the vector in degrees (see :func:`direction` for explanation)

    In the target xy representation the x axis points East while the y axis points North.

    The type of the result depends on the type of the input data:

    * if the input is number the result is a list of two numbers
    * if the input is ndarray the result is a list of two ndarrays, the first ndarray contains the x components while the second ndarray the y components
    * if the input is :class:`Fieldset` the result is a fieldset where an x component field is immediately followed by the corresponding y component field.

    .. note::   
      
      See also :func:`direction`.


.. mv-minigallery:: xy_from_polar
