ls
===========

..  py:function:: ls(fs, extra_keys=[], filter={})
..  py:function:: Fieldset.ls(extra_keys=[], filter={})
    :noindex:

    *New in metview-python version 1.8.0*.

    Lists the messages of a :class:`Fieldset` by printing the values of some ecCodes keys. 

    :param fs: input fieldset
    :type fs: :class:`Fieldset` 
    :param extra_keys: list of additional ecCodes keys. Type qualifiers (s=string, l=long, d=double) can be appended to each key name following the ":" character. E.g. to get "centre" as long use "centre:l".
    :type extra_keys: list of str
    :param filter: defines a filter to list only a subset of the messages. A filter is a set of ecCodes keys each with a matching value or list of values. These individual conditions are combined together with a logical AND to define the filter (just like in :func:`select`).
    :type filter: dict 
    :rtype: Pandas dataframe. If not in a Jupyter notebook the dataframe is printed to the standard output
    
    :func:`ls` scans the :class:`Fieldset` and for each message extracts values for a **default** set of ecCodes keys. Additional keys can be listed with ``extra_keys`` while ``filter`` defines the conditions to list only a subset of the messages. 

    The following example shows how the output looks in a notebook using the default set of ecCodes keys:

        .. code-block:: python

            import metview as mv
            f = mv.read("tuv_pl.grib")
            f.ls()

        .. image:: /_static/api/ls_1.png
            :width: 550px

    We can add additional keys by using ``extra_keys``:

        .. code-block:: python

            f.ls(extra_keys=["edition", "paramId:s", "mars.param"])
    
        .. image:: /_static/api/ls_2.png
            :width: 750px


    To list only the fields on 850 hPa we can use ``filter`` in the following way:

        .. code-block:: python

            f.ls(filter={"level": 850})

        .. image:: /_static/api/ls_3.png
            :width: 550px

..  mv-minigallery:: ls
