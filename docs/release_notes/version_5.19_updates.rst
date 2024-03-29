.. _version_5.19_updates:

Version 5.19 Updates
////////////////////

Version 5.19.2
==============

* Externally `released <https://confluence.ecmwf.int//display/METV/Releases>`__\  on 2023-07-11
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.07.0.0 (Atos HPC)

-  **At ECMWF:**

   -  Installed **2023-07-11**

   -  Built
      with **Magics** `4.14.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.31.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.31.0+released>`__

   -  Built with **ODC** version **1.4.6**


**Fixes:**

- UI: fixed an issue that could cause the :ref:`Process Monitor <process_monitor_section>` to crash
- :func:`mhovmoellerview`: improved error message when failing to find matching LNSP fields to ML to PL conversion
- :func:`read`: fixed a small memory leak



Version 5.19.1
==============

* Externally `released <https://confluence.ecmwf.int//display/METV/Releases>`__\  on 2023-05-17
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2023.04.1.0 (Atos HPC)

-  **At ECMWF:**

   -  Installed **2023-05-16**

   -  Built
      with **Magics** `4.13.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.30.2 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.30.0+released>`__

   -  Built with **ODC** version **1.4.6**


**Regrid:**

- Added parameters to :func:`regrid` to control whether geography limits are encoded as decimals or fractions 

**Fixes:**

- uPlot: fixed an issue when zooming in the Geography Tool crashed
- uPlot: fixed an issue when cursor data showed the latitude/longitude coordinates in the wrong order for data layers
- :func:`nearest_gripoints`: fixed an issue when did not get any valid results for GRIB data on a reduced Gaussian grid on a subarea crossing the Greenwich meridian
- :func:`longitudes`: fixed an issue when inaccurate values returned for GRIB data on a reduced Gaussian grid on a subarea 
- :func:`valid_date` and :func:`base_date`: fixed memory leak


Version 5.19.0
==============

* Externally `released <https://confluence.ecmwf.int//display/METV/Releases>`__\  on 2023-04-04
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
