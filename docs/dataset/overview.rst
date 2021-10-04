.. _dataset_overview:

Dataset overview
**********************

What is a dataset?
---------------------

A dataset is simply a **set of data files** (GRIB and CSV) packed together with **customised styles** for the ease of visualisation. The GRIB data in a dataset is typically indexed providing fast access to the individual fields. Datasets are best suited for case studies and training courses where participants mainly want to focus on the scientific contents and not on the details of data access and plot customisation. 

.. note::

    The :ref:`/examples/working_with_datasets.ipynb` notebook gives an overview of how to work with a dataset. 


Data access
-----------------

* We load a dataset via :func:`load_dataset`. The contents can be inspected via :func:`describe` and GRIB data can be extracted with :func:`select`. 

* The data access is based on metadata-indexing and normally much faster than standard GRIB access in Metview 

* On top of the GRIB files a dataset can also contain storm tracks in CSV format.

Visualisation
------------------

* The dataset comes with a set of predefined map areas, map styles and data plotting styles. Metview offers a set of high-level plotting functions that are aware of these settings and try to use them by default. This is the full list of these functions:

    * :func:`plot_maps`: generic map-based plots. Can be used for both the GRIB and track data from a dataset.
    * :func:`plot_diff_maps`: generates difference plots for GRIB data. Ideal to compare experiments or forecast and analysis.
    * :func:`plot_xs`: generates vertical cross sections with a side map showing the transect line.

* Custom, user defined styles (visual definitions in the Metview terminology) can also be used with all the above plotting routines. 



