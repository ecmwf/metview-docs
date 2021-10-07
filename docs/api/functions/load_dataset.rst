load_dataset
===============

.. py:function:: load_dataset(name_or_path)

    Loads a dataset (see :ref:`Datasets <dataset_overview>`.) 
   
    :param name_or_path: name or path of the dataset (see explanation below)
    :type name: str
    :rtype: :class:`Dataset`

    
Dataset lookup order
++++++++++++++++++++++

    The **MPY_DATASET_ROOT** environment variable defines the root directory for datasets. If it is undefined **$HOME/mpy_dataset** is regarded as the root. When we load a dataset by name like this:

    .. code-block:: python
        
        ds = mv.load_dataset("oifs_2021")

    first the $MPY_DATASET_ROOT/oifs_2021 folder is checked. If this folder does not exist "oifs_2021" is regarded as a **built-in dataset**, and Metview will automatically try to download it from the dedicated download server.

Using a path to a dataset
++++++++++++++++++++++++++++ 

    Datasets can be loaded from a given filesystem path like this:
    
    .. code-block:: python

        ds = mv.load_dataset(mypath)

    In this case the name of the last directory in *mypath* will be the name of the dataset. If, using the name, the dataset is identified as a built-in dataset (i.e. stored on the download server) and not yet available under *mypath*, Metview will automatically download it. Otherwise a well-formed dataset must exist in the folder specified by *mypath*.

    .. warning::
        
        Datasets can be very large so you need to carefully select the location where you want to store them.


.. mv-minigallery:: load_dataset
