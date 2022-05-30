"""
GRIB - Forecast Steps with Shared Legend and Title
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

# read msl and 10m wind gust (max in last 6 hours)
msl = g.select(shortName="msl")
wg = g.select(shortName="10fg6")

# -------------------------------
# define map plots
# -------------------------------

# define contouring for msl
msl_cont = mv.mcont(
    contour_line_thickness=2,
    contour_line_colour="charcoal",
    contour_highlight="off",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=4,
    contour_level_selection_type="interval",
    contour_interval=5,
    contour_label_height=0.2,
    grib_scaling_of_derived_fields="on",
)

# define contouring for wind gust. The legend is turned off because
# we want to show only a shared legend at the top of the page
wg_cont = mv.mcont(
    contour="off",
    contour_level_selection_type="level_list",
    contour_level_list=[12, 15, 20, 25, 30, 35, 50],
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="list",
    contour_shade_method="area_fill",
    contour_shade_colour_list=[
        "RGB(0.5374,0.6855,0.9606)",
        "RGB(0.1259,0.5569,0.9878)",
        "avocado",
        "yellowish_orange",
        "red",
        "violet",
    ],
)

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="RGB(0.3137,0.3137,0.3137)",
    map_coastline_thickness="2",
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
pages = mv.mvl_regular_layout(view, 4, 3, 1, 1, [0, 100, 0, 100])

# define title generator for the maps
def make_title(f):
    step = mv.grib_get_long(f[0], "step")
    vdate = mv.valid_date(f[0])
    title = mv.mtext(
        text_lines="{} (+{}h)".format(vdate.strftime("%Y-%m-%d %H UTC"), int(step)),
        text_font_size=0.4,
    )
    return title


# ---------------------------------------------
# define positional title at the top
# ---------------------------------------------

# we want to show a shared title at the top of the page. The space is
# is simple not enough above the maps to display this amount of information.

# create an annotation view covering the whole page area (dimensions are in %).
# It is just a placeholder and its only purpose is to hold a custom positional
# mtext object.
title_view = mv.annotationview()

# create the page (dimensions are in %) holding the annotation view. For simplicity
# it covers the whole plot area
title_page = mv.plot_page(top=0, bottom=100, left=0, right=100, view=title_view)

pages.append(title_page)

# create a positional title to be added to the annotation view.
# Note: its coordinates are in cm! x is measured from the left side
# of the parent page (e.i. title_page), while y is measured from the bottom
# of the parent page!

# width of an A4 landscape page in cm

pw = 29.7

bdate = mv.base_date(msl[0])
shared_title = mv.mtext(
    text_lines="ECMWF HRES Param: msl/10fg6 Run: {}".format(
        bdate.strftime("%Y-%m-%d %H UTC")
    ),
    text_font_size=0.6,
    text_mode="positional",
    text_box_x_position=3,
    text_box_y_position=19.2,
    text_box_x_length=20,
    text_box_y_length=2,
    text_justification="left",
)

# ----------------------------------------------
# define positional shared legend at the top
# ----------------------------------------------

# we do not want to display the legend for each plot (since the space is
# confined) but want to show only one legend atop just below the main page title.
# Since the legend is only generated when data is plotted into a view, we will
# create an "invisible" geo view and properly adjust it so that the legend can
# appear at the desired position.

# create an empty coastlines
empty_coast = mv.mcoast(map_coastline="off", map_grid="off", map_label="off")

# create a geoview
legend_view = mv.geoview(
    page_frame="off",
    subpage_frame="off",
    coastlines=empty_coast,
    subpage_x_position=40,
    subpage_y_position=65,
    subpage_x_length=20,
    subpage_y_length=20,
)


# create a page (dimensions are in %) holding the view. It is positioned at the
# top of the A4 superpage
legend_page = mv.plot_page(top=0, bottom=20, left=0, right=100, view=legend_view)

pages.append(legend_page)

# create a field to be plotted into the view. It should only contain missing values,
# since we do not want to generate any result
empty_fld = mv.bitmap(wg[0] * 0, 0)

# define the conturing. It is the same that we defined for wg but the
# legend has to be enabled now!
empty_cont = mv.mcont(**wg_cont, legend="on")

# define an empty title
empty_title = mv.mtext(text_line_count=0)

# define the legend. Note: its coordinates are in cm! x is measured
# from the left side of the parent page (legend_page), while y is measured from
# the bottom of the parent page!
shared_legend = mv.mlegend(
    legend_box_mode="positional",
    legend_text_font_size=0.4,
    legend_box_x_position=3,
    legend_box_y_position=1.5,
    legend_box_x_length=10,
    legend_box_y_length=0.6,
    legend_units_text="m/s",
    legend_title="on",
    legend_title_text="m/s",
    legend_title_position="right",
)

# create the final layout
dw = mv.plot_superpage(pages=pages)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="fc_steps_shared_legend_title"))

# generate plot object
d = [
    [dw[i + 3], wg[i], wg_cont, msl[i], msl_cont, make_title(msl[i])] for i in range(9)
]
d.extend([dw[-2], shared_title])
d.extend([dw[-1], empty_fld, empty_cont, shared_legend, empty_title])

# generate plot
mv.plot(d)
