flexpart_filter
==================

.. py:function:: flexpart_filter(**kwargs) 

   Extracts fields from the output GRIB files of the FLEXPART disperison model run within Metview. 
   
   :param source: the path to the FLEXPART output GRIB file
   :type source: str

   :param data: the :class:`Fieldset` containing the FLEXPART output GRIB data. It takes precedence over ``source``. 
   :type source: :class:`Fieldset` 

   :param param: the ecCodes shortName of the parameter to extract
   :type param: str

   :param levType: the type of level to extract
   :type levType: {"hl", "sfc"}, default "hl"

   :param level: the level to extract
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

            # to read parameter mdc (mass density concentration) for level 5000 m, 
            # for all the timesteps, releases and ageclasses
            g = mv.flexpart_filter(
                    source="my_flexpart_output.grib",
                    param="mdc",
                    level=5000)

   .. note:: 

        This function is obsolete. From *metview-python version 1.8.0* use :func:`select` instead. The example above can be rewritten with :func:`select` as follows:

        .. code-block:: python

            import metview as mv

            # to read parameter mdc (mass density concentration) for level 5000 m, 
            # for all the timesteps, releases and ageclasses
            f = mv.read("my_flexpart_output.grib")
            g = f.select(shortName="mdc", level=5000, typeOfLevel="heightAboveGround")



.. mv-minigallery:: flexpart_filter