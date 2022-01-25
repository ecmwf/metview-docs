.. _version_5.9_updates:

Version 5.9 Updates
///////////////////

Version 5.9.1
=============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2020-07-22
* Became metview/new at ECMWF on 2020-07-22 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2020-07-22**

   -  Built
      with **Magics** `4.4.1 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.18.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.18.0+released>`__

   -  Built
      with **ODB_API** version `0.19.4 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Includes
      version `1.4.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**BUFR Filtering:**

-  fixed issue where geopoints were sometimes generated with a mixture
   of spaces and tabs; now in these cases, only tabs are used

**MARS access:**

-  fixed issue where fdb5 was not being directly accessed when Metview
   is built at ECMWF

**Meteogram:**

-  fixed issue where
   the :ref:`Meteogram <meteogram_icon>`
   module could crash if given a large number of stations (> 20 or so)

**Plotting:**

-  fixed issue in the :ref:`Geographical
   View <geoview_icon>`
   icon where some of the pre-defined areas in polar stereographic
   projection were not correctly plotted

**ecCharts:**

-  the :ref:`ECCHARTS <eccharts_icon>`
   module is now built by default; previously it was only built if the
   UI was built

**Tests:**

-  fixed a geopoints test that was failing with clang compilers

Version 5.9.0
=============

* Externally `released <https://software.ecmwf.int/wiki/display/METV/Releases>`__\  on 2020-06-24
* Became metview/new at ECMWF on 2020-06-24 (Linux desktops, ecgate, lxc, lxop)


-  **At ECMWF:**

   -  Installed **2020-06-24**

   -  Built
      with **Magics** `4.4.0 <https://confluence.ecmwf.int/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.18.0 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.18.0+released>`__

   -  Built
      with **ODB_API** version `0.19.4 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Includes
      version `1.4.2 <https://confluence.ecmwf.int/display/METV/Metview+Python+Release+Notes>`__ of
      the Python interface

**Plotting:**

-  support for more grids, with the latest versions of ecCodes (2.18.0)
   and Magics (4.4.0):

   -  Mercator grid supported for processing and plotting, including
      Cursor Data

      .. image:: /_static/release/version_5.9_updates/image1.png
            :width: 3.50048in
            :height: 2.60417in

   -  Lambert Azimuthal Equal Area grid, including on oblate spheroid,
      supported for plotting

      .. image:: /_static/release/version_5.9_updates/image2.png
            :width: 3.91234in
            :height: 2.60417in

   -  Lambert Conformal grid supported for processing and plotting,
      including Cursor Data

      .. image:: /_static/release/version_5.9_updates/image3.png
            :width: 3.82348in
            :height: 2.60417in

   -  Polar Stereographic grid supported for plotting, including Cursor
      Data

      .. image:: /_static/release/version_5.9_updates/image4.png
            :width: 4.03625in
            :height: 2.60417in

-  :ref:`Input
   Visualiser <input_visualiser_icon>`
   now accepts vectors (Macro langauge) and numpy arrays (Python) for
   the following parameters:
   input_x_values, input_y_values, input_x2_values, input_y2_values,
   input_longitude_values, input_latitude_values, input_values. For
   arrays with more than 10,000 or so entries, this can provide a speed
   up of hundreds of times compared to using lists. Example plot using
   the Binning options of the Input Visualiser:

      .. image:: /_static/release/version_5.9_updates/image5.png
         :width: 3.60577in
         :height: 2.60417in

-  Improved step string in the title of a FLEXPART plot using
   the flexpart_build_title() function - for example, a step of 90
   minutes will now be rendered as "1h 30m" in the title

**BUFR:**

-  fixed occasional crash in the :ref:`Observation
   Filter <obsfilter_icon>`
   when used with TEMP data

**Fortran:**

-  Metview's two remaining Fortran-based modules, `Potential
   Temperature <https://confluence.ecmwf.int/display/METV/Potential+Temperature>`__
   and :ref:`Spectra <spectra_icon>`,
   have now been re-written in C++, meaning that a Fortran environment
   is no longer required in order to use them. These modules were
   disabled in Metview's conda builds in order to avoid the need for
   Fortran; from this release onwards, they will be available in the
   conda versions

**Macro/Python:**

-  function direction() now handles missing values properly -
   see :ref:`Fieldset
   Functions <macro_fieldset_fn>`

-  function univertint() now supports pressure levels as input

-  added function filetype() to return the internal Metview type of a
   given file

-  Macro-based user interfaces can now use the help_script parameter for
   any input type

**macOS:**

-  fixed issue seen on macOS where the area selection tool in
   the :ref:`Geographical
   View <geoview_icon>`
   icon editor could cause a crash

-  fixed issue seen on macOS where using the :ref:`Cross Section
   View <mxsectview_icon>`
   and related icons multiple times could cause instability

**Gallery:**

-  added new examples for ensemble data handling:

   -  :ref:`ENS Stamp Map
      Example <gallery_ens_stamp>`

   -  :ref:`ENS Spaghetti Map
      Example <gallery_ens_spag>`

   -  :ref:`CDF Curve
      Example <gallery_cdf_curve>`

-  added new example using
   the :ref:`Spectra <spectra_icon>`
   module:

   -  :ref:`Spherical Harmonics Spectrum
      Example <gallery_spectra>`
