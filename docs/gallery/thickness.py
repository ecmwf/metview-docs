"""
GRIB - 500/1000 hPa Thickness
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
use_cds = False

filename = "thickness_era5.grib"

# getting data from CDS
if use_cds:
    import cdsapi

    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-pressure-levels",
        {
            "product_type": "reanalysis",
            "format": "grib",
            "variable": [
                "geopotential",
            ],
            "pressure_level": [
                "1000",
                "500",
            ],
            "year": "1995",
            "month": "02",
            "day": "02",
            "time": "06:00",
            "area": [
                90,
                -100,
                10,
                80,
            ],
        },
        filename,
    )
    g = mv.read(filename)
# reading data from file or getting from data server
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# get z fields on 1000 and 500 hPa
z1 = g.select(shortName="z", level=1000)
z2 = g.select(shortName="z", level=500)

# compute the 500/1000 thickness (units gpm)
th = z2 - z1

# define contouring for dam units. The gpm units will
# automatically be scaled to dam for contouring because
# "grib_scaling_of_derived_fields" is "on". Fieldset th now qualifies
# as "derived" since it is the result of a mathematical field
# operation.
cont_th = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="level_list",
    contour_max_level=600,
    contour_level_list=[
        460,
        480,
        485,
        490,
        495,
        500,
        505,
        510,
        515,
        520,
        525,
        530,
        535,
        540,
        545,
        550,
        555,
        560,
        565,
        570,
        575,
        580,
        585,
        590,
        595,
        610,
    ],
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="m_rainbow_purple_blue_red_24",
    grib_scaling_of_derived_fields="on",
)


# define coastlines
coast = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_thickness=2,
    map_coastline_resolution="medium",
)

# define the geographical view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="centre",
    map_centre_latitude=55,
    map_scale=35.0e6,
    coastlines=coast,
)


# define title
vdate = mv.valid_date(th)
title = mv.mtext(
    text_lines=[
        "ERA5 500/1000 hPa thickness [dam] {}".format(
            vdate.strftime("%Y-%m-%d %H UTC")
        ),
        "",
    ],
    text_font_size=0.5,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define output
mv.setoutput(mv.pdf_output(output_name="thickness"))

# generate plot
mv.plot(view, th, cont_th, title, legend)
