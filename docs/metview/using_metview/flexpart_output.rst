.. _flexpart_output:

FLEXPART output
///////////////


Outputs
=======

Metview runs FLEXPART in a temporary directory. Having finished the
simulation Metview converts and rename the output files and move them
into the **Output Path** directory specified in the :ref:`FLEXPART
Run <flexpart_run_icon>` icon.
The different output types are handled in a different way.

Gridded outputs
===============

Gridded outputs are converted to GRIB using local GRIB definitions built
into Metview.

FLEXPART GRIB files have their own local section (Section 2) containing
additional information about the given field and the FLEXPART simulation
itself. The snapshot below taken from Metview's Grib Examiner shows the
currently defined set of keys in Section 2.

.. image:: /_static/ug/flexpart_output/image1.png
   :width: 5.90069in
   :height: 1.66708in

.. admonition:: Handling FLEXPART GRIB output
                                                    
    To plot a particular parameter and level we need to *filter* the   
    desired fields from the resulting FLEXPART output GRIB file.       
    Unfortunately, Metview's *Grib Filter* icon cannot handle these    
    files (partly due to the local GRIB definition they use) so we     
    need to use *Macro* with some FLEXPART-related command to deal     
    with this problems. See `Using FLEXPART with Metview <https://confluence.ecmwf.int/display/METV/Using+FLEXPART+with+Metview>`__ for details.                                                       

Concentration fields
--------------------

Concentration fields are only produced for *forward* simulations when
**Output Field Type** is set to **conc** or **both** in :ref:`FLEXPART
Run <flexpart_run_icon>`.

The output filename is:

   conc_sSSS.grib

where SSS is the species index (starts from 1) with leading zeros. The
actual field type and units are based on the **Receptor Units** settings
in the :ref:`FLEXPART
Run <flexpart_run_icon>` icon.

+--------------------+------------------+----------+--------+---------+
| Options in         | Description      | GRIB     | GRIB   | GRIB    |
|                    |                  |          |        |         |
| FLEXPART Run       |                  | s        | p      | units   |
|                    |                  | hortname | aramId |         |
+====================+==================+==========+========+=========+
| r                  | mass             | conc     | 20001  | kg      |
| eceptor_units=mass | concentration    |          |        | m**-3   |
+--------------------+------------------+----------+--------+---------+
| r                  | mass mixing      | mxrm     | 20002  | kg      |
| eceptor_units=mixr | ratio            |          |        | kg**-1  |
+--------------------+------------------+----------+--------+---------+

Volume mixing ratio fields
--------------------------

Volume mixing ratio fields are only produced for *forward* simulations
when **Output Field Type** is set to **mixr** or **both** in :ref:`FLEXPART
Run <flexpart_run_icon>`.

The output filename is:

   pptv_sSSS.grib

where SSS is the species index (starts from 1) with leading zeros.

+-------------------------+--------------+-----------+----------------+
| Description             | GRIB         | GRIB      | GRIB           |
|                         |              |           |                |
|                         | shortname    | paramId   | units          |
+=========================+==============+===========+================+
| volume mixing ratio     | mxrv         | 20052     | mol mol**-1    |
+-------------------------+--------------+-----------+----------------+

Dry and wet deposition fields
-----------------------------

These fields are only produced for *forward* simulations when **Output
Field Type** is set to **conc**, **mixr** or **both** in :ref:`FLEXPART
Run <flexpart_run_icon>`. They
are always inserted into the concentration or/and volume mixing ratio
files.

+----------------------+-----------------+-------------+--------------+
| Description          | GRIB            | GRIB        | GRIB         |
|                      |                 |             |              |
|                      | shortname       | paramId     | units        |
+======================+=================+=============+==============+
| dry deposition       | fdd             | 20197       | kg m**-2     |
+----------------------+-----------------+-------------+--------------+
| wet deposition       | fwd             | 20198       | kg m**-2     |
+----------------------+-----------------+-------------+--------------+

Flux fields
-----------

These fields are only produced when **Output Flux** is set to **on** in
:ref:`FLEXPART
Run <flexpart_run_icon>`. The
output filename is:

   flux_sSSS.grib

where SSS is the species index (starts from 1) with leading zeros.

+--------------------+---------------+-----------+--------------------+
| Description        | GRIB          | GRIB      | GRIB               |
|                    |               |           |                    |
|                    | shortname     | paramId   | units              |
+====================+===============+===========+====================+
| eastward flux      | feflux        | 20199     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+
| westward flux      | fwflux        | 20200     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+
| southward flux     | fnflux        | 20201     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+
| northward flux     | fsflux        | 20202     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+
| upward flux        | fuflux        | 20203     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+
| downward flux      | fdflux        | 20204     | kg m**-2 s**-1     |
+--------------------+---------------+-----------+--------------------+

Residence time/response fields
------------------------------

