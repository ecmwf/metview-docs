.. _build_from_source:

Build from source
//////////////////

.. note::

    Note: this guide provides information on how to build Metview from 
    source. Please consider installing a pre-built version, as         
    described in the :ref:`Installation <install>` 
    page.                                                              

Overview
========

Metview uses **CMake** for its compilation and installation, in line
with all other ECMWF packages. Note that there are other ways to install
Metview from pre-built binary packages, or from a source bundle that
includes many dependencies.
See `Releases <https://confluence.ecmwf.int/display/METV/Releases>`__.

CMake installation instructions
===============================

The `CMake <http://cmake.org>`__ build system is used to build ECMWF
software. The build process comprises two stages:

1. CMake runs some tests on the system and finds out if required
   software libraries and headers are available. It uses this
   information to create native build tools (e.g. Makefiles) for the
   current platform.

2. The actual build can take place, for example by typing 'make'.

Prerequisite
============

To install any ECMWF software package, CMake needs to be installed on
your system. On most systems it will be already installed or this can be
done through the standard package manager to install software. For
further information to install CMake see

   http://www.cmake.org/cmake/help/install.html

Directories
===========

During a build with CMake there are three different directories
involved: The **source dir**, the **build dir** and the **install dir**.

+-----------+------------------------------------------------+-------------+
| Directory | Use                                            | Example     |
+===========+================================================+=============+
| Source    | Contains the software's source code. This is   | /tmp/src/   |
|           | where a source tarball should be extracted to. | sw-package  |
+-----------+------------------------------------------------+-------------+
| Build     | Configuration and compiler outputs are         | /tmp/build/ |
|           | generated here, including libraries and        | sw-package  |
|           | executables.                                   |             |
+-----------+------------------------------------------------+-------------+
| Install   | Where the software will actually be used from. | /usr/local  |
|           | Installation to this directory is the final    |             |
|           | stage.                                         |             |
+-----------+------------------------------------------------+-------------+

Of these, the source and build directories can be anywhere on the
system. The installation directory is usually left at its default, which
is /usr/local. Installing software here ensures that it is automatically
available to users. It is possible to specify a different installation
directory by adding -DCMAKE_INSTALL_PREFIX=/path/to/install/dir to the
CMake command line.

.. note::

    ECMWF software does **not** support in-source builds. Therefore    
    the build directory **cannot** be (a subdirectory of) the source   
    directory.                                                         

Quick Build Example
===================

Here is an example set of commands to set up and build a software
package using default settings. More detail for a customised build is
given below.

.. code-block:: bash

    # unpack the source tarball into a temporary directory                                                                                    
    mkdir -p /tmp/src                                                                                                                      
    cd /tmp/src                                                                                                                              
    tar xzvf software-version-Source.tar.gz                            
                          
    # configure and build in a separate directory                                                                                       
    mkdir -p /tmp/build                                                                                                                     
    cd /tmp/build                                                                                                                           
    cmake /tmp/src/software-version-Source                                                                                                  
    make                                                               

On a machine with multiple cores, compilation will be faster by
specifying the number of cores to be used simultaneously for the build,
for example::

    make -j8                                                           

If the make command fails, you can get more output by typing::

    make VERBOSE=1                                                     

The software distribution will include a small set of tests which can
help ensure that the build was successful. To start the tests, type::

    ctest                                                              


As before if you have multiple cores, you can run the tests in parallel
by::

    ctest -j8                                                          

.. note::

    Some projects might not be set up to run tests in parallel. If you 
    experience test failures, run the tests sequentially.              

If the tests are successful, you can install the software::

    make install                                                       

General CMake options
=====================

Various options can be passed to the CMake command. The following table
gives an overview of some of the general options that can be used.
Options are passed to the cmake command by prefixing them with **-D**,
for example **-DCMAKE_INSTALL_PREFIX=/path/to/dir**.

+----------------------+--------------------------+-----------------------+
| CMake Option         | Description              | Default               |
+======================+==========================+=======================+
| CMAKE_INSTALL_PREFIX | where to install the     | /usr/local            |
|                      | software                 |                       |
+----------------------+--------------------------+-----------------------+
| CMAKE_BUILD_TYPE     | to select the type of    | RelWithDebInfo        |
|                      | compilation:             | (release with debug   |
|                      |                          | info)                 |
|                      | -  Debug                 |                       |
|                      |                          |                       |
|                      | -  RelWithDebInfo        |                       |
|                      |                          |                       |
|                      | -  Release               |                       |
|                      |                          |                       |
|                      | -  Production            |                       |
+----------------------+--------------------------+-----------------------+
| CMAKE_CXX_FLAGS      |  Additional flags to     |                       |
|                      | pass to the C++ compiler |                       |
+----------------------+--------------------------+-----------------------+
| CMAKE_C_FLAGS        | Additional flags to pass |                       |
|                      | to the C compiler        |                       |
+----------------------+--------------------------+-----------------------+
| CMAKE_Fortran_FLAGS  | Additional flags to pass |                       |
|                      | to the Fortran compiler  |                       |
+----------------------+--------------------------+-----------------------+

The C, C++ and Fortran compilers are chosen by CMake. This can be
overwritten by setting the environment variables CC, CXX and F77, before
the call to cmake, to set the preferred compiler. Further the
variable CMAKE_CXX_FLAGS can be used to set compiler flags for
optimisation or debugging. For example, using::
    
     CMAKE_CXX_FLAGS="-O2 -mtune=native" 
    
sets options for better optimisation. 

Finding support libraries
-------------------------

If any support libraries are installed in non-default locations, CMake
can be instructed where to find them by one of the following
methods. First, the option CMAKE_PREFIX_PATH can be set to a
colon-separated list of base directories where the libraries are
installed, for example::

    -DCMAKE_PREFIX_PATH=/path/where/my/sw/is/installed. 

