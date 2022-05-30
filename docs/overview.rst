Overview
===================

**Metview** is a meteorological workstation application designed to be a complete working environment
for both the operational and research meteorologist. Its capabilities include powerful data access,
processing and visualisation. It features both a powerful **icon-based user interface** for
interactive work and a **Python** interface for batch processing.

Metview can take input data from a variety of sources, including:

* :doc:`GRIB </data_types/fieldset>` files (editions 1 and 2)
* :doc:`BUFR </data_types/bufr>` files
* :doc:`MARS </gen_files/icon_functions/retrieve>` (ECMWF's meteorological archive)
* :doc:`ODB </data_types/odb>` (Observation Database)
* :doc:`ASCII data file </data_types/table>` (CSV, grids and scattered data)
* :doc:`Geopoints </data_types/geopoints>` (Metview's own format for handling scattered data)
* :doc:`NetCDF </data_types/netcdf>` files

Powerful data filtering and processing facilities are then available, and if graphics output is desired, then Metview can produce many plot types, including:

* map views with :ref:`scalar <gallery_group_map_scalar>`, :ref:`ensemble <gallery_group_map_ens>`, :ref:`vector <gallery_group_map_vector>`, :ref:`point <gallery_group_map_point>` and :ref:`curve <gallery_group_map_curve>` data in various :ref:`projections <gallery_group_map_projections>` 
* :ref:`cross sections <gallery_group_cross_section>`
* :ref:`Hovmoeller diagrams <gallery_group_hovmoeller>`
* :ref:`average sections <gallery_group_average_section>`
* :ref:`vertical profiles <gallery_group_vertical_profile>`
* :ref:`thermodynamic diagrams <gallery_group_map_thermo>`
* :ref:`x/y graph plots <gallery_group_xy>`
* intelligent overlay of data from various sources on the same map arrangement of multiple plots on the same page

Metview can also interface with external models and applications, such as :ref:`VAPOR <3d_visualisation_with_vapor>`, :ref:`Met3D  <met3d_prepare_icon>`, :ref:`FLEXTRA <the_flextra_interface>` and :ref:`FLEXPART <the_flexpart_interface>`.

