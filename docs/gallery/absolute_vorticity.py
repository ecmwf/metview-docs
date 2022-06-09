"""
GRIB - Absolute Vorticity
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

filename = "absv_era5.grib"

# getting forecast data from CDS
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
                "vorticity",
            ],
            "pressure_level": [
                "500",
            ],
            "year": "2002",
            "month": "01",
            "day": "03",
            "time": "00:00",
            "area": [
                90,
                -170,
                10,
                40,
            ],
        },
        filename,
    )
    g = mv.read(filename)
# read data from file
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# get fields on 500 hPa
level = 500
vo = mv.read(data=g, param="vo", levelist=level)
z = mv.read(data=g, param="z", levelist=level)

# compute absolute vorticity from relative vorticity
absv = mv.absolute_vorticity(vo)

# define contouring for absolute vorticity
cont_vo = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_viobrn_fM50t50lst_less",
    legend="on",
    grib_scaling_of_derived_fields="on",
)

# define contouring for geopotential
cont_z = mv.mcont(
    contour_line_thickness=2,
    contour_line_colour="charcoal",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=4,
    contour_level_selection_type="interval",
    contour_interval=5,
    contour_label_height=0.4,
    grib_scaling_of_derived_fields="on",
)

# define coastlines
coast = mv.mcoast(map_coastline_colour="chestnut", map_coastline_thickness=3)
# define the geographical view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="centre",
    map_vertical_longitude=-95,
    map_centre_latitude=35,
    map_centre_longitude=-80,
    map_scale=30.0e6,
    coastlines=coast,
)

# define title
vdate = mv.valid_date(z)
title = mv.mtext(
    text_lines=[
        "ERA5 z [dam] and absv [1E5 1/s] {} hPa {}".format(
            level, vdate.strftime("%Y-%m-%d %H UTC")
        ),
        "",
    ],
    text_font_size=0.5,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define output
mv.setoutput(mv.pdf_output(output_name="absolute_vorticity"))

# generate plot
mv.plot(view, absv, cont_vo, z, cont_z, title, legend)
