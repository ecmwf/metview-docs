"""
GRIB - Ageostrophic Wind 
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

filename = "gw_era5.grib"

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
                "specific_humidity",
                "temperature",
                "u_component_of_wind",
                "v_component_of_wind",
            ],
            "pressure_level": ["250", "500"],
            "year": "2010",
            "month": "04",
            "day": "24",
            "time": "12:00",
            "area": [
                90,
                -150,
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
z = mv.read(data=g, param="z", levelist=level)
w = mv.read(data=g, param=["u", "v"], levelist=level)

# compute geostrophic wind
gw = mv.geostrophic_wind(z)

# compute ageostrophic wind
agw = w - gw

# compute speed for ageostrophic wind
agw_sp = mv.sqrt(agw[0] ** 2 + agw[1] ** 2)

# define wind plotting style
w_style = mv.mwind(
    wind_thinning_factor=4.0,
    legend="on",
    wind_arrow_calm_below=0.6,
    wind_arrow_colour="navy",
    wind_arrow_head_ratio=0.6,
    wind_arrow_unit_velocity=40,
)

# define z style
cont_z = mv.mcont(
    contour_line_thickness=2,
    contour_line_colour="burgundy",
    contour_highlight_colour="burgundy",
)

# define ageostrophic wind speed style
cont_sp = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=45,
    contour_min_level=15,
    contour_interval=5,
    contour_label="off",
    contour_shade="on",
    contour_shade_method="area_fill",
    contour_shade_max_level_colour="red",
    contour_shade_min_level_colour="turquoise",
    contour_shade_colour_direction="clockwise",
)

# define the geographical view
coastlines = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_resolution="medium",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8471,0.8471,0.8471)",
    map_boundaries="on",
    map_boundaries_colour="gold",
)

view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="corners",
    area=[20.24, -117.36, 45.17, -62.94],
    map_vertical_longitude=-100,
    coastlines=coastlines,
)

# define title
vdate = mv.valid_date(z)
title = mv.mtext(
    text_lines="z [dam] and ageostrophic wind {} hPa {}".format(
        level, vdate.strftime("%Y-%m-%d %H UTC")
    ),
    text_font_size=0.5,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define output
mv.setoutput(mv.pdf_output(output_name="ageostrophic_wind"))

# generate plot
mv.plot(view, agw_sp, cont_sp, agw, w_style, z, cont_z, title, legend)
