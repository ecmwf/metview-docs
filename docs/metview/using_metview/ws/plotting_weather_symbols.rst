.. _ws_plotting:

Plotting weather symbols
===========================

.. note::

    Plotting Weather Symbol Objects using a script was introduced in Metview 5.15.0.


The plotting of Weather Symbol Objects from a script (Python or Macro) is restricted to the case when the output target is Metview's plot window. On the one hand this requires the Metview GUI to be installed, on the other hand it limits the visualisation to these cases:

* execute the code in Metview's Code Editor (the default output target here is already 'screen')
* execute the code as a Jupyter notebook with the output target set to 'screen' (see :func:`setoutput`):

In any other cases, e.g. in batch mode, :func:`plot` does not work.