CMake will check
these directories for any package it requires. This method is therefore
useful if many support libraries are installed into the same location.

Troubleshooting
===============

Debugging configure failures
----------------------------

If CMake fails to configure your project, run with debug logging first::

    cmake -DECBUILD_LOG_LEVEL=DEBUG [...] /path/to/source              

This will output lots of diagnostic information (in blue) on discovery
of dependencies and much more.

Requirements to build Metview
=============================

The following table lists the dependencies Metview requires to be built
from source. Please note, if you install these package from source you
also might have to install the respective "-devel" packages.

**Compilers**

.. list-table::
   :widths: 50 50

   * - C++ 
     - http://gcc.gnu.org/ 
   * - Fortran
     - http://gcc.gnu.org/fortran/  
    
**Utilities**

.. list-table:: 
   :widths: 25 75

   * - make 
     - http://www.gnu.org/software/make/


**Third party packages** 
*(best installed through system package manager.)*

.. list-table:: 
   :widths: 25 35 40
   :header-rows: 1
   
   * - Package
     - URL
     - Notes
   * - Qt5/Qt6 
     - http://www.qt.io/
     - if Metview's user interface is required. Note that on some systems it is also necessary to install the libQtWebKit-devel development package (it may have different names on different systems)
   * - gdbm
     - http://www.gnu.org.ua/software/gdbm/
     - 
   * - bash 
     - https://www.gnu.org/software/bash/
     - 
   * - netcdf 4
     - http://www.unidata.ucar.edu/software/netcdf/
     - Please note: You also will need to install `HDF5 <https://www.hdfgroup.org/HDF5/>`__ and the `legacy C++ interface <https://www.unidata.ucar.edu/downloads/netcdf/index.jsp>`__ if you wish to un the Single Column Model from Metview (ECMWF only)
   * - curl
     -
     -
   * - bison
     -
     -
   * - flex
     -
     -


**ECMWF libraries**


.. list-table:: 
   :widths: 25 35 40
   :header-rows: 1

   * - Package
     - URL
     - Notes
   * - ecCodes
     - `ecCodes Home <https://confluence.ecmwf.int/display/ECC/ecCodes+Home>`__
     - 
   * - magics
     - `Magics <https://confluence.ecmwf.int/display/MAGP/Magics>`__
     - if plotting support is needed. Note that Magics should be configured with the **-DENABLE_METVIEW=ON** option. For a 'pure batch' installation of Metview with no user interface, it is possible to supply Magics no user interface, it is possible to supply Magics with the option **-DENABLE_METVIEW_NO_QT=ON**
   * - odc
     - `ODC Home <https://confluence.ecmwf.int/display/ODC/ODC+Home>`__ `ODB-API Home <https://confluence.ecmwf.int/display/ODB/ODB+Home>`__
     - if ODB support needed  


CMake options used in Metview
=============================

CMake options are passed to the cmake command by prefixing them with
**-D**, for example **-DENABLE_UI=OFF**.

.. list-table:: 
   :widths: 25 35 40
   :header-rows: 1

   * - CMake option
     - Description
     - Default
   * - ENABLE_UI
     - enables the Qt-based user interface
     - ON
   * - ENABLE_PLOTTING
     - enables plotting capabilities using `Magics <https://confluence.ecmwf.int/display/MAGP>`__
     - ON
   * - ENABLE_METVIEW_FORTRAN
     - enables inline Fortran code inside macros
     - OFF (since Metview 5.10.2)
   * - ENABLE_MARS 
     - enables MARS access (not required if using through the `Web API <https://confluence.ecmwf.int/display/METV/Using+the+MARS+Web+API+from+Metview>`__)
     - OFF
   * - MARS_LOCAL_HOME
     - sets the path to where local MARS is installed
     - 
   * - ENABLE_ODB
     - enables processing and plotting of ODB data
     - OFF
   * - ENABLE_MARS_ODB
     - enables ODB capabilities in MARS client
     - OFF
   * - ENABLE_USAGE_LOG
     - enables logging of Metview startup calls
     - OFF
   * - LOG_DIR
     - path to where to log the Metview startup calls
     - 
   * - METVIEW_SCRIPT
     - name of the generated Metview startup script 
     - metview
   * - EXTRA_CONFIG_PATH
     - path to optional directory containing metview_local script files
     - 
   * - ENABLE_QT_DEBUG
     - outputs additional log messages from Qt-based modules
     - OFF
   * - EXTRA_TITLE
     - build-specific title to add to the log entries
     - 
   * - ENABLE_INPE
     - enables INPE modules
     - OFF

   * - ENABLE_MIR_DOWNLOAD_MASKS
     - whether to download land-sea masks for use with certain interpolation methods
     - ON

**Path options - only required when support libraries are not installed in default locations**

.. list-table:: 
   :widths: 25 35 40
   :header-rows: 1

   * - CMake option
     - Description
     - Default
   * - ECCODES_PATH
     - path to where ecCodes has been installed
     - 
   * - MAGICS_PATH
     - path to where `Magics <https://confluence.ecmwf.int/display/MAGP/Magics>`__ has been installed
     - Only required if plotting is enabled
   * - NETCDF_PATH
     - path to where netCDF has been installed
     - 
   * - ODC_PATH
     - path to where ODC has been installed
     - Only required if ODB is enabled
   * - ODB_PATH
     - path to where the original ODB has been installed 
     - Only required if ODB is enabled
   * - FDB_PATH
     - path to where fdb has been installed
     - Only required if MARS is enabled
   * - FLEXTRA_PATH
     - path to where the FLEXTRA executable has been installed
     - See :ref:`FLEXTRA <the_flextra_interface>` for more details
