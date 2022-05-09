"""
GRIB - Vertical Hovmoeller in Height with Model Level Data
"""

# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv

# Note: at least Metview version 5.16.0 is required

# getting data
use_mars = False

filename = "vert_hovm_ml_tq.grib"
steps = list(range(0, 132, 12))

# getting forecast data from MARS
if use_mars:
    ret_core = {
        "date": 20171016,
        "time": 0,
        "levtype": "ml",
        "grid": [1, 1],
        "area": [45, -10, 55, 5],
    }

    tq = mv.retrieve(
        type="fc",
        param=["t", "q"],
        step=steps,
        levelist=list(range(80, 138)),
        **ret_core
    )
    lnsp = mv.retrieve(type="fc", param="lnsp", step=steps, levelist=1, **ret_core)
    zs = mv.retrieve(type="an", param="z", levelist=1, **ret_core)
    g = mv.merge(tq, lnsp, zs)
# read data from file
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# extract surface geopotential
zs = g.select(shortName="z")

# compute geopotential on model levels
z = mv.Fieldset()
for step in steps:
    t = g.select(shortName="t", step=step)
    q = g.select(shortName="q", step=step)
    lnsp = g.select(shortName="lnsp", step=step)
    z.append(mv.mvl_geopotential_on_ml(t, q, lnsp, zs))

# scale geopotential to height above sea level
z = z / 9.81

# scale temperature from K to C
t = g.select(shortName="t") - 273.16

# create input fieldset for vertical Hovmoeller
g_hov = mv.merge(t, z)

# define time axis
time_axis = mv.maxis(
    axis_type="date",
    axis_tick_label_height=0.4,
    axis_date_type="hours",
    axis_days_label_height=0.4,
)

# define vertical axis
vertical_axis = mv.maxis(
    axis_type="position_list",
    axis_tick_position_list=list(range(0, 4500, 500)),
    axis_tick_label_height=0.4,
    axis_title_text="Height ASL (m)",
    axis_title_height=0.5,
)

# define vertical Hovmoeller with height above sea level axis for model level
# data for a given location (at least Metview version 5.16.0 is required)
hov = mv.mhovmoellerview(
    type="vertical_hovm",
    input_mode="nearest_gridpoint",
    point=[48, 2],
    vertical_level_type="param",
    top_level=4000,
    bottom_level=0,
    vertical_coordinate_param=129,
    vertical_coordinate_extrapolate="off",
    time_axis=time_axis,
    vertical_axis=vertical_axis,
)

# define contour shading
t_shade = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_fM50t58i2",
    legend="on",
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.3, legend_text_colour="charcoal")

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="vert_hovm_ml_in_height"))

# generate plot
mv.plot(hov, g_hov, t_shade, legend)
