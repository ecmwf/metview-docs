.. _using_flexpart_with_metview:

Using FLEXPART with Metview
###########################

This tutorial explains how to use the FLEXPART Lagrangian dispersion model within Metview

.. note::

  Please note that this tutorial requires Metview version **5.0** or later.

Preparations
************

First start Metview; at ECMWF, the command to use is metview (see `Metview at ECMWF <https://confluence.ecmwf.int/display/METV/Metview+at+ECMWF>`_ for details of Metview versions). 
You should see the main Metview desktop popping up.

The icons you will work with are already prepared for you - please download the following file:

.. list-table::

  * - `flexpart_tutorial.tar.gz <http://download.ecmwf.org/test-data/metview/tutorial/flexpart_tutorial.tar.gz>`_

and save it in your ``$HOME/metview`` directory. 
You should see it appear on your main Metview desktop, from where you can right-click on it, then choose **execute** to extract the files.

Alternatively, if **at ECMWF** then you can copy it like this from the command line::

  cp -R /home/graphics/cgx/tutorials/flexpart_tutorial ~/metview
  
You should now (after a few seconds) see a *flexpart_tutorial* folder. 
Please open it up.

The input data
**************

The input data is already prepared for you and is located in folder 'Data'. 
You will find a :ref:`FLEXPART Prepare <flexpart_prepare_icon>` icon that was used to generate the data in folder 'Prepare'. 
The corresponding macro code can also be found there.

You do not need to run the data preparation. 
However, if you wish to do so please note that it requires MARS access and you must set the **Output Path** parameter accordingly.

Tutorials
**************

.. toctree::
    :maxdepth: 1

    forward/index
    flexpart_backward_simulation_with_residence_times
    flexpart_plume_trajectories
