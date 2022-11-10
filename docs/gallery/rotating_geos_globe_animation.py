"""
Rotating GEOS Globe Animated GIF
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

import os

import metview as mv

# get temperature 850 hPa field
filename = "t850.grb"
if mv.exist(filename):
    g = mv.read(filename)
else:
    g = mv.gallery.load_data

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="RGB(0.3569,0.3569,0.3569)",
    map_coastline_thickness=3,
    map_grid_colour="charcoal",
    map_label="off",
)

# define contour shading
t_shade = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_fM48t56i4",
    legend="on",
)

# define legend + title
title = mv.mtext(text_font_size=0.5)
legend = mv.mlegend(legend_text_font_size=0.45)

# define PDF output
out_basename = "rotating_geos_globe_animation"
mv.setoutput(mv.pdf_output(output_name=out_basename))

# the list containing the plot objects
gr = []

# generate each frame
for i, lon in enumerate(range(90, -100, -10)):

    # define the view
    view = mv.geoview(
        map_projection="geos",
        map_vertical_longitude=lon,
        coastlines=coast,
        page_frame="off",
        subpage_frame="off",
    )

    dw = mv.plot_superpage(pages=[mv.plot_page(view=view)])

    # define the contents of a given page in the PDF output
    gr.extend([dw, g[0], t_shade, title, legend, mv.newpage()])

# generate the plot
mv.plot(gr)

# convert the PDF file to animated GIF using imagemagick
# with a 100ms pause between frames
pdf_file = f"{out_basename}.pdf"
gif_file = f"{out_basename}.gif"
os.system(rf"""convert -delay 100 {pdf_file} {gif_file}""")
