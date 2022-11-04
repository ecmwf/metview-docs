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

out_basename = "rotating_geos_globe_animation"

# create temporary dir for the intermediate PDFs
out_dir = f"{out_basename}_tmp"
os.makedirs(out_dir, exist_ok=True)

# generate one PDF for each frame
for i, lon in enumerate(range(90, -100, -10)):

    mv.setoutput(
        mv.pdf_output(output_name=os.path.join(out_dir, f"{out_basename}_{i:02d}"))
    )

    # define view
    view = mv.geoview(
        map_projection="geos",
        map_vertical_longitude=lon,
        coastlines=coast,
        page_frame="off",
        subpage_frame="off",
    )

    dw = mv.plot_superpage(pages=[mv.plot_page(view=view)])

    # generate plot
    mv.plot(dw, g[0], t_shade, title, legend)

# convert the individual PDF files to animated GIF using imagemagick
# with a 100ms pause between frames
pdf_file = os.path.join(out_dir, f"{out_basename}_*.pdf")
gif_file = f"{out_basename}.gif"
os.system(rf"""convert -delay 100 {pdf_file} {gif_file}""")

# NOTE: the temporary PDF files are not cleaned up automatically
