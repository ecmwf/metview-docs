"""
Polar Stereographic Projection Defined by Centre and Scale
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

# define coastlines
coast = mv.mcoast(
    map_coastline_colour="charcoal",
    map_coastline_resolution="medium",
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="beige",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.8178,0.9234,0.9234)",
    map_boundaries="on",
    map_boundaries_colour="brick",
    map_boundaries_thickness=1,
    map_grid_colour="RGB(0.4,0.4,0.4)",
    map_grid_latitude_increment=5,
    map_grid_longitude_increment=10,
    map_label_height=0.35,
)

# set up the geographical area
view = mv.geoview(
    map_projection="polar_stereographic",
    map_area_definition="centre",
    map_vertical_longitude=20,
    map_centre_latitude=47,
    map_centre_longitude=20,
    map_scale=1e7,
    coastlines=coast,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="polar_with_centre_point"))

# plot the data onto the map
mv.plot(view)
