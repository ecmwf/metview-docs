select
=============

.. py:function:: select(fs, [d], **kwargs)
.. py:function:: Fieldset.select([d], **kwargs)
   :noindex:


   *New in metview-python version 1.8.0*.

   Extracts a subset of fields matching the conditions defined by a set of ecCodes keys from ``fs``. If called multiple times on the same :class:`Fieldset` it will result in a much better performance than :func:`read`.

   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :param d: filter expressed as a dict
   :type d: dict 
   :param kwargs: filter expressed as a set of keyword arguments
   :rtype: :class:`Fieldset`
   
   .. warning::

        The result is always sorted in ascending order by the following keys: shortName, paramId, date, time, step, typeOfLevel, level, number, experimentVersionNumber, marsClass, marsStream and marsType. 

   We can call :func:`select` either with a set of keyword arguments or with a dictionary as a single positional argument. 

   When **keyword arguments** are used each must be an ecCodes key specifying a value or list of values. These individual conditions are combined together with the logical AND operator to form the filter. For example, extracting temperature fields on 850 and 500 hPa levels can be done like this:

       .. code-block:: python

            import metview as mv
            f = mv.read("my.grib")
            g = f.select(shortName="t", typeOfLevel="isobaricInhPa", level=[850, 500])

   The same filter can be expressed with a **single dictionary argument**:
    
        .. code-block:: python

            g = f.select({"shortName": "t", 
                "typeOfLevel": "isobaricInhPa", 
                "level": [850, 500]
                })

   With the dictionary argument it is possible to use type qualifiers (s=string, l=long, d=double) on the ecCodes keys. For example:

        .. code-block:: python

            g = f.select({"centre:l": 98}) 
       
Date and time keys
+++++++++++++++++++++

   We can use multiple formats to specify the values for the following **date** and **time** related ecCodes keys:
   
    * date, time
    * dataDate, dataTime
    * validityDate, validityTime
    * marsDate, marsTime
   
   E.g. the **date** of 2021-02-04 can be written as:

     * 20210204
     * "20210204"
     * "2021-02-04"
     * datetime.datetime(2021, 2, 4)

   and we have these options for the **time** of 12 hours:

    * 12
    * "12"
    * "1200"
    * "12:00"
    * datetime.time(12)

   For example:

        .. code-block:: python

            g = f.select(date=20210204, time=12, step=9) 
            g = f.select(validityDate="2021-02-04", validityTime=21) 

 
Datetime keys
+++++++++++++++++++++

   It is also possible to use **datetime** keys, which are combined together from individual date and time keys. Please note that these are not valid ecCodes keys, but offered by :func:`select` for convenience. The table below summarises the available datetime keys:
   
   .. list-table::
        :widths: 50 50
        :header-rows: 1

        * - datetime key
          - the keys it is built from
        * - dateTime
          - date, time
        * - dataDate
          - dataDate, dataTime
        * - validityDateTime
          - validityDate, validityTime
        * - marsDateTime
          - marsDate, marsTime

   The value for a datetime key can be defined in multiple ways. E.g. the datetime of 2021-02-04 06:00 can be written as:

    * 20210204.25
    * "2021-02-04 06:00"
    * "2021-02-04 06"
    * datetime.datetime(2021, 2, 4, 6, 0)

   In the example below the three :func:`select` calls are equivalent:

        .. code-block:: python

            g = f.select(date=20210204, time=12, step=9) 
            g = f.select(dateTime="2021-02-04 12:00", step=9)
            g = f.select(validityDateTime="2021-02-04 21:00")

   Datetime keys are particularly useful when we need to extract analyis fields matching a set of forecast fields. The following example shows how it can be done with the help of  :func:`base_date`:

        .. code-block:: python

            fc = mv.read("fc.grib")
            an = mv.read("an.grib")
            # define target datetimes
            d = mv.valid_date(base="2021-02-04 12:00", step=[0, 12, 18])
            # extract data from forecast
            f_fc = fc.select(validityDateTime=d)
            # extract data from analyis
            f_an = an.select(dateTime=d) 
            # compute the fc-an difference (the fields are correctly paired up!)
            diff = f_fc - f_an



.. mv-minigallery:: select