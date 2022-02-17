.. :ref:`Interactive Weather Symbols <weather_symbols>` are a collection of weather symbol and annotation objects that can be interactively added to and then edited in the Metview plot window. 

Please note that currently the visualisation is restricted to the case when the output target is Metview's plot window. On the one hand this requires the Metview GUI to be installed, on the other hand it limits the visualisation to these cases:

* executing the code in Metview's Code Editor (and using the default output target)
* executing the code as a Jupyter notebook with the output target set to 'screen' (see :func:`setoutput`):

In any other cases, e.g. in batch mode :func:`plot`, does not work.
