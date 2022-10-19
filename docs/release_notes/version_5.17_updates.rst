.. _version_5.17_updates:

Version 5.17 Updates
////////////////////


Version 5.17.2
==============

* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2022.08.1.0 (Atos HPC, tag 'new')

-  **At ECMWF:**

   -  Installed **2022-10-19**

   -  Built
      with **Magics** `4.12.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.27.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.27.0+released>`__

   -  Built with **ODC** version **1.4.6**


**Fixes:**

-  Meteogram module (:func:`meteogram`) uses URL to retrieve charts from Bologna by default
-  Meteogram module: fixed issue where the specified time was ignored and the meteogram for time 00UTC was always retrieved
-  FLEXPART: fixed paths to FLEXPART executable and resources at ECMWF
-  Macro: fixed issue in the :func:`mask` function that caused an infinite loop if an area that straddled the date line was given
  

Version 5.17.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-08-24
* Became metview/new at ECMWF on 2022-08-24 (Linux desktops, ecgate, lxc, lxop, Cray HPC)
* Installed as part of `ecmwf-toolbox <https://confluence.ecmwf.int/display/UDOC/HPC2020%3A+ECMWF+software+and+libraries>`__\ /2022.08.0.0 (Atos HPC)


-  **At ECMWF:**

   -  Installed **2022-08-24**

   -  Built
      with **Magics** `4.12.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.27.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.27.0+released>`__

   -  Built with **ODC** version **1.4.6**

   -  Includes
      version `1.13.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface

**Plotting**

:func:`mcont` can automatically adjust predefined palettes and user defined colour lists to the actual contour level values with the new ``contour_shade_colour_list_policy`` = "dynamic" option. It is also possible to reverse palettes and colour lists for plotting by setting ``contour_shade_colour_reverse_list`` to "on". See the :ref:`gallery example <gallery_dynamic_palette>`:

   .. image:: /_static/gallery/dynamic_palette.png
      :width: 260px
      :target: ../gen_files/gallery/dynamic_palette.html
   

**Thermo parcel path**

The parcel computations have been revised and several new option were added:

* :func:`lifted_condensation_level`: improved speed by using [Bolton1980]_ instead of an iterative process to compute the :math:`t_{LCL}`. Works now with ndarrays and :class:`Fieldset` as input (previously only numbers were accepted).
* :func:`thermo_parcel_path`: 
  
  Algorithmic changes:

  * the equivalent potential temperature defining the pseudo-adiabatic path is now computed with formula (39) from [Bolton1980]_ 
  * the LFC (Level of Free Convection) is now determined as the bottom pressure of the positive buoyancy area highest in the atmosphere. This results in improved CIN computation when there are multiple positive buoyancy areas above the LCL. In these situations the CIN was formerly underestimated.
  * the Lifted Index (LI) is now computed and added to the output

  Interface changes:

  * the ``options`` became keyword arguments. Previously they were specified as a dict as the last positional argument. The old interface still works for backwards compatibility. E.g.:

      .. code-block:: python

         # the new interface
         mv.thermo_parcel_path(prof, mode="surface", stop_at_el=False)

         # the old interface
         mv.thermo_parcel_path(prof, {"mode": "surface", "stop_at_el": False})

  * The computations can now use the **virtual temperature correction**, which is enabled by default. See the ``virtual`` key in the ``options`` argument.
  * The "most_unstable" mode was renamed "mucape". The old name is still supported but deprecated.
  * The "mean_layer" mode was renamed "ml". The old name is still supported but deprecated.
  * The "ml" start conditions are determined in a new way. Previously simply the mean values of temperature, dewpoint and pressure in the given layer were used. Now, the temperature is determined from the mean potential temperature, the dewpoint is the mean value in the layer and pressure is the surface pressure.
  * New start modes were added: "m50" and "ml100". They are the variants of the "ml" mode with a fixed 50 hPa and 100 hPa bottom layer, respectively.
  * The size of the layer in "ml" and "mucape" mode can now be specified via the ``layer_depth`` parameter. 
  * The default start conditions were changed to ``mode`` = "mucape" with ``layer_depth`` = 300. E.g.:

      .. code-block:: python

        # these calls are now equivalent
        mv.thermo_parcel_path(prof)
        mv.thermo_parcel_path(prof, mode="mucape", layer_depth=300)

  * Added new parameters ``compute_top`` to control the  computations and data extraction above the Equilibrium Level (EL)

  * See the :ref:`gallery example <gallery_parcel_path_multiple_start_conditions>` showcasing some of the new features:

   .. image:: /_static/gallery/parcel_path_multiple_start_conditions.png
      :width: 260px
      :target: ../gen_files/gallery/parcel_path_multiple_start_conditions.html
   

**Thermo profile**

* Thermo Bufr: added new parameters to specify location by WMO name, WMO ident and :xref:`wigos_wsi`. See: :func:`thermo_bufr` and :func:`thermoview`.
* Improved error message when no BUFR message matching the required location and BUFR data subtype was found in input.


**Hovmoller**

* Vertical Hovmoeller: added new parameters ``use_fixed_surface_pressure`` and ``fixed_surface_pressure`` to use a fixed surface pressure value in the computations. These can be used when the input data is model level and the vertical axis is pressure ( ``vertical_level_type`` = "pressure"). See: :func:`mhovmoellerview` and :func:`mhovmoeller_vertical`.
* Line Hovmoeller: fixed issue when North and South coordinates of lines going from SW to NE were automatically swapped
  

**User interface**

* Colour editor: redesigned interface and added RGB, HSL and greyscale colour sliders
  
   .. image:: /_static/release/version_5.17_updates/colour_slider.png  
      :width: 280px
      
* Desktop: added "Copy filesystem path" action to the context menu of the Breadcrumbs items
* Contour icon editor: added option to show/hide filter options for palette chooser interface
* Family icons: fixed issue when could not edit newly created family icons
* Advanced search: fixed issue when search did not work with time period in Metview versions built with Qt >= 5.8.0 
* Advanced search: fixed issue when results from the last day of time period were excluded
* Grib Examiner: fixed issue when the value of the mars.expver key was not shown in the Namespace dump

**FLEXTRA/FLEXPART**

* :func:`flextra_prepare`: added parameter ``flextra_an_mars_class`` to control the MARS class of the analysis data retrieved when ``flextra_prepare_mode`` is "period". The possible values are "od" (operational analysis) and "ea" (ERA5).
* :func:`flextra_prepare`: fixed issue when setting ``flextra_prepare_mode`` to "period" caused an error
* :func:`flexpart_prepare`: fixed issue when setting ``flexpart_prepare_mode`` to "period" caused an error

**Macro/Python**

* :func:`mean` and :func:`sum`: added new parameter ``dim`` to restrict computations to a specific dimension of :class:`Fieldset` data in python, e.g. compute an ensemble mean when multiple steps exist in the data
* added new function :func:`pl_to_pl` to perform interpolation from pressure level GRIB fields onto a set of target pressure levels
* improved speed and reduced memory usage in many GRIB-related functions
* added new function :func:`static_stability` to compute the static stability. See the :ref:`gallery example <gallery_static_stability>`:

   .. image:: /_static/gallery/static_stability.png
      :width: 350px
      :target: ../gen_files/gallery/static_stability.html

* added new function :func:`q_vector` to compute the Q-vector used in the quasi-geostrophic (QG) theory. See the :ref:`gallery example <gallery_q_vector>`:

   .. image:: /_static/gallery/q_vector.png
      :width: 280px
      :target: ../gen_files/gallery/q_vector.html

* added new functions :func:`smooth_n_point` and :func:`smooth_gaussian` to perform spatial smoothing on fieldsets with lat-lon grids. See the :ref:`gallery example <gallery_gaussian_smoothing>`:

   .. image:: /_static/gallery/gaussian_smoothing.png
      :width: 280px
      :target: ../gen_files/gallery/gaussian_smoothing.html

* added new function :func:`convolve` to perform spatial 2D convolution on fieldsets with lat-lon grids
* added new function :func:`rms_a` to compute area-weighted root mean square for each field in a fieldset
* added new function :func:`grib_indexes` to return GRIB message information for a Fieldset
* :func:`grib_set`: added new option ``repack`` to repack GRIB data. It is required to use when setting some ecCodes keys (e.g. *packingType*) involving properties of the packing algorithm.
* :func:`geostrophic_wind`: added new option ``coriolis`` to use a constant Coriolis parameter value
* :func:`mvl_ml2hPa`: allowed to specify the target pressure levels as an ndarray
* :func:`direction`: fixed issue when the ecCodes paramId in the resulting field was not set to 131 (=wind direction)
* fixed issue when using fields with mixed expver caused Metview to hang in cross section, average cross section, vertical profile and Hovmoeller computations and plotting


**New Gallery Examples**


   .. image:: /_static/gallery/absolute_vorticity.png
      :width: 250px
      :target: ../gen_files/gallery/absolute_vorticity.html

   .. image:: /_static/gallery/thickness.png
      :width: 250px
      :target: ../gen_files/gallery/thickness.html

   .. image:: /_static/gallery/eddy_kinetic_energy.png
      :width: 250px
      :target: ../gen_files/gallery/eddy_kinetic_energy.html

   .. image:: /_static/gallery/categorical_wind_direction.png
      :width: 250px
      :target: ../gen_files/gallery/categorical_wind_direction.html

   .. image:: /_static/gallery/high_vegetation_type.png
      :width: 250px
      :target: ../gen_files/gallery/high_vegetation_type.html
   
   .. image:: /_static/gallery/low_vegetation_type.png
      :width: 250px
      :target: ../gen_files/gallery/low_vegetation_type.html

   .. image:: /_static/gallery/fc_steps.png
      :width: 250px
      :target: ../gen_files/gallery/fc_steps.html

   .. image:: /_static/gallery/fc_steps_shared_title.png
      :width: 250px
      :target: ../gen_files/gallery/fc_steps_shared_title.html

   .. image:: /_static/gallery/fc_steps_shared_legend_title.png
      :width: 250px
      :target: ../gen_files/gallery/fc_steps_shared_legend_title.html

   .. image:: /_static/gallery/cross_section_pl_tadv.png
      :width: 250px
      :target: ../gen_files/gallery/cross_section_pl_tadv.html

   .. image:: /_static/gallery/line_hovm_era5_t850.png
      :width: 250px
      :target: ../gen_files/gallery/line_hovm_era5_t850.html

   .. image:: /_static/gallery/line_hovm_with_map_era5.png
      :width: 250px
      :target: ../gen_files/gallery/line_hovm_with_map_era5.html

   .. image:: /_static/gallery/line_hovm_with_orog_era5.png
      :width: 250px
      :target: ../gen_files/gallery/line_hovm_with_orog_era5.html

   .. image:: /_static/gallery/tephigram_fc_and_obs.png
      :width: 250px
      :target: ../gen_files/gallery/tephigram_fc_and_obs.html

   .. image:: /_static/gallery/parcel_path_from_bufr.png
      :width: 250px
      :target: ../gen_files/gallery/parcel_path_from_bufr.html

   .. image:: /_static/gallery/skewt_parcel_path_with_hodograph.png
      :width: 250px
      :target: ../gen_files/gallery/skewt_parcel_path_with_hodograph.html