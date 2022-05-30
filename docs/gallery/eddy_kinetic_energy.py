"""
GRIB - Eddy Kinetic Energy ERA5
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

filename = "eke_era5.grib"

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
                "vorticity",
                "u_component_of_wind",
                "v_component_of_wind",
            ],
            "pressure_level": [
                "500",
            ],
            "year": "1997",
            "month": "02",
            "day": "11",
            "time": "00:00",
            "area": [
                90,
                -180,
                10,
                180,
            ],
        },
        filename,
    )
    g = mv.read(filename)
# reading data from file or getting it from data server
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)


# get fields on 500 hPa
level = 500
u = mv.read(data=g, param="u", levelist=level)
v = mv.read(data=g, param="u", levelist=level)
z = mv.read(data=g, param="z", levelist=level)

# compute the eddy kinetic energy (per unit mass) in m2/s2 units
u_p = u - mv.mean_ew(u)
v_p = v - mv.mean_ew(v)
eke = (u_p**2 + v_p**2) / 2

# define contouring
cont_eke = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="level_list",
    contour_level_list=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1500],
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="m_purple2_11",
)

cont_z = mv.mcont(
    contour_line_thickness=2,
    contour_line_colour="charcoal",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=4,
    contour_level_selection_type="interval",
    contour_interval=10,
    contour_label_height=0.4,
    grib_scaling_of_derived_fields="on",
)

# define coastlines
coast = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="grey",
    map_grid_colour="RGB(0.3843,0.3843,0.3843)",
)


# define the geographical view
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="centre",
    map_vertical_longitude=-20,
    map_centre_latitude=55,
    map_centre_longitude=-20,
    map_scale=35.0e6,
    coastlines=coast,
)


# define title
vdate = mv.valid_date(z)
title = mv.mtext(
    text_lines=[
        "ERA5 z [dam] and EKE [m2/s2] {} hPa {}".format(
            level, vdate.strftime("%Y-%m-%d %H UTC")
        ),
        "",
    ],
    text_font_size=0.5,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define output
mv.setoutput(mv.pdf_output(output_name="eddy_kinetic_energy"))

# generate plot
mv.plot(view, eke, cont_eke, z, cont_z, title, legend)
