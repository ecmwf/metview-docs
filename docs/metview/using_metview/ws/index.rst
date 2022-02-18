.. _weather_symbols:

Weather Symbol Objects
==================================

.. note::

    Weather Symbol Objects were introduced in Metview 5.14.0, with   
    further development planned for the future   

Weather Symbol Objects are a collection of weather symbols and annotations that can be interactively :ref:`added and edited in <how_to_use_the_weather_symbol_editor_in_metview>` the Metview plot window. These objects are projection aware and will survive plot updates such as
zooming, changes of projection and contouring. 

.. image:: /_static/ug/how_to_use_the_weather_symbol_editor_in_metview/image1.png
   :width: 5.20833in
   :height: 4.23958in

At ECMWF you need the latest Metview version to try out the Weather Symbol Objects. The
command to run is::

    module swap metview/new    
    metview     

From **Metview 5.15.0** each Weather Symbol Object is represented by a Metview icon (see the full list of icons :ref:`here <toc_plot_ws>`). Using the icons the symbols :ref:`can be saved <ws_saving_and_loading>` from the Metview plot window for later reuse. These icons can also be directly visualised or dragged into the plot window. Plotting from a script (Python or Macro) also works but it requires a Metview installation with the GUI component enabled. 

.. toctree::
    :maxdepth: 1
    
    interactive_usage.rst
    save_and_load.rst
    add_your_weather_symbol.rst
