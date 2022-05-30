"""
GRIB - Cross Section for Temperature Advection ERA5
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

# read grib file
filename = "xs_tadv_era5.grib"

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
                "temperature",
                "u_component_of_wind",
                "v_component_of_wind",
                "relative-humidity",
            ],
            "pressure_level": [
                "100",
                "125",
                "150",
                "175",
                "200",
                "225",
                "250",
                "300",
                "350",
                "400",
                "450",
                "500",
                "550",
                "600",
                "650",
                "700",
                "750",
                "775",
                "800",
                "825",
                "850",
                "875",
                "900",
                "925",
                "950",
                "975",
                "1000",
            ],
            "year": "2007",
            "month": "01",
            "day": [
                "20",
            ],
            "time": ["06:00"],
            "area": [
                60,
                -20,
                40,
                10,
            ],
        },
        filename,
    )
    fs = mv.read(filename)
# read data from file
else:
    if mv.exist(filename):
        fs = mv.read(filename)
    else:
        fs = mv.gallery.load_dataset(filename)

# read parameters
t = fs.select(shortName="t")
u = fs.select(shortName="u")
v = fs.select(shortName="v")
rh = fs.select(shortName="r")

# compute temperature advection in K/s units
t_g = mv.gradient(t)
adv = -(u * t_g[0::2] + v * t_g[1::2])

# scale advection to 1E-4 K/s units
adv = adv * 1e4

# compute equivalent potential temperature
ept = mv.eqpott_p(temperature=t, humidity=rh)

# define cross section line
line = [54, -10, 49, 0]

# define vertical axis
vertical_axis = mv.maxis(
    axis_orientation="vertical",
    axis_type="position_list",
    axis_tick_position_list=[1000, 925, 850, 700, 500, 400, 300, 250, 200],
    axis_tick_label_height=0.4,
)

# define pressure range for cross section
top_pressure = 200
bottom_pressure = 1000

# create cross section for advection
xs_adv = mv.mcross_sect(
    data=adv, line=line, bottom_level=bottom_pressure, top_level=top_pressure
)

# create cross section for ept
xs_ept = mv.mcross_sect(
    data=ept, line=line, bottom_level=bottom_pressure, top_level=top_pressure
)

# define cross section view
xs_view = mv.mxsectview(
    line=line,
    bottom_level=bottom_pressure,
    top_level=top_pressure,
    vertical_axis=vertical_axis,
)

# define contouring for advection
cont_adv = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=24,
    contour_min_level=-24,
    contour_interval=3,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="colorbrewer_RdBu_16",
)

# define contouring for ept
cont_ept = mv.mcont(
    contour_line_colour="charcoal",
    contour_highlight_colour="charcoal",
    contour_highlight_thickness=2,
    contour_level_selection_type="interval",
    contour_interval=2,
    contour_label_height=0.4,
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define title
vdate = mv.valid_date(t[0])
title = mv.mtext(
    text_lines=[
        "ERA5 t advection [1E-4 K/s] and ept [K] {}".format(
            vdate.strftime("%Y-%m-%d %H UTC")
        ),
        "",
    ],
    text_font_size=0.5,
)


# define the output plot file
mv.setoutput(mv.pdf_output(output_name="cross_section_pl_tadv"))

# generate plot
mv.plot(xs_view, adv, cont_adv, ept, cont_ept, legend, title)
