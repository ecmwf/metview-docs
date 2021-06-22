describe
===========

.. py:function:: describe(fs, param=None)
.. py:function:: Fieldset.describe(param=None)
   :noindex:

    Summarizes the content of a :class:`Fieldset` in a compact way. The output is optimised for Jupyter notebooks.

    :param fs: input fieldset
    :type fs: :class:`Fieldset` 
    :param param: only prints the summary for the specified ecCodes shortName
    :type param: str
    :rtype: HTML formatted output in a Jupyter notebook, otherwise the summary is printed to the standard output
    
    :func:`describe` scans the :class:`Fieldset` and for each message (i.e. field) extracts a fixed set of metadata values, which are then grouped by parameter and presented in a tabular format. The parameters are identified by their ecCodes shortNames. :func:`describe` does not try to form a hypercube(s) but simply lists the unique metadata values for each parameter.

    The following example shows how the output looks in a notebook for a fieldset containing 432 surface and pressure level fields:

        .. image:: /_static/api/describe_1.png
            :width: 600px

    By specifying param="q" we can get the detailed summary for specific humidity:

        .. image:: /_static/api/describe_2.png
            :width: 400px


.. mv-minigallery:: ls
