.. _installation_faq:

Installation FAQ
////////////////


.. note::
   
   We welcome any feedback and will add frequently asked questions to future editions of this document. To report bugs or ask for help please visit the `Software
   Support <https://confluence.ecmwf.int/display/SUP/Home>`__ home page.


Q: Build fails with message relating to the file macro_built_in_functions.txt OR Metview fails to start because it cannot connect to port/host
----------------------------------------------------------------------------------------------------------------------------------------------

This issue can occur, often on laptops, when the IP loopback is not
set up. The quickest way to fix this is to set the environment
variable::

   METVIEW_LOCALHOST=1

and then resume the build. This variable will also need to be set
before starting Metview.

On OpenSuSE 12 & 13 systems, a better solution is to go into Yast >
Network Settings > Hostname/DNS  : the option Assign Hostname to
Loopback IP should be checked.

Q: Problems linking with Intel tools
----------------------------------------

We've had a report that when using the Intel compiler, the linking of
the DataCoverage module produces errors with defined symbols from
libemos. This can be because the Intel C++ compiler does not know
that it needs to link with the Intel Fortran libraries (a few of
Metview's modules use some Fortran code). A solution is to add the
following to your CMake command when configuring
Metview::
   
   -DCMAKE_EXE_LINKER_FLAGS="-L[ifort8.1path]/lib -lifcore"

where [ifort8.1path] is replaced by the path to where the Intel
fortran libraries are.

Q: How should I build ecCodes for Metview?
-------------------------------------------------

If you plan to use Metview's interactive GRIB and BUFR examiner
tools, then you must ensure that ecCodes is built with thread safety
enabled. Do this by passing the following option to CMake::

   -DENABLE_ECCODES_THREADS=ON                                        

Q: I get the following error message when I try to read GRIB data in Metview: “ecCodes ERROR : Unable to find boot.def”
--------------------------------------------------------------------------------------------------------------------------

It is possible to check a ecCodes installation from the command line
by finding a GRIB file and typing::

   grib_ls <path/to/grib/file>

If this error message appears, then ecCodes is not properly
installed. One option, which does not require a rebuild of
ecCodes, is to change the value of the environment variable
GRIB_DEFINITION_PATH. The command *grib_info* will tell you the
current value. Normally, it should be set to: /usr/local/share/eccodes/definitions, 
but you should first check that this directory exists.

Q: I get this message at CMake time: "CMake Error at cmake/ecbuild_download_resource.cmake:57 (math): math sub-command EXPR option "+" is unknown."
---------------------------------------------------------------------------------------------------------------------------------------------------

This error has occasionally been seen on some systems. It comes from trying to download
land-sea masks that are used only in specific cases when regridding data, so they are
not necessary in most cases and the download can be disabled by rebuilding with

   -DENABLE_MIR_DOWNLOAD_MASKS=OFF
