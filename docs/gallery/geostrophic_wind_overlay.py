"""
GRIB - Geostrophic Wind Overlay
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

# define wind and contour style
w_style = mv.mwind(
    wind_thinning_factor=8,
    wind_arrow_colour="greenish_blue",
    wind_arrow_thickness=1,
    wind_arrow_unit_velocity=50,
    legend="on",
    wind_legend_text="(50 m/s)  wind",
)

gw_style = mv.mwind(
    wind_thinning_factor=8,
    wind_arrow_colour="magenta",
    wind_arrow_thickness=1,
    wind_arrow_unit_velocity=50,
    legend="on",
    wind_legend_text="(50 m/s) geostrophic wind",
)

cont_z = mv.mcont(contour_automatic_setting="ecmwf", legend="off")

# define the geographical view
coastlines = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8353,0.8353,0.8353)",
    map_boundaries="on",
    map_boundaries_colour="brick",
    map_grid_colour="charcoal",
)

view = mv.geoview(area_mode="name", area_name="north_america", coastlines=coastlines)

# define title
vdate = mv.valid_date(z)
title = mv.mtext(
    text_lines="z [dam] and wind and geostrophic wind {} hPa {}".format(
        level, vdate.strftime("%Y-%m-%d %H UTC")
    ),
    text_font_size=0.5,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.5)

# define output
mv.setoutput(mv.pdf_output(output_name="geostrophic_wind_overlay"))

# generate plot
mv.plot(view, w, w_style, gw, gw_style, z, cont_z, title, legend)
