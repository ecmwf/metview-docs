.. _visualisers:

Visualisers
///////////


Whilst some data formats (e.g. GRIB) can be straightforward to visualise
because their contents are quite constrained and their meta-data is
standardised, this is not true for all formats; for example, netCDF or
:ref:`ASCII
tables <macro_tables>` can
contain many types of data which could be plotted in various ways.

In order to allow visualisation of these formats, Metview has a set of
**visualiser** icons, one for each data type:
:ref:`netCDF <netcdf_visualiser_icon>`,
ODB, ASCII table and :ref:`direct input
lists <input_visualiser_icon>`.
In each case, the first question is what the data represents, e.g.
points or matrix; in a geographical or x/y coordinate system. After this
has been chosen, the rest of the available parameters can be filled in,
thus giving enough information to plot the data. The visualiser icon can
then be visualised via its context menu, producing a default plot for
the data. The plot may be further customised by using appropriate
**view** and **visual definition** icons.

Dates should be strings formatted as "YYYY-MM-DD"; a time can optionally
be specified like this: "YYYY-MM-DD HH:MM:SS".
