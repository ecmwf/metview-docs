"""
GRIB - Vertical Hovmoeller in Pressure with Model Level Data
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

filename = "vert_hovm_ml_w.grib"

# getting forecast data from MARS
if use_mars:
    ret_core = {
        "type": "fc",
        "date": 20171016,
        "time": 0,
        "step": list(range(0, 132, 12)),
        "levtype": "ml",
        "grid": [1, 1],
        "area": [45, -10, 55, 5],
    }
    w = mv.retrieve(param="w", levelist=list(range(50, 138)), **ret_core)
    lnsp = mv.retrieve(param="lnsp", levelist=1, **ret_core)
    g = mv.merge(w, lnsp)
# read data from file
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

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
    axis_tick_position_list=[
        1000,
        925,
        850,
        700,
        500,
        400,
        300,
        250,
        200,
        150,
        100,
    ],
    axis_tick_label_height=0.4,
    axis_title_text="Pressure (hPa)",
    axis_title_height=0.5,
)

# define vertical Hovmoeller with pressure axis for model level
# data for a given location (at least Metview version 5.16.0 is required)
hov = mv.mhovmoellerview(
    type="vertical_hovm",
    input_mode="nearest_gridpoint",
    point=[52, -7],
    vertical_level_type="pressure",
    top_level=100,
    bottom_level=1010,
    vertical_coordinate_extrapolate="on",
    vertical_coordinate_extrapolate_mode="constant",
    time_axis=time_axis,
    vertical_axis=vertical_axis,
)

# define contour shading
w_shade = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_viobrn_fM5t5lst",
    legend="on",
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.3, legend_text_colour="charcoal")

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="vert_hovm_ml_in_pressure"))

# generate plot
mv.plot(hov, g, w_shade, legend)
