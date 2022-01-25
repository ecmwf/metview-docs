.. _version_5.4_updates:

Version 5.4 Updates
///////////////////


**Not externally released.**

* Became  metview/default and metview/new at ECMWF on 2019-01-29 (Linux desktops, ecgate, lxc, lxop)

-  **At ECMWF:**

   -  Installed **2019-01-17**

   -  Built
      with **Magics** `3.3.1 <https://software.ecmwf.int/wiki/display/MAGP/Latest+News>`__

   -  Built
      with **ecCodes** `2.10.1 <https://confluence.ecmwf.int/display/ECC/ecCodes+version+2.10.0+released>`__

   -  Built
      with **ODB_API** version `0.18.1 <https://software.ecmwf.int/wiki/display/ODBAPI/Latest+news>`__

   -  Built
      with **emoslib** `000459 <https://confluence.ecmwf.int/pages/viewpage.action?pageId=78283744>`__

   -  Built with **mir 1.1.1**

**Highlights:**

-  **interpolation**: this is the first version of Metview to use
   **mir** as its interpolation library **by default** when running at
   ECMWF. The following functions are affected:

   -  retrieve()

   -  read()

   -  divrot()

   -  divwind()

   -  uvwind()

-  and their corresponding icons:

   -  *Mars Retrieval*

   -  *Grib Filter*

   -  *Rotational or Divergent Wind*

-  The environment variable METVIEW_MARS_INTERP can be set to either MIR
   or EMOS in order to change this behaviour before running Metview.

-  In order to facilitate running and comparing both interpolation
   methods within a single Metview session, there also exist separate
   versions of the above functions, e.g. retrieve_mir() and
   retrieve_emos(), which will use the interpolation package in their
   name and will not be affected by the environment variable.
   Corresponding to these functions are also icons, which are available
   from Metview's user interface.

-  Please note that the existence of these specialised functions is
   temporary - operational scripts should not depend on them.

-  We currently do not have an externally available version of Metview
   that includes mir.
