.. _version_5.17_updates:

Version 5.17 Updates
////////////////////


Version 5.17.0
==============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2022-xx-xx
* Became metview/new at ECMWF on 2022-xx-xx (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2022-xx-xx**

   -  Built
      with **Magics** `4.12.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.26.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.26.0+released>`__

   -  Built with **ODC** version **1.4.5**

   -  Includes
      version `1.12.0 <https://github.com/ecmwf/metview-python/blob/master/CHANGELOG.rst>`__ of
      the Python interface


**Thermo parcel path**

The parcel computations have been revised and several new option were added. 

* :func:`lifted_condensation_level`: improved speed by using [DaviesJones1983]_ instead of an iterative process to compute the :math:`t_{LCL}`. Works now with ndarrays and :class:`Fieldset` as input (previously only numbers were accepted).
* :func:`thermo_parcel_path`: 
  
  * the options became keyword arguments. Previously they were specified as a dict as the last positional argument. The old interface still works for backwards compatibility. E.g.:

      .. code-block:: python

         # the new interface
         mv.thermo_parcel_path(prof, mode="surface", stop_at_el=False)

         # the old interface
         mv.thermo_parcel_path(prof, {"mode": "surface", "stop_at_el": False})

  * The computations can now use the **virtual temperature correction**, which is enabled by default. See the ``virtual`` key in the ``options`` argument.
  * The **Lifted Index (LI)** was added to the output
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

  * Added new parameters ``compute_top`` and ``el_area`` to to control the  computations and data extraction above the Equilibrium Level (EL)
   
      
**Hovmoller**

* Line Hovmoeller: fixed issue when North and South coordinates of lines going from SW to NE were automatically swapped
  

**Macro/Python**

* :func:`mvl_ml2hPa`: allowed to specify the target pressure levels as an ndarray
* added new function :func:`static_stability` to compute the static stability 
* added new function :func:`q_vector` to compute the Q-vector used in the quasi-geostrophic (QG) theory
* :func:`geostrophic_wind`: added new option ``coriolis`` to use a constant Coriolis parameter value


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