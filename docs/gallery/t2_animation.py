"""
T2m Animated GIF
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

import os
import metview as mv

# getting data (forecast steps up to 72h)
use_mars = False

filename = "t2_global_fc_72h.grib"

# getting forecast data from MARS
if use_mars:
    f = mv.retrieve(
        type="fc",
        levtype="sfc",
        param="2t",
        date=20221002,
        time=0,
        step=list(range(0, 78, 6)),
        grid=[2, 2],
    )

    mv.write(filename, f)
# read data from file or fetch from download server
else:
    if mv.exist(filename):
        f = mv.read(filename)
    else:
        f = mv.gallery.load_dataset(filename)

# define our plotting attributes
t_shade = mv.mcont(legend="on", contour_automatic_setting="ecchart")

# define view
view = mv.geoview(area_mode="name", area_name="pacific")

# define postscript output
# (will contain one page per timestep)
out_basename = "t2_animation"
mv.setoutput(mv.ps_output(output_name=f"{out_basename}"))

# generate plot
mv.plot(view, f, t_shade)

# convert ps file to animated gif using imagemagick
# with a 100ms pause between frames
ps_file = f"{out_basename}.ps"
gif_file = f"{out_basename}.gif"
os.system(rf"""convert -delay 100 -rotate "90<" {ps_file} {gif_file}""")
