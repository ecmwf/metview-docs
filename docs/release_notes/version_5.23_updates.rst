.. _version_5.23_updates:

Version 5.23 Updates
////////////////////

Version 5.23.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2024-xx-xx
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2024-xx-xx (Atos HPC)


-  **At ECMWF:**

   -  Installed **2024-xx-xx**

   -  Built
      with **Magics** `4.15.4 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.35.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.35.0+released>`__

   -  Built with **ODC** version **1.5.0**


**Vertical interpolation**

- :func:`ml_to_hl` now interprets target heights as geometric height. Previously, geopotential height was used internally in the computations. 
- Added the :func:`pl_to_hl` function to interpolate pressure levels to height levels. See the new gallery example :ref:`gallery_pl_to_hl_map`:

   .. image:: /_static/gallery/pl_to_hl_map.png
      :width: 250px
      :target: ../gen_files/gallery/pl_to_hl_map.html


- Added the :func:`geometric_height_from_geopotential` function to compute geometric height from geopotential height. See the new gallery example :ref:`gallery_cross_section_height_pl_orog`:

   .. image:: /_static/gallery/cross_section_height_pl_orog.png
      :width: 250px
      :target: ../gen_files/gallery/cross_section_height_pl_orog.html

- Added the :func:`geopotential_from_geometric_height` function to compute geopotential from geometric height. 
  
**Display Window**

- Added option to export the Display Window contents as an SVG when it contains any weather feature objects.

**Fixes**  

- Fixed issue when dropping a second icon into the plot window caused a crash
- Fixed issue when the tree view was not generated when the underlying dump process wrote anything to stderr
- Fixed issue when the ``vertical_coordinate_param`` option in the Cross section did not work for fields containing string values for the "mars.param" ecCodes key
- Fixed issue when :func:`thermo_parcel_path` did not work with array(Python)/vector(Macro) input data
