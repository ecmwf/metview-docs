.. _dataset_plotting styles:

Dataset plotting styles
**************************

.. note::

    The :ref:`/examples/working_with_datasets.ipynb` notebook gives an overview of how to work with a dataset. 


Using plot_maps()
----------------------------

Fields from a dataset can be plotted with :func:`plot_maps`, which is using a predefined style (when available) for each parameter. 

The following code: 

.. code-block:: python

    import metview as mv
    ds = mv.load_dataset("demo")

    run = mv.date("2016-09-25 00:00")
    step = [0, 24, 48, 72, 96]

    op = ds["oper"].select(date=run.date(), time=run.time(), step=step)
    msl = op["msl"]
    mv.plot_maps(msl)


generates the following plot with the default style assigned to the mean sea level pressure ("msl"):

.. image:: /_static/dataset/msl_default.png
    :width: 400px

Using a custom style
-----------------------------

We can define our own :func:`mcont` to define a custom style:

.. code-block:: python

    vd = mv.mcont({"contour_line_colour": "purple"})
    mv.plot_maps(msl, vd)

.. image:: /_static/dataset/msl_visdef.png
        :width: 400px


Updating the default style
-----------------------------

We can use ``ds_style()`` the get the associated default style for a given fieldset:

.. code-block:: python

    s = msl.ds_style()
    print(s)
    
::

    Style[name=msl] Visdef[verb=mcont, params={'legend': 'off', 
     'contour_highlight_colour': 'black',
     'contour_highlight_thickness': 4, 'contour_interval': 5, 'contour_label': 'on', 
     'contour_label_frequency': 2, 'contour_label_height': 0.4, 
     'contour_level_selection_type': 'interval', 'contour_line_colour': 'black', 
     'contour_line_thickness': 2, 'contour_reference_level': 1010}]

    
We can create a new style out of it with ``update()`` and pass it to :func:`plot_maps`: 

.. code-block:: python

    s1 = s.update({"contour_interval": 10, "contour_line_colour": "red"})
    mv.plot_maps(msl, s1)

.. image:: /_static/dataset/msl_custom.png
    :width: 400px

    
Getting the available styles
-----------------------------

We can print the list of available styles for a fieldset:

.. code-block:: python

    print(msl.ds_style_list())

::

    ['msl', 'default_mcont']

Then we can get a style object by name:

.. code-block:: python

    s = mv.style.find('default_mcont')
    print(s)

::

    Style[name=default_mcont] Visdef[verb=mcont, params={'contour_automatic_setting': 'ecmwf', 'legend': 'on'}]

and pass it  to :func:`plot_maps`: 

.. code-block:: python

    mv.plot_maps(msl, s)

.. image:: /_static/dataset/msl_default_mcont.png
    :width: 400px


Altering the style with ``update`` works in the same way as was shown for the default style above.