These fields are only produced for *backward* simulations when **Output
Field Type** is set to **rtime** in :ref:`FLEXPART
Run <flexpart_run_icon>`. The
output filename is:

   time_sSSS.grib

where SSS is the species index (starts from one) with leading zeros.

Plume trajectories 
==================

Trajectories are produced when **Output Trajectory** is set to **on** in
:ref:`FLEXPART
Run <flexpart_run_icon>`. The
ASCII file generated by FLEXPART is split according to releases and
converted into another (CSV) format that is better suited to metview.
The output filenames are:

   tr_rRRR.csv

where R is the release number (starts from one) with leading zeros. The
first row in the trajectory file contains metadata as a set of key value
pairs, while the the second row contains the header. The table below
gives a detailed description about the different columns.

+------+---------+------+----------------------------------------------+
| Co   | Name    | U    | Description                                  |
| lumn | (       | nits |                                              |
|      | header) |      |                                              |
+======+=========+======+==============================================+
| 1    | time    | s    | the elapsed time in seconds since the middle |
|      |         |      | point of the release interval                |
+------+---------+------+----------------------------------------------+
| 2    | meanLon | deg  | mean longitude position for all the          |
|      |         | rees | particles                                    |
+------+---------+------+----------------------------------------------+
| 3    | meanLat | deg  | mean latitude position for all the particles |
|      |         | rees |                                              |
+------+---------+------+----------------------------------------------+
| 4    | meanZ   | m    | mean height for all the particles (above sea |
|      |         |      | level)                                       |
+------+---------+------+----------------------------------------------+
| 5    | m       | m    | mean topography underlying all the particles |
|      | eanTopo |      |                                              |
+------+---------+------+----------------------------------------------+
| 6    | meanPBL | m    | mean PBL (Planetary  Boundary Layer) height  |
|      |         |      | for all the particles (above ground level)   |
+------+---------+------+----------------------------------------------+
| 7    | me      | m    | mean tropopause height at the positions of   |
|      | anTropo |      | particles (above sea level)                  |
+------+---------+------+----------------------------------------------+
| 8    | meanPv  | PVU  | mean potential vorticity for all the         |
|      |         |      | particles                                    |
+------+---------+------+----------------------------------------------+
| 9    | rms     | km   | total horizontal RMS (root mean square)      |
|      | HBefore |      | distance before clustering                   |
+------+---------+------+----------------------------------------------+
| 10   | rm      | km   | total horizontal RMS distance after          |
|      | sHAfter |      | clustering                                   |
+------+---------+------+----------------------------------------------+
| 11   | rms     | m    | total vertical RMS distance before           |
|      | VBefore |      | clustering                                   |
+------+---------+------+----------------------------------------------+
| 12   | rm      | m    | total vertical RMS distance after            |
|      | sVAfter |      | clustering                                   |
+------+---------+------+----------------------------------------------+
| 13   | p       | %    | fraction of particles in the PBL             |
|      | blFract |      |                                              |
+------+---------+------+----------------------------------------------+
| 14   | p       | %    | fraction of particles with PV<2pvu           |
|      | v2Fract |      |                                              |
+------+---------+------+----------------------------------------------+
| 15   | tro     | %    | fraction of particles within the             |
|      | poFract |      | troposphere                                  |
+------+---------+------+----------------------------------------------+
| 16\* | clLon   | deg  | mean longitude position for all the          |
|      | \_\ *N* | rees | particles in *cluster N*                     |
+------+---------+------+----------------------------------------------+
| 17\* | clLat   | deg  | mean latitude position for all the particles |
|      | \_\ *N* | rees | in *cluster N*                               |
+------+---------+------+----------------------------------------------+
| 18\* | clZ     | m    | mean height for all the particles in         |
|      | \_\ *N* |      | *cluster N* (above sea level)                |
+------+---------+------+----------------------------------------------+
| 19\* | clFract | %    | fraction of particles in *cluster N* (above  |
|      | \_\ *N* |      | sea level)                                   |
+------+---------+------+----------------------------------------------+
| 20\* | clRms   | km   | total horizontal RMS distance in *cluster N* |
|      | \_\ *N* |      |                                              |
+------+---------+------+----------------------------------------------+

Columns 16-20 get repeated for each cluster.

Receptor output
===============

Output at receptor points are produced when **Receptors** is set to
**on** in :ref:`FLEXPART
Run <flexpart_run_icon>`. The
binary file generated by FLEXPART is split according to species and
converted to CSV.   

When **Receptor Units** is set to **mass** in :ref:`FLEXPART
Run <flexpart_run_icon>` the
output filename is: 

   receptor_conc_sSSS.csv

When **Receptor Units** is set to **mixr** in :ref:`FLEXPART
Run <flexpart_run_icon>` the
output filename is

   receptor_pptv_sSSS.csv

where SSS is the species number (with leading zeros).
