speed
==============

.. py:function:: speed(u, v)
.. py:function:: Fieldset.speed()
   :noindex:

   *New in metview-python version 1.9.0*.

   Computes the wind speed from the ``u`` and ``v`` wind components.

   :param u: u wind component
   :type u: :class:`Fieldset`
   :param v: v wind component
   :type v: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The resulting values are speed values in the same units as the input fields. A missing value in either ``u`` or ``v``  will result in a missing value in the corresponding place in the output fieldset.

   When :func:`speed` is called on a :class:`Fieldset` without arguments it is assumed that the fields are already ordered in such a way that each u field is followed by the corresponding v field in the input data.

   The ecCodes **paramId** in the output is set according to the paramId of ``u`` fields.  The possible output paramIds are as follows:
   
   * 10 (atmospheric wind speed)
   * 207 (10m wind speed)
   * 228249 (100m wind speed)
   * 228241 (200m wind speed)

   In any  other cases the ecCodes **paramId** is set to 10.

.. mv-minigallery:: speed
