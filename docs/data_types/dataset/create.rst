Creating datasets
**********************

First, find a name for you dataset, e.g. "my_ds". 

Next, create a dataset template by running the following Python script:

    .. code-block:: python

        import metview as mv
        mv.dataset.create_dataset_template("my_ds")

This will create a new directory called "my_ds" in the $MPY_DATASET_ROOT directory (~/mpy_dataset by default). 

Enter "my_ds" and copy your GRIB/CSV data into the "data" directory, preferably each experiment should have a separate subfolder in "data".

The next step is to edit "data.yaml" and put your experiment descriptions there. 

Your dataset is now ready for use. The GRIB indexing will be performed for each experiment on first use. However, it is advised to run it separately with the following script to see if there are any issues with the data configuration:

    .. code-block:: python

        import metview as mv
        ds = mv.load_dataset("my_ds")
        ds.scan()

This will scan all the experiments. I you need to scan (or rescan) only a given experiment you can use the **name** argument of scan():

    .. code-block:: python

        import metview as mv
        ds = mv.load_dataset("my_ds")
        ds.scan(name="my_experiment")


Having done so everything is prepared and you can try out your dataset e.g. like this:

    .. code-block:: python

        import metview as mv
        ds = mv.load_dataset("my_ds")
        ds.describe()


When it comes to the plotting you probably want to change your map area(s), and the map and data plotting styles. You can do it all by editing the files in the "conf" directory. Do not forget, if your working in a Jupyter notebook after any change in "conf" you need to load your dataset again (with load_dataset()) to pick up the cahnges.

.. note::

    See also the page about the :ref:`dataset structure <dataset_structure>`.