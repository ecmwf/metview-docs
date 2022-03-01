direction
==============

.. py:function:: direction(u, v)

   Computes the meteorological wind direction in degrees in each grid point of ``u`` and ``v``.

   :param u: u wind component
   :type u: :class:`Fieldset`
   :param v: v wind component
   :type v: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The meteorological wind direction is the direction from which the wind is blowing. Wind direction increases
   clockwise such that a northerly wind is 0°, an easterly wind is 90°, a southerly wind is 180°, and
   a westerly wind is 270°. The figure below illustrates how it is related to the actual orientation of the wind vector.

   .. image:: /_static/api/wind_direction.png
        :width: 400px

   .. note::

      See also :func:`xy_from_polar`

.. mv-minigallery:: direction
