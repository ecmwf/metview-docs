load_dataset
===============

.. py:function:: load_dataset(name, path="")

   *New in MPY version 1.8.0*.

   Loads a dataset. 
   
   :param name: name of the dataset
   :type name: str
   :param path: path to the dataset 
   :type path: str
   :rtype: :class:`Dataset`

    
Dataset lookup order
++++++++++++++++++++++

    The **MPY_DATASET_ROOT** environment variable defines the root directory for datasets. If it is undefined **$HOME/mpy_dataset** is regarded as the root. When we load a dataset like this:

    .. code-block:: python
        
        ds = mv.load_dataset("oifs_2021")

    first the $MPY_DATASET_ROOT/oifs_2021 folder is checked then if this folder does not exist "oifs_2021" is regarded as a **built-in dataset**, and if available it will be automatically downloaded from the dedicated download server.

Using a path to a dataset
++++++++++++++++++++++++++++ 

    Datasets can be loaded from a given path like this:
    
    .. code-block:: python

        ds = mv.load_dataset("oifs_2021", path=mypath)

    If the dataset is a built-in dataset (i.e. stored on the download server) and not yet available under ``path``, Metview will automatically download it. Otherwise a well-formed dataset must exist in the folder specified by ``path``.

    .. warning::
        
        Datasets can be very large so you need to carefully select the location where you want to store them.

