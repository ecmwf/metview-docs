Metview in Jupyter
===================

Metview fits perfectly well into a Jupyter notebook environment! Just make sure that everything is
installed (see :doc:`installation guide<install>`), fire up a notebook, import metview and you're
ready to go! See the :doc:`notebook gallery <notebook_gallery>` for examples.

If you wish to view a plot inline in the notebook, you will need to call

   .. code-block:: python

      mv.setoutput("jupyter")

before you call the :py:func:`plot` command. As this will generate PNG images in the background,
you can add the parameters for the :py:func:`png_output` function here too, e.g.

   .. code-block:: python

      mv.setoutput("jupyter", output_width=1200)

As an added bonus, if you are plotting :py:class:`Fieldset` s that contain multiple fields,
you will see a widget that allows you to scroll and animate through the different fields
(add `animate=False` to the arguments to the :py:func:`plot` command to disable this). You need to make
sure that your environment has the necessary jupyter and ipywidgets packages installed for
this to work! Note that a widget is always used to display the plots, even if the animation controls
are not visible. This allows the :py:func:`plot` command to be used in a loop to obtain
multiple plots. However, it also means that generated plots will not be written into the notebook
when it is saved. If you would like to save a 'rendered' notebook complete with plots (or you do not
have ipywidgets installed), you can set it up like this before running the noteboook:

   .. code-block:: python

      mv.setoutput("jupyter", plot_widget=False)

