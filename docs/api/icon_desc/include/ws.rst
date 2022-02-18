.. :ref:`Weather Symbol Objects <weather_symbols>` are a collection of weather symbol and annotation objects that can be interactively added to and then edited in the Metview plot window. 

*New in Metview version 5.15.0*.

.. warning:: 

    The script-based Weather Symbol Object visualisation is currently restricted to 'screen' output target (i.e. when the output is Metview's plot window). On the one hand this requires the Metview GUI to be installed, on the other hand it limits the visualisation to these cases:

    * execute the code in Metview's Code Editor (and using the default output target)
    * execute the code as a Jupyter notebook with the output target set to 'screen' (see :func:`setoutput`):

    In any other cases, e.g. in batch mode, :func:`plot` does not work.
