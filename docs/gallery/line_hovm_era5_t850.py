"""
GRIB - Line Hovmoeller T850 ERA5
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

filename = "t850_era5_atl.grib"

# getting forecast data from CDS
if use_cds:
    import cdsapi

    c = cdsapi.Client()

    c.retrieve(
        "reanalysis-era5-pressure-levels-monthly-means",
        {
            "format": "grib",
            "variable": [
                "temperature",
            ],
            "pressure_level": "850",
            "year": [
                "2000",
                "2001",
            ],
            "month": list(range(1, 13)),
            "time": "00:00",
            "area": [
                50,
                -40,
                -50,
                -20,
            ],
            "product_type": "monthly_averaged_reanalysis",
        },
        filename,
    )
    g = mv.read(filename)
# getting data locally or from file server
else:
    if mv.exist(filename):
        g = mv.read(filename)
    else:
        g = mv.gallery.load_dataset(filename)

# get t from file
t = g.select(shortName="t", level=850)

# convert to Celsius
t = t - 273.16

# define section line (N/W/S/E)
line = [50, -35, -50, -35]

# define t shading
t_shading = mv.mcont(
    legend="on",
    contour="off",
    contour_level_selection_type="interval",
    contour_max_level=22,
    contour_min_level=-10,
    contour_interval=2,
    contour_label="off",
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="norway_blue_red_16",
)

# define time axis
time_axis = mv.maxis(
    axis_type="date",
    axis_date_type="months",
    axis_years_label_quality="high",
    axis_years_label_height=0.5,
    axis_months_label_quality="high",
    axis_months_label_height=0.4,
    axis_days_label="off",
)

# define time axis
geo_axis = mv.maxis(axis_tick_label_height=0.4)

# define line Hovmoeller view
view = mv.mhovmoellerview(
    type="line_hovm", line=line, swap_axes="yes", time_axis=time_axis, geo_axis=geo_axis
)

# define legend
legend = mv.mlegend(legend_text_font_size=0.4)

# define title
title = mv.mtext(text_font_size=0.5)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="line_hovm_era5_t850"))

# generate plot
mv.plot(view, t, t_shading, legend, title)
