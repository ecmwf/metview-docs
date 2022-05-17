"""
GRIB - Frame Masking
"""

# (C) Copyright 2021- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv

# read the input grib file
# regular lat-lon 1x1 degree
filename = "2m_temperature.grib"
if mv.exist(filename):
    f = mv.read(filename)
else:
    f = mv.gallery.load_dataset(filename)

# interpolate to a subarea and generate frame with a bitmap (missing values) inside.
# The width of the frame is 3 gridpoints (3x2=6 degrees)
r_bm = mv.regrid(data=f, area=[34, -10, 60, 30], grid=[2, 2], frame=3)

# turn the frame field into a mask (0 and 1 values)
r_msk = mv.nobitmap(r_bm * 0 + 1, 0)

# define t contouring
t_cont = mv.mcont(contour_automatic_setting="ecchart", legend="on")

# define grid shading for mask (0 and 1) values
grid_shading_01 = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="level_list",
    contour_level_list=[0, 0.9, 1.1],
    contour_label="off",
    contour_shade="on",
    contour_shade_technique="grid_shading",
    contour_shade_colour_method="list",
    contour_shade_colour_list=["RGB(0.765,0.8789,0.9448)", "RGB(0.8074,0.5293,0.4004)"],
)

# define coastlines
coast = mv.mcoast(
    map_coastline_resolution="low",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.6314,0.6314,0.6314)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8294,0.8294,0.8294)",
    map_label_height=0.3,
    map_grid_latitude_increment=10,
)

# define geographical view
view = mv.geoview(area_mode="name", area_name="europe", coastlines=coast)

# define layout
page_0 = mv.plot_page(top=20, bottom=80, right=50, view=view)
page_1 = mv.plot_page(top=20, bottom=80, left=50, right=100, view=view)
dw = mv.plot_superpage(page=[page_0, page_1])

# define legend
legend = mv.mlegend(legend_text_font_size=0.35)

# define titles
title_bm = mv.mtext(text_lines=["frame with bitmap inside", ""], text_font_size=0.6)
title_msk = mv.mtext(text_lines=["frame turned into a mask", ""], text_font_size=0.6)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="frame_masking"))

# generate plot
mv.plot(
    dw[0],
    r_bm,
    t_cont,
    legend,
    title_bm,
    dw[1],
    r_msk,
    grid_shading_01,
    legend,
    title_msk,
)
