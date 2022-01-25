.. _version_5.3_updates:

Version 5.3 updates
///////////////////


* Externally `released <https://confluence.ecmwf.int/display/METV/Releases>`__ on 2018-12-05
* Became metview/new at ECMWF on 2018-12-05 (Linux desktops, ecgate, lxc, lxop)

-  **At ECMWF:**

   -  Installed **2018-12-05**

   -  Built
      with **Magics** `3.3.1 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.10.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.10.0+released>`__

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib** `000459 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

   -  Built with **mir 1.1.0**

**Highlights:**

-  **ecCharts icon:** new icon,
   :ref:`ecCharts <eccharts_icon>`, 
   which gives access to ecCharts layers and styles through Metview.
   This means that pre-defined data layers used in ecCharts can be
   accessed through Metview, but for past or experimental data as well
   as recent data. Through the context menu, macros and Python scripts
   can also be generated from this icon.

   .. figure:: /_static/release/version_5.3_updates/image1.png
      :width: 4.27083in
      :height: 2.60417in

   The ecCharts icon gives access to data layers and graphical styles defined in ecCharts

**Other features and fixes:**

-  **General**: improved error reporting, e.g. in cases where a plot
   command calls another module (e.g. Cross Section)

-  **Plotting**: plotting to file no longer accumulates memory between
   plots

-  **Plotting**: added Polar South projection to Geographical View

-  **Met3D**: fixed issue with retrieving LNSP data in :ref:`Met3D
   Prepare <met3d_prepare_icon>`
   icon

-  **Python**: fixed error message when indexing a fieldset with a bad
   index

-  **Python**: allow export of Tables to pandas dataframe

-  **BUFR Filtering**: improvement in performance in certain cases

-  **BUFR Examiner**: added context menu item to copy the name of the
   selected key to the clipboard

-  **UI**: simplified the filter for the contouring styles in the
   :ref:`Contouring <mcont_icon>`
   editor

-  **UI**: icon editors now have 'Copy colour' and 'Paste colour' so as
   to share colour definitions via the clipboard

   .. image:: /_static/release/version_5.3_updates/image2.png
         :width: 2.08333in
         :height: 1.12016in

-  **Build**: fixed installation issue on Mac OSX
