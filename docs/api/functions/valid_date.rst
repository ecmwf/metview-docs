valid_date
=================

.. py:function:: valid_date(base=None, step=[], step_units=datetime.timedelta(hours=1))
   
   *New in MPY version 1.8.0*.
   
   Adds a list of steps specified in ``step_units`` to the ``base`` date.
      
   :param base: the base date
   :type base: datetime.datetime 
   :param step: the steps to be added to ``base``
   :type step: list of numbers or str
   :param step_units: the units of the values in ``step``
   :type step_units: datetime.timedelta
   :rtype: list of datetime.datetime objects


.. py:function:: valid_date(fs)

   Returns the valid dates (including the time components) for each field in ``fs``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: datetime.datetime or list of datetime.datetime objects

   If ``fs`` has only one field, a date is returned; otherwise a list of dates are returned.

.. mv-minigallery:: valid_date