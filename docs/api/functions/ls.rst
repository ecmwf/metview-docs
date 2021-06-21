ls
===========

.. py:function:: Fieldset.ls(extra_keys=[])

    Lists the content of a :class:`Fieldset` by printing values of some ecCodes keys. 

    :param extra_keys: list of additional ecCodes keys. Type qualifiers (s=string, l=long, d=double) can be appended to each key name following the ":" character. E.g. to get "centre" as long use "centre:l".
    :type extra_keys: list of str
    :rtype: Pandas dataframe in a Jupyter notebook, otherwise the dataframe is printed to the standard output
    
    ``ls`` scans the :class:`Fieldset` and for each message extracts values for a **default set of ecCodes keys** and a set of user defined ``extra_keys``. 

    The following example shows how the output looks like in a notebook using the default set of ecCodes keys:

        .. image:: /_static/api/ls_1.png
            :width: 550px

    By adding a set of ``extra_keys`` we get this output:

        .. image:: /_static/api/ls_2.png
            :width: 700px


.. mv-minigallery:: ls
