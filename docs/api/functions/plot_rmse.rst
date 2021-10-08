plot_rmse
=============

.. py:function:: plot_rmse(*args, ref=None, area=None, title_font_size=0.4, legend_font_size=0.35, y_max=None)

    High level function with automatic styling to generate RMSE (root mean square error) curve plots from GRIB data.

    :param ref: the reference GRIB data (typically it is an analysis)  
    :type ref: :class:`Fieldset`
    :param area: specifies the geographical area for the RMSE computations as [S, W, N, E]. If it is not not specified all the gridpoints from the input data is used.
    :type area: list
    :param title_font_size: specifies the font size in cm for the plot title
    :type title_font_size: number
    :param legend_font_size: specifies the font size in cm for the plot legend
    :type legend_font_size: number
    :param y_max: specifies the maximum value in scaled data units for the y axis in the RMSE plot. When it is not specified the value is automatically determined from the data.
    :type y_max: number
    
    :func:`plot_rmse` is a convenience function allowing to generate RMSE curve plots in a simple way using predefined settings.
    
    The RMSE value for a given field *f* with respect to the corresponding field from ``ref`` can be written as (N is the number of gridpoints in the field): 

        .. math:: 
            
                rmse = \sqrt {\frac {1}{N} \sum_{i}^{N} (f_{i}-ref_{i})^{2}}

    
Data
++++++++++++++++++++++++

    The :class:`Fieldset` data to be compared to ``ref`` is defined by the positional arguments (``*args``). In ``*args`` each :class:`Fieldset` must be defined on the same grid as ``ref`` and contain the same number of fields. It is also assumed that the dates/times/steps are properly matching that of ``ref``.

Plot style
++++++++++++++
  
    The curve style is automatically assigned to each input data item. The title and the legend is automatically generated using the *label* attribute in the :class:`Fieldset` data in ``*args`` and ``ref``. If a data item is part of a :class:`Dataset` the *label* is automatically set, otherwise it can be defined like this:

    .. code-block:: python

        an = mv.read("an.grib")
        an.label = "an"

    The data units are automatically scaled for the RMSE computations using the same rules that are applied for the units scaling in :func:`mcont`.

Limitations
++++++++++++++++ 

    :func:`plot_rmse` is a high-level function using pre-defined settings, therefore it comes with certain limitations: 

    * the curve style cannot be customised 
    * the title and the legend cannot be customised
    * the horizontal axis cannot be customised
    * on the y axis the maximum value can be set via ``y_max`` but everything else is automatically generated


Example with deterministic forecast
+++++++++++++++++++++++++++++++++++++++++++

    The following example shows how to create an RMSE curve plot with deterministic forecast data (geopotential on 500 hPa): 

        .. code-block:: python

            import metview as mv

            an = mv.gallery.load_dataset("an_z_rmse.grib", check_local=True)
            fc = mv.gallery.load_dataset("fc_z_rmse.grib", check_local=True)

            # filter 500 hPa z
            f_an = an["z500"]
            f_fc = fc["z500"]

            # assign a label
            f_an.label = "AN"
            f_fc.label = "OPER"

            # generate plot
            mv.plot_rmse(f_fc, ref=f_an)


    .. image:: /_static/api/plot_rmse_1.png
        :width: 400px


.. mv-minigallery:: plot_rmse
