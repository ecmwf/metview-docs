describe
===========

..  py:function:: describe(fs, [param])
..  py:function:: Fieldset.describe([param])
    :noindex:

    Summarizes the content of a :class:`Fieldset` in a compact way. The output is optimised for Jupyter notebooks.

    :param fs: input fieldset
    :type fs: :class:`Fieldset` 
    :param param:  prints a more detailed summary for the specified ecCodes shortName (str) or paramId (number)
    :type param: str or number
    :rtype: HTML formatted output in a Jupyter notebook, otherwise the summary is printed to the standard output
    
    :func:`describe` scans the :class:`Fieldset` and for each message (i.e. field) extracts a fixed set of metadata values, which are then grouped by parameter and presented in a tabular format. The parameters are identified by their ecCodes shortNames or paramIds. :func:`describe` does not try to form a hypercube(s) but simply lists the unique metadata values for each parameter.

    The following example shows how the output looks in a notebook for a fieldset containing 432 surface and pressure level fields:

        .. code-block:: python

            f = mv.read("fc.grib")
            f.describe() 

        .. image:: /_static/api/describe_1.png
            :width: 600px

    By specifying "q" as an **argument** we can get the detailed summary for specific humidity:

        .. code-block:: python

            f.describe("q") 
        
        .. image:: /_static/api/describe_2.png
            :width: 400px

    We can achieve the same result by using the paramId of specific humidity:

        .. code-block:: python

            f.describe(133) 

    

..  mv-minigallery:: describe
