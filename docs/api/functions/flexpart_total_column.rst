flexpart_total_column
===========================

.. py:function:: flexpart_total_column(**kwargs) 

   Computes the sum/vertical integral of fields in a FLEXPART output GRIB file. 
   
   :param source: the path to the FLEXPART output GRIB file
   :type source: str

   :param data: the :class:`Fieldset` containing the FLEXPART output GRIB data. It takes precedence over ``source``. 
   :type source: :class:`Fieldset` 

   :param param: the ecCodes shortName of the parameter. If param is "mdc" (mass density concentration) the column integrated mass is computed. Otherwise the fields are simply added up for the specified level range.
   :type param: str

   :param top_level: the top height level (inclusive) for the computations. When not specified the integration goes up to the highest available level.
   :type levType: number

   :param bottom_level: the bottom height level (inclusive) for the computations. When not specified the integration starts from the lowest available level.
   :type level: number

   :param step: the forecast step to extract
   :type step: str

   :param release: the release to extract. Release indexing starts at 1.
   :type release: number

   :param ageclass: the ageclass to extract. Ageclass indexing starts at 1.
   :type ageclass: number

   :rtype: :class:`Fieldset`


   :Example:

        .. code-block:: python

            import metview as mv

            # to compute the total column integrated mass for all 
            # the steps, releases and ageclasses
            g = mv.flexpart_total_column(source="my_flexpart_output.grib")


.. mv-minigallery:: flexpart_total_column