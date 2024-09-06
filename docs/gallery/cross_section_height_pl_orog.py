"""
Cross Section in Height for Pressure Level Data with Orography
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

# get data
use_mars = False
if use_mars:
    # retrieve data from MARS
    ret_core = {
        "date": 20200822,
        "time": 0,
        "area": [40, -93, 51, -84],
        "grid": [0.5, 0.5],
    }

    # forecast fields on pressure levels
    fs_pl = mv.retrieve(
        **ret_core,
        type="fc",
        levtype="pl",
        levelist=[1000, 925, 850, 700, 400, 500, 300],
        step=12,
        param=["t", "z"]
    )

    # surface geopotential
    zs = mv.retrieve(**ret_core, type="an", levtype="sfc", param="z")
else:
    # read data from GRIB file
    filename = "xs_pl_orog.grib"
    if mv.exist(filename):
        fs_pl = mv.read(filename)
    else:
        fs_pl = mv.gallery.load_dataset(filename)
    zs = mv.read(data=fs_pl, param="z", levtype="sfc")

# extract pl data
t = mv.read(data=fs_pl, param="t")
z = mv.read(data=fs_pl, param="z", levtype="pl")

# define cross section line
line = [50.21, -91.82, 40.82, -84.71]

# define bottom level (m)
bottom_level = 0

# converts temperature from K to C and z to m
t = mv.read(data=t) - 273.16
h = mv.geometric_height_from_geopotential(mv.read(data=z))

# compute cross section in height (above sea level) for t
# (using h, paramId=3008)
xs_t = mv.mcross_sect(
    data=mv.merge(t, h),
    line=line,
    vertical_coordinates="user",
    vertical_coordinate_param=3008,
    vertical_coordinate_extrapolate="on",
)

# generate orography area curve
hs = mv.geometric_height_from_geopotential(zs)
orog_curve = mv.xs_build_orog(xs_t, hs, bottom_level, "charcoal")

# define contour shading for temperature
cont = mv.mcont(
    legend="on",
    contour_line_colour="charcoal",
    contour_highlight="off",
    contour_level_selection_type="interval",
    contour_max_level=25,
    contour_min_level=4,
    contour_interval=1,
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="eccharts_sh_BuYlRd_aod_lowthreshold_14",
    contour_shade_colour_list_policy="dynamic",
)

# define vertical axis
vertical_axis = mv.maxis(
    axis_orientation="vertical",
    axis_title_text="Height ASL (m)",
    axis_tick_label_height=0.4,
)

# define cross section in height above sea level  (m)
xs_view = mv.mxsectview(line=line, top_level=3000, bottom_level=bottom_level, vertical_axis=vertical_axis)

# define legend
legend = mv.mlegend(legend_text_font_size=0.35)

# define title
title = mv.mtext(text_font_size=0.4)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="cross_section_height_pl_orog"))

# generate plot
mv.plot(xs_view, xs_t, cont, orog_curve, legend, title)
