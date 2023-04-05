.. _version_5.19_updates:

Version 5.19 Updates
////////////////////


Version 5.19.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2023-04-04
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.04.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2023-04-04**

   -  Built
      with **Magics** `4.13.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.30.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.30.0+released>`__

   -  Built with **ODC** version **1.4.6**


**Plot window**

- added location label to the bottom right corner (in the statusbar) displaying the coordinates at the mouse cursor position. It can be shown/hidden by using the **Show location label** action in the **View** menu. Visible by default.

   .. image:: /_static/uplot/location_label.png
      :width: 320px

- added new action **Reset cursor data** to the **Tools** menu to move back the cursor data to the middle of the view. It is particularly useful when the cursor data is accidentally moved out of the view and we cannot interact with it any more.

- changed the order how the current coordinates are displayed in the cursor data in geographical views. In the new version latitude comes first followed by longitude.

**Macro/Python**

- :func:`surrounding_points_indexes`: fixed issue when wrong results were generated when target longitude was less than 0 for reduced Gaussian grids in GRIB2 data


.. **Macro to Python converter**

.. A main new feature in this release is the :ref:`Macro to Python converter <macro_to_python>`. It can be launched from the icon context menu in the :ref:`user interface <mv_desktop_overview>` and from the File menu of the Macro editor. The converter is able to generate fully functional Python code in most of the cases but some code structures have to adjusted manually. Details about the adjustment process can be found :ref:`here <macro_to_python_adjustments>`.

**User interface**

- Macro Editor: improved vertical and horizontal space usage in help sidebar. The sidebar now stretches along the full vertical extent and its minimum horizontal extent is significantly reduced. As a further improvement the size of the lower and upper part of the parameter selector (available only for icon functions in the sidebar) can now be controlled with a vertical splitter.

   .. image:: /_static/ui/macro_editor_all_panels.png
      :width: 320px

- Icon Editors: line style parameters now show preview pixmaps of the available styles

   .. image:: /_static/ui/desktop_line_style_editor.png
      :width: 320px

- Icon Editors: fixed issue when widgets were misaligned in weather symbol editors
- Icon Drawers: fixed issue when cannot add icons to newly created drawers



**Cross section**

- Fixed issue when no data was generated when ``vertical_scaling`` was set to "log" and ``level_selection_type`` was set to "count" in :func:`mcross_sect` or :func:`mxsectview`


**New Gallery Examples**

   .. image:: /_static/gallery/ens_stamp_shared_legend_title.png
      :width: 300px
      :target: ../gen_files/gallery/ens_stamp_shared_legend_title.html
