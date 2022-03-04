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

        From *metview-python version 1.11.0* the result is not sorted but keeps the original field ordering. You need to use :func:`sort` to sort the output. 

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
        * - dataDateTime
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

   Datetime keys are particularly useful when we need to extract analysis fields matching a set of forecast fields. The following example shows how it can be done with the help of  :func:`valid_date`:

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


  .. _select_slice_operator:

Slicing with the [] operator
++++++++++++++++++++++++++++++

    For simple data extractions with :func:`select` a shorthand notation with the [] operator is also available. E.g. instead of

         .. code-block:: python

            g = fs.select(shortName="msl")
      
    we can write:

         .. code-block:: python

            g = fs["msl"]
      

    The following code snippet shows further examples for **scalar** data:

         .. code-block:: python

            fs = mv.Fieldset(path="test.grib")

            # each select/[] pair below is equivalent

            # single level data - we only need to use the ecCodes shortName
            g = fs.select(shortName="msl")
            g = fs["msl"]

            # upper level data without specifying the level
            g = fs.select(shortName="t")
            g = fs["t"]

            # pressure level data - the level units specifier can be omitted in [],  
            # since by default typeOfLevel is assumed to be "isobaricInhPa".
            g = fs.select(shortName="t", level=500, typeOfLevel="isobaricInhPa")
            g = fs["t500"]

            # pressure level data - with level units specifier
            g = fs.select(shortName="t", level=500, typeOfLevel="isobaricInhPa" )
            g = fs["t500hPa"]

            # ECMWF model level data - the level units specifier ("ml") must be used
            g = fs.select(shortName="t", level=32, typeOfLevel="hybrid" )
            g = fs["t32ml"]
            
            # potential temperature level data - the level units specifier (K) must be used
            g = fs.select(shortName="pv", level=320, typeOfLevel="theta" )
            g = fs["pv320K"]


    For **wind** data the [] operator not only extracts the wind components but pair them up properly so that they could be directly plotted. For wind plotting a U wind field must always be followed by a V wind field in the given :class:`Fieldset`.

      .. note::
      
        This wind extraction method only works for "10u"/"10v" and "u"/"v" ecCodes shortNames.
            
    The following code snippet shows some examples:
      
        .. code-block:: python

           fs = mv.Fieldset(path="wind.grib")

           # 10m wind - extract "10u","10v" and pair them up
           g = fs["wind10m"]
           
           # pressure level wind data - extract "u","v" on 500 hPa and pair them up.
           # The level units specifier can be omitted in [], since by default 
           # typeOfLevel is assumed to be "isobaricInhPa".        
           g = fs["wind500"]

           # pressure level wind data -  with level units specifier.
           # Extract "u"/"v" on 500 hPa and pair them up.
           g = fs["wind500hPa"]

           # model level wind data - the level units specifier ("ml") must be used.
           # Extract "u"/"v" on model level 32 and pair them up.
           g = fs["wind32ml"]
                     
    There is a special notation for the extraction and alignment of 3D wind components. It works with the "u", "v" and "w" ecCodes shortNames. The following code shows how to extract the 3D wind for all the levels present in a :class:`Fieldset`: 

         .. code-block:: python

           fs = mv.Fieldset(path="wind3d.grib")

           # extract "u","v", "w" and align them in that order
           g = fs["wind3d"]
           

.. mv-minigallery:: select