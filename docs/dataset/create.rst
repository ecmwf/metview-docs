Creating datasets
**********************

What is a dataset?
---------------------

First a folder with a name of you dataset, e.g. "my_ds". 

Next, take the "demo" dataset as a template. If do not yet have it on you machine the run the following Python script to get it:

    .. code-block:: python

        import metview as mv
        mv.load_dataset("demo")

Let us suppose not that "demo" is 



A dataset is simply a **set of data files** (GRIB and CSV) packed together with **customised styles** for the ease of visualisation. The GRIB data in a dataset is typically indexed providing fast access to the individual fields. Datasets are best suited for case studies and training courses where participants mainly want to focus on the scientific contents and not on the details of data access and plot customisation. 

.. note::

    The :ref:`/examples/working_with_datasets.ipynb` notebook gives an overview of how to work with a dataset. 
