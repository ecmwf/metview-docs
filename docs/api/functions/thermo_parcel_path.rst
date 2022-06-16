thermo_parcel_path
=====================

..  py:function:: thermo_parcel_path(profile, mode="mucape", virtual=True, start_t=None, start_td=None, start_p=None, top_p=None, bottom_p=None, layer_depth=None, stop_at_el=False, comp_top=False, el_area=False)
..  py:function:: thermo_parcel_path(t, td, p, **kwargs)
    :noindex:

    Computes the path of an ascending thermodynamic parcel with the given start condition for the given vertical profile. 
    
    :param t: temperature profile (°C)
    :type t: ndarray
    :param td: dewpoint temperature profile (°C)
    :type td: ndarray
    :param p: pressure profile (hPa)
    :type p: ndarray
    :param profile: profile data extracted from a :class:`Fieldset` or :class:`Bufr` for a thermodynamic diagram
    :type profile: :func:`thermo_bufr` or :func:`thermo_grib`
    :param mode: the start condition mode. The possible values are "surface", "custom", "ml", "ml50", "ml100" and "mucape" (see  below for details)
    :type mode: str
    :param virtual: enables the virtual temperature correction. Default is True.
    :type virtual: bool
    :param start_t: the start temperature (°C) of the parcel when ``mode`` is "custom"
    :type start_t: number
    :param start_td: the start dewpoint (°C) of the parcel when ``mode`` is "custom"
    :type start_td: number
    :param start_p: the start pressure (hPa) of the parcel when ``mode`` is "custom"
    :type start_p: number
    :param top_p: the top pressure (hPa) of the start layer when ``mode`` is "ml" or "mucape". Cannot be used together with ``layer_depth``.
    :type top_p: number
    :param bottom_p: the bottom pressure (hPa) of the start layer when ``mode`` is "ml" or "mucape". When it is None the pressure layer starts at the surface.
    :type bottom_p: number
    :param layer_depth: the depth of the start layer (hPa) when ``mode`` is "ml" or "mucape". Cannot be used together with ``top_p``. When none of ``top_p``, ``bottom_p`` and ``layer_depth`` is specified, it is implicitly set to 100 when ``mode`` is "ml" and to 300 when ``mode`` is "mucape".
    :type layer_depth: number
    :param stop_at_el: makes all parcel computations stop at the Equilibrium Level (EL). Default is False.
    :type stop_at_el: bool
    :param comp_top: enables the computation of the Cloud Top Level (TOP). Default is False. Ignored when ``stop_at_el`` is enabled.
    :type comp_top: bool
    :param el_area: enables the computation of the parcel area above the Equilibrium Level (EL) that can then plotted onto the thermodynamic diagram. Default is False. Ignored when ``stop_at_el`` is enabled.
    :type el_area: bool    
    :rtype: dict
    
    It returns a dict containing all the data to plot the parcel path, buoyancy areas and related data into a thermodynamic diagram.

    All the input values must be specified in °C (temperature) and hPa (pressure) units. The actual start condition is determined by ``mode``:

    * **"surface"**: the parcel ascends from the surface, i.e. the lowest point of the profile. E.g.:

        .. code-block:: python
            
            mv.thermo_parcel_path(prof, mode="surface")

    * **"custom"**: the parcel ascends from a given temperature, dewpoint and pressure. E.g.:
    
        .. code-block:: python
            
            mv.thermo_parcel_path(prof, mode="custom",
                start_t=27.2, 
                start_td=21.8,
                start_p=998)

    * **"ml"**: the parcel ascends from the following mean start condition in a given layer:
  
        * temperature: determined from the mean potential temperature of the layer
        * dew point: the mean value in the layer
        * pressure: the surface value
 
     The layer is specified with the combination of ``top_p``, ``bottom_p``, ``layer_depth``. When ``bottom_p`` is None the pressure layer starts at the surface. E.g.: 
    
        .. code-block:: python
            
            mv.thermo_parcel_path(prof, mode="ml", layer_depth=150)

     When none of ``top_p``, ``bottom_p`` and ``layer_depth`` is specified, ``layer_depth`` is implicitly set to 100. E.g.

         .. code-block:: python
            
            # these calls are equivalent
            mv.thermo_parcel_path(prof, mode="ml", layer_depth=100)
            mv.thermo_parcel_path(prof, mode="ml")

    * **"ml50"**: the parcel ascends from the mean start condition in the lowest 50 hPa layer above the surface. The start condition is determined similarly to "ml". 
    * **"ml100"**: the parcel ascends from the mean start condition in the lowest 100 hPa layer at the surface. The start condition is determined similarly to "ml". 
    * **"mucape"**: the parcel ascends from the most unstable condition. This is the default ``mode``. To determine "mucape", a parcel is started from all the points along the profile in the specified pressure layer. The start level of the parcel that results in the highest CAPE value will define the most unstable start condition. The layer is specified with the combination of ``top_p``, ``bottom_p``, ``layer_depth``.  When ``bottom_p`` is None the pressure layer starts at the surface. E.g.
        
        .. code-block:: python

            mv.thermo_parcel_path(prof, mode="mucape", layer_depth=200)
        
     When none of ``top_p``, ``bottom_p`` and ``layer_depth`` is specified, ``layer_depth`` is implicitly set to 300. E.g.

         .. code-block:: python
            
            # these calls are equivalent
            mv.thermo_parcel_path(prof, mode="mucape", layer_depth=300)
            mv.thermo_parcel_path(prof, mode="mucape")
            mv.thermo_parcel_path(prof)


    :func:`thermo_parcel_path` returns a dict to describe all the parameters related to the ascend of the parcel. The members of this dict are as follows (temperature values are in °C and pressure values are in hPa) :

    * "path": path of the parcel. It is itself a dict with two members: t and p, both containing a list of values.

    * "area": positive and negative buoyancy areas between the parcel path and the profile. It is a list of dictionaries describing the areas.

    * "cape": value of the CAPE (Convective Available Potential Energy)  (J/kg)

    * "cin": value the CIN (Convective Inhibition) (J/kg)

    * "li": the Lifted Index (K)

    * "lcl": Lifted Condensation Level. It is a definition with two members: t and p. If no LCL exists it is set to None.

    * "lfc": Level of Free Convection. It is a definition with two members: t and p. If no LFC exists it is set to None.

    * "el": Equilibrium Level. It is a definition with two members: t and p. If no EL exists it is set to None.

    * "top": Cloud Top Level. It is a definition with two members: t and p. If no TOP exists it is set to None.

    * "start": start conditions of the parcel with four members: mode, t, td and p.


.. mv-minigallery:: thermo_parcel_path