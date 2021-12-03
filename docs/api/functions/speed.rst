speed
==============

.. py:function:: speed(u, v)

   Computes the wind speed from the ``u`` and ``v`` wind components.

   :param u: u wind component
   :type u: :class:`Fieldset`
   :param v: v wind component
   :type v: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The resulting values are speed values in the same units as the input fields. A missing value in either ``u`` or ``v``  will result in a missing value in the corresponding place in the output fieldset.

   The ecCodes **paramId** in the output is set as follows:
   
   * 10 (atmospheric wind speed)
   * 207 (10m wind speed)
   * 228249 (100m wind speed)
   * 228241 (200m wind speed)

   In any  other cases the ecCodes **paramId** is set to 10.

.. mv-minigallery:: speed
