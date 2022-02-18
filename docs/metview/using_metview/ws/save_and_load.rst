.. _ws_saving_and_loading:

Saving and loading weather symbols
///////////////////////////////////////////////

.. note::

    Saving and loading Weather Symbol Objects was introduced in Metview 5.15.0.


Saving individual objects
----------------------------

You can save weather symbols from Metview's plot window by selecting the given object and using the context menu:

.. image:: /_static/ug/ws_saving_and_loading/context_menu_1.png
   :width: 120px

Here the **Save to user library** action will add the given object to the :ref:`User library<ws_user_library>`. The other action is **Save to disk** that will write the object to disk into a file represented by a :ref:`weather symbol icon <toc_plot_ws>` in Metview's :ref:`user interface <user_interface>`.

.. note::

    Both the style and the geographical location are saved for each object.


Saving a collection
----------------------------

The context menu in the plot window also allows to save all the weather symbols in the current scene into disk as a collection. The resulting file is represented by a WS_COLLECTION icon in Metview's :ref:`user interface <user_interface>`.

.. image:: /_static/WS_COLLECTION.png
   :width: 36px


Working with icons in the user interface
---------------------------------------------

Weather symbol icons can be directly visualised (right-click **Visualise**) or dragged into the plot. Please note that when dropping these icons into a plot they will be placed at the coordinates they store and not at the drop position!

The parameters stored in the icons (with the exception of WS_COLLECTION) can all be edited using the icon editor (right-click **Edit**).


.. _ws_user_library:

The User library
-----------------------

The **User library** of weather symbols can be accessed in Metview's plot window in the sidebar under the **Symbols** tab:

.. image:: /_static/ug/ws_saving_and_loading/user_library_sidebar.png
   :width: 200px

You can add the library items to the plot using two different actions:

* **Add to plot at stored coord**: the item is added to the plot at the coordinate position stored in the item
* **Add to plot as click**: the item is added to the plot at the location where we click

.. image:: /_static/ug/ws_saving_and_loading/context_menu_2.png
   :width: 200px


Where does the User library store its items?
----------------------------------------------

The items in the User library are stored as weather symbol icons in two possible directories.

The primary directory is **System/Symbols/icons** in your Metview home directory. All the items added from the plot to the User library will be placed here.

You can also specify an extra directory using the **METVIEW_EXTRA_FEATURE_SYMBOLS_DIR** environment
variable. If it is defined and it has an **icons** subdirectory its contents will be available in the User library. 
