.. _installation_guide_for_metview_4.4_and_below:

Installation Guide for Metview 4.4 and below
////////////////////////////////////////////

Metview

Exported on Feb 17, 2022

Table of Contents
=================

1 Overview `3 <#overview>`__

2 Requirements `4 <#requirements>`__

2.1 Platforms `4 <#platforms>`__

2.2 ECMWF support libraries `4 <#ecmwf-support-libraries>`__

2.3 Required third-party software `4 <#required-third-party-software>`__

2.4 Compilation environment `5 <#compilation-environment>`__

2.5 Notes for installers of Metview 3
`5 <#notes-for-installers-of-metview-3>`__

3 Compilation and installation `6 <#compilation-and-installation>`__

3.1 Generating the Makefiles with configure
`6 <#generating-the-makefiles-with-configure>`__

3.2 Compiling the code `7 <#compiling-the-code>`__

3.3 Testing your build `7 <#testing-your-build>`__

3.4 Installing Metview `7 <#installing-metview>`__

3.5 FAQ `7 <#faq>`__

Overview
========

Metview uses the GNU *autotools* for its installation. These are the
standard installation tools for most free and commercial software
packages to date on Unix.

*Autotools’* main task is to generate Makefiles for the desired platform
on which Metview will be used. This is necessary, because the various
platforms differ from each other in various ways, such as compiler
options and library/include paths.

*Autotools* themselves do not need to be installed on the system of the
customer. Supplied is a Unix shell script called *configure* which is
executed by the person installing Metview. The script will run some
tests on the customer's system to find out if required third-party
software libraries are available and notes their locations (paths).
Based on this information the script produces the Makefiles needed to
compile and install Metview.

Metview can be built in either 32- or 64-bit mode. This is handled by
either leaving it to your system defaults, or by passing the appropriate
compilation flags to the *configure* script (see Compilation and
installation).

Requirements
============

Platforms
---------

At ECMWF, openSUSE 11.3 and SLES 11 Linux systems (64bit) were used for
testing Metview. A 64-bit version was also built for AIX. Ubuntu 10.4
was found to have a defective OpenMotif library, which made Metview's
user interface inoperable, but one user reported that installing an
update fixed this problem.

ECMWF support libraries
-----------------------

All required support libraries from ECMWF are available without charge
from the `Software
Support <https://confluence.ecmwf.int/display/SUP/Home>`__ web page.

To produce plots, Magics must be installed:

-  Magics++ (2.18.1 or higher is required)

   -  should be configured with the –-enable-metview option

   -  for a 'pure batch' installation of Metview with no user interface,
      it is possible to supply Magics with the options –-enable-metview
      --disable-qt

The following two libraries need to be installed (both are required,
even if you will not handle GRIB or BUFR data):

-  GRIB_API (1.9.9 or higher)

   -  see the `Installation
      FAQ <https://confluence.ecmwf.int/display/METV/Installation+FAQ>`__
      for details of building GRIB_API for Metview, as this contains
      some important information

-  EmosLib

   -  version 381 or higher

   -  compiled with double floating point precision (answer “y” to “Do
      you want 64-bit reals? [y,n]”)

   -  must be built with GRIB_API support

   -  64-bit versions should be built with *-fPIC* compilation flag

   -  *Remember to set the ARCH environment variable before building
      Emoslib, e.g.* export ARCH=linux\ *.*

.. note::

    **Note**                                                           
                                                                       
    The latest versions of EmosLib depend on GRIB_API, therefore       
    GRIB_API must be installed before EmosLib.                         

Required third-party software
-----------------------------

First, ensure that all third-party libraries required by Magics and
GRIB_API are installed (this is likely to have been fulfilled already
unless Magics was built on another system and copied across).

Additionally, the following list of software should be installed on your
system before you try to install Metview. If you use a package manager,
such as RPM, to install software make sure to include the corresponding
development packages with the header files. The *configure* script will
test for these libraries and give error messages if one of them is
missing.

-  | Qt (4.6.2 or later) if building the user interface (default=yes)
   | *note that on some systems it is also necessary to install the
     libQtWebKit-devel development package (it may have different names
     on different systems)*

