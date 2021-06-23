select
=============

.. py:function:: select(fs, [d], **kwargs)
.. py:function:: Fieldset.select([d], **kwargs)
   :noindex:

   Extracts a subset of fields matching the conditions defined by a set of ecCodes keys from ``fs``. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :param d: filter expressed as a dict
   :type d: dict 
   :rtype: :class:`Fieldset`
   

   We can call :func:`select` either with a set of keyword arguments or with a dictionary as a single positional argument. 

   When **keyword arguments** are used each must be an ecCodes key specifying a value or list of values. These individual conditions are combined together with a logical AND to form the filter. For example, extracting temperature fields on 850 and 500 hPa levels can be done like this:

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
            
   .. note::
        
        If :func:`select` is called on the same :class:`Fieldset` multiple times it provides a better performance than :func:`read`.


.. mv-minigallery:: select