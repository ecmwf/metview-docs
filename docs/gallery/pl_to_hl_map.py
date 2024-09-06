"""
GRIB - Pressure to height level interpolation
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

# get data
use_mars = False
if use_mars:
    # retrieve data from MARS

    # forecast fields on pressure levels
    fs_pl = mv.retrieve(
        type="fc",
        date=20240901,
        time=0,
        step=12,
        levtype="pl",
        levelist=[1000, 925, 850, 700, 400, 500, 300],
        param=["t", "z"],
        area=[55, -5, 46, 10],
        grid=[0.1, 0.1],
    )

else:
    # read data from GRIB file
    filename = "pl_to_hl_input.grib"
    if mv.exist(filename):
        fs_pl = mv.read(filename)
    else:
        fs_pl = mv.gallery.load_dataset(filename)

# extract pl data
t = mv.read(data=fs_pl, param="t")
z = mv.read(data=fs_pl, param="z")

# define target heights
h_levels = [100, 200, 500, 1000]

# interpolate t from pressure levels to height levels
t_h = mv.pl_to_hl(t, z, None, h_levels, "sea", "linear")

#  define contour shading
cont = mv.mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_fM48t56i4",
    legend="on",
    grib_scaling_of_derived_fields="on",
)

# define coastline
coast = mv.mcoast(map_grid_colour="charcoal", map_grid_longitude_increment=10)

# define map view
view = mv.geoview(map_area_definition="corners", area=[55, -5, 46, 10], coastlines=coast)

# create a 2x2 plot layout with the defined geoview
dw = mv.plot_superpage(pages=mv.mvl_regular_layout(view, 2, 2, 1, 1, [5, 100, 15, 100]))

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="pl_to_hl_map"))


# # build plot definition
p_def = []
for i in range(4):
    title = mv.mtext(text_lines=[f"temperature  h={h_levels[i]}m ASL"], text_font_size=0.5)
    p_def.extend([dw[i], t_h[i], cont, title])

# generate plot
mv.plot(p_def)