-  | NetCDF library with C++ interface
   | (http://www.unidata.ucar.edu/software/netcdf/)

-  OpenMotif

-  gdbm

-  ImageMagick (Metview uses the convert command during the build
   process)

-  ksh - the Korn Shell is used by Metview's startup script and some
   other internal scripts

If you wish to access OPERA radar BUFR data, then you will need to also
install the proj4 development libraries.

Compilation environment
-----------------------

Any C++ Compiler which supports features required for the ANSI C++
standard from 1998 (STL, namespaces, templates) should work with
Metview. At ECMWF we tested GCC’s *g++* 4.1, 4.3 and 4.5 successfully. A
Fortran compiler is required to build some of Metview's modules. It will
also be required to build EmosLib, for which *Cray pointer* support is
required. At ECMWF the *Portland Pgf90* compiler 7.2 and *GFortran* 4.1
and newer were tested successfully on Linux platforms, and Xlf was used
on AIX.

Notes for installers of Metview 3
---------------------------------

If you have installed Metview 3 before, then here are some things to
note. Metview 4 does not use directly OpenGL for its on-screen graphics;
therefore, it is not necessary to build your own Mesa library anymore.
However, Metview 4 does not come with its own Emoslib; therefore, it
will be necessary to install your own.

Metview 4 can be installed side-by-side with an existing Metview 3
installation. However, note that the default startup script will be

   /usr/local/bin/metview

so make sure this will not clash with an existing installation. See
Compilation and installation on page 6 for details of flags which will
allow you to change this.

 Compilation and installation
============================

To compile and install Metview, the installer must first unpack the
\*.tar.gz file, provided by ECMWF, to a temporary location:

   tar -xzvf Metview-4.3.4.tar.gz

Generating the Makefiles with configure
---------------------------------------

After changing into the unpacked Metview directory, the user should run
the configure script. The script gives feedback on what requirements are
fulfilled and what software is still required. Table 1 gives an overview
of some of the different options of configure. More options of the
script can be listed by typing configure --help in the console. The
default (without any options) will prepare Metview to be built and then
installed into /usr/local/. The startup script will then, by default, be
/usr/local/bin/metview. In case of clashes with another Metview
installation, the name of this script can be changed.

+----------------+------------------------------------------+----------+
| **Option**     | **Explanation**                          | **D      |
|                |                                          | efault** |
+================+==========================================+==========+
| --help         | Outputs all options of configure         |          |
+----------------+------------------------------------------+----------+
| --prefix=\     | Directory into which Metview will be     | /u       |
|  */your/path/* | installed                                | sr/local |
+----------------+------------------------------------------+----------+
| --enable-debug | Add debug information to assist          | no       |
|                | debuggers                                |          |
+----------------+------------------------------------------+----------+
| --wi           | Provide the location where Emoslib is    | /usr/l   |
| th-emos-librar | installed                                | ocal/lib |
| ies=\ *<path>* |                                          |          |
+----------------+------------------------------------------+----------+
| --wit          | Provide the name of the Emoslib library  | emosR64  |
| h-emos-libname |                                          |          |
| =\ *<libname>* |                                          |          |
+----------------+------------------------------------------+----------+
| --with-grib-   | Provide the location where GribAPI is    | /u       |
| api=\ *<path>* | installed                                | sr/local |
+----------------+------------------------------------------+----------+
| --with-net     | Provide the location where NetCDF is     | from     |
| cdf=\ *<path>* | installed                                | system   |
+----------------+------------------------------------------+----------+
| --enable-ui    | Disable this and no user interface will  | yes      |
|                | be built; only macros can be run from    |          |
|                | the command line                         |          |
+----------------+------------------------------------------+----------+
| -              | Enables the generation of plots          | yes      |
| -enable-magics |                                          |          |
+----------------+------------------------------------------+----------+
| --enab         | Enables access to the MARS archive       | no       |
| le-mars-access |                                          |          |
+----------------+------------------------------------------+----------+
| --enab         | Enables processing of OPERA radar data – | yes      |
| le-opera-radar | requires proj4 to be installed           |          |
+----------------+------------------------------------------+----------+
| --wi           | Name of the generated Metview startup    | metview  |
| th-startup-scr | script                                   |          |
| ipt=\ *<name>* |                                          |          |
+----------------+------------------------------------------+----------+

Table 1: Options of the configure scripts. Typing configure -h gives a
complete listing.

 

The C, C++ and Fortran compilers are chosen by configure. This can be
overwritten by setting the variables **CC**, **CXX** and **F77** on the
configure command line to the preferred compiler.

The most important option is --prefix. Setting the prefix defines where
your Metview files will be installed.

Compilation flags (e.g. to determine optimisation levels or 32-bit or
64-bit compilation or options for debugging) can be specified either
through environment variables or passed as options to configure. For
instance, depending on your compiler, you could force 32-bit compilation
with the CXXFLAGS variable, either through the environment:

   export CXXFLAGS=-m32

   ./configure

or else passed to configure directly:

   ./configure CXXFLAGS=-m32

(In practice, you would also need to set CFLAGS and FCFLAGS).

Compiling the code
------------------

After the configure script has run successfully, the user can compile
the library by typing make in the same directory.

Testing your build
------------------

The Metview distribution contains a directory called test in which some
Metview macros are run when make check is invoked. This will give you a
first indication of whether your build was successful.

The build process will have created a start-up script (default name
metview) in your root build directory. If you have built the UI
(default=yes), then running this script will create a menu bar from
which you should click the **MetviewUI** button to launch Metview. This
will use your locally-built files. You should see a folder called
'Getting Started' which contains some example icons and data files.

Installing Metview
------------------

Once the build and tests have been successfully completed, the command
*make install* copies Metview with all its associated files into the
correct location on the system. Administrator permission might be
required, depending on the installation directory. You might want to run
make -n install first, which will show you what will be installed where,
without performing any changes to your system.

To free space, the temporary unpacked source directory can be cleaned of
the object files with *make clean* after a successful installation.

 FAQ
---

**Please see the**\ `Installation
FAQ <https://confluence.ecmwf.int/display/METV/Installation+FAQ>`__\ **for
frequently asked questions about installing and testing Metview.**
