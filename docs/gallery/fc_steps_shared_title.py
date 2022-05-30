"""
GRIB - Forecast Steps with Shared Title
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

# getting data
use_mars = False

# getting forecast data from MARS
if use_mars:
    g = mv.retrieve(
        type="fc",
        levtype="sfc",
        param=["msl", "10fg6"],
        date=20111215,
        time=00,
        step=[0, "to", 48, "by", 6],
        area=[80, -60, 20, 60],
        grid=[0.5, 0.5],
    )
# reading data from file or getting from data server
else:
    filename = "fc_msl_wg_joachim.grib"
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# read msl
msl = g.select(shortName="msl")

# -------------------------------
# define map plots
# -------------------------------

# define contouring for msl
cont_msl = mv.mcont(
    contour_line_thickness=2,
    contour_line_colour="charcoal",
    contour_highlight="on",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=3,
    contour_level_selection_type="interval",
    contour_interval=5,
    contour_label_height=0.2,
)

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="RGB(0.3137,0.3137,0.3137)",
    map_coastline_resolution="medium",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8314,0.8314,0.8314)",
    map_boundaries="on",
    map_boundaries_colour="chestnut",
    map_grid="off",
    map_label="off",
)

# define geo view
view = mv.geoview(area_mode="name", area_name="central_europe", coastlines=coast)

# create a 2x4 plot layout with the defined geoview
pages = mv.mvl_regular_layout(view, 4, 2, 1, 1, [0, 100, 0, 100])


# define title for the maps - it will automatically
# extract the specified GRIB metadata
title = mv.mtext(
    text_line_1="<grib_info key='valid-date' format='%Y-%m-%d %H'/> UTC (+<grib_info key='step'/>h)",
    text_font_size=0.4,
)

# ---------------------------------------------
# define shared (positional) title at the top
# ---------------------------------------------

# we want to show a shared title at the top of the page. The space is
# is simple not enough above the maps to display this amount of information.

# create an annotation view covering the whole page area (dimensions are in %).
# It is just a placeholder and its only purpose is to hold a custom positional
# mtext object.
empty_view = mv.annotationview()

# create the page (dimensions are in %) holding the annotation view. For simplicity
# it covers the whole plot area
title_page = mv.plot_page(top=0, bottom=100, left=0, right=100, view=empty_view)

pages.append(title_page)

# create a positional title to be added to the annotation view.
# Note: its coordinates are in cm! x is measured from the left side
# of the parent page (e.i. title_page), while y is measured from the bottom
# of the parent page!

# width of and A4 landscape page in cm
pw = 29.7

bdate = mv.base_date(msl[0])
shared_title = mv.mtext(
    text_lines="ECMWF HRES Param: msl Run: {}".format(
        bdate.strftime("%Y-%m-%d %H UTC")
    ),
    text_font_size=0.6,
    text_mode="positional",
    text_box_x_position=pw / 2 - 20 / 2,
    text_box_y_position=19,
    text_box_x_length=20,
    text_box_y_length=2,
)

# create the final layout
dw = mv.plot_superpage(pages=pages)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="fc_steps_shared_title"))

# generate plot object
d = [[dw[i], msl[i], cont_msl, title] for i in range(len(dw) - 1)]
d.extend([dw[-1], shared_title])

# generate plot
mv.plot(d)
