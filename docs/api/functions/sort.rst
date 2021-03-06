sort
=========

.. py:function:: sort(fs, [keys, [orders]], ascending=True)
.. py:function:: Fieldset.sort([keys, [orders]], ascending=True)
   :noindex:

   Sorts ``fs`` according to the specified options.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param keys: sorting key(s), they must be valid ecCodes keys
   :type keys: str or list
   :param orders: sorting order(s)
   :type orders: str or list
   :param ascending: sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the ``keys``.
   :type ascending: bool or list of bool
   :rtype: :class:`Fieldset` 

   If no ``keys`` are specified the sorting is performed by the following ecCodes keys in the specified order:

      * date
      * time
      * step
      * number
      * level
      * paramId

   Here **number** is the ENS forecast member number.

   If ``keys`` are specified (either as a list or a str) they define the sorting keys (they must be valid ecCodes keys).

   The optional ``ascending`` can specify the ascending/descending sorting direction. ``ascending`` can be either a bool or a list of bool:

   * if it is a str the sorting direction applies to all the ``keys``
   * if it is a list ``keys`` must also be a list with the same number of elements - the sorting directions apply to each sorting key specified.

   The sorting direction can also be expressed by the optional ``orders``: ">" means descending, while "<" means ascending order. It cannot be used together with ``ascending``. ``orders`` can be either a str or a list:

   * if it is a str the sorting direction applies to all the ``keys``
   * if it is a list ``keys`` must also be a list with the same number of elements - the sorting directions apply to each sorting key specified.


.. .. py:function:: sort(fs, [keys, [orders]])

..    Sorts ``fs`` according to the specified options.

..    :param fs: input fieldset
..    :type fs: :class:`Fieldset`
..    :param keys: sorting key(s)
..    :type keys: str or list
..    :param orders: sorting order(s)
..    :type orders: str or list
..    :rtype: :class:`Fieldset` 

..    The list of MARS keys that can be used for the sorting are as follows (they are specified in order of precedence): 

..       * date
..       * time
..       * step
..       * number
..       * levelist
..       * param
   
..    Here **number** is the ENS forecast member number, while **param** is the ecCodes paramID (int).

..    If no options are specified :func:`sort` sorts ``fs`` in ascending order according to the allowed MARS keys.

..    If ``keys`` are specified (either as a list or a str) they define the sorting keys, which must be chosen from the allowed list of MARS keys.

..    The optional ``orders`` can specify the sorting direction: ">" means descending, while "<" means ascending order. ``orders`` can be either a str or a list:

..    * if it is a str the sorting direction applies to all the ``keys``
..    * if it is a list ``keys`` must also be a list with the same number of elements - the sorting directions apply to each sorting key specified.

.. mv-minigallery:: sort
