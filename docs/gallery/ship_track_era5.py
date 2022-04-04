"""
GRIB - ERA5 Data Along Ship Track
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
import numpy as np


def extract_scalar(track_lats, track_lons, track_dates, fs, param):
    """Extract scalar GRIB data along track as geopoints"""
    fs_p = fs.select(shortName=param)
    fs_dates = fs_p.valid_date()
    vals = []
    track_idx = []
    for i in range(len(track_dates)):
        try:
            fs_idx = fs_dates.index(track_dates[i])
            vals.append(fs_p[fs_idx].nearest_gridpoint(track_lats[i], track_lons[i]))
            track_idx.append(i)
        except:
            pass

    gpt = mv.create_geo(
        type="standard",
        latitudes=np.array([track_lats[x] for x in track_idx]),
        longitudes=np.array([track_lons[x] for x in track_idx]),
        values=np.array(vals),
        dates=[track_dates[x] for x in track_idx],
        times=[mv.hour(track_dates[x]) for x in track_idx],
    )

    return gpt


def extract_vector(track_lats, track_lons, track_dates, fs, param):
    """Extract vector GRIB data along track as geopoints"""
    fs_u = fs.select(shortName=param[0])
    fs_v = fs.select(shortName=param[1])
    fs_dates = fs_u.valid_date()
    vals_u = []
    vals_v = []
    track_idx = []
    for i in range(len(track_dates)):
        try:
            fs_idx = fs_dates.index(track_dates[i])
            vals_u.append(fs_u[fs_idx].nearest_gridpoint(track_lats[i], track_lons[i]))
            vals_v.append(fs_v[fs_idx].nearest_gridpoint(track_lats[i], track_lons[i]))
            track_idx.append(i)
        except:
            pass

    gpt = mv.create_geo(
        type="xy_vector",
        latitudes=np.array([track_lats[x] for x in track_idx]),
        longitudes=np.array([track_lons[x] for x in track_idx]),
        values=np.array(vals_u),
        value2s=np.array(vals_v),
        dates=[track_dates[x] for x in track_idx],
        times=[mv.hour(track_dates[x]) for x in track_idx],
    )

    return gpt


# getting the data
use_cds = False

filename_grib = "ship_track_era5.grib"
filename_track = "ship_track.gpt"

# getting ERA5 data from CDS
if use_cds:
    import cdsapi

    c = cdsapi.Client()
    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "format": "grib",
            "variable": [
                "10m_u_component_of_wind",
                "10m_v_component_of_wind",
                "significant_height_of_combined_wind_waves_and_swell",
            ],
            "year": "2020",
            "month": "11",
            "day": [
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
            ],
            "time": [
                "03:00",
                "07:00",
                "10:00",
                "13:00",
                "14:00",
                "16:00",
                "20:00",
            ],
            "area": [
                55,
                -45,
                25,
                5,
            ],
        },
        filename_grib,
    )
    g = mv.read(filename_grib)
# read GRIB data from file
else:
    if mv.exist(filename_grib):
        g = mv.read(filename_grib)
    else:
        g = mv.gallery.load_dataset(filename_grib)


# get track data as Geopoints
if mv.exist(filename_track):
    track_gpt = mv.read(filename_track)
else:
    track_gpt = mv.gallery.load_dataset(filename_track)

# extract track details
track_lats = track_gpt.latitudes()
track_lons = track_gpt.longitudes()
track_dates = track_gpt.dates()
track_idx = [x for x in range(len(track_dates))]

# extract wave height along the track
gpt_sc = extract_scalar(track_lats, track_lons, track_dates, g, "swh")

# extract wind along the track
gpt_wind = extract_vector(track_lats, track_lons, track_dates, g, ["10u", "10v"])

# define track line plotting
track_line_vd = mv.mgraph(graph_line_colour="chestnut", graph_line_thickness=2)

track_line_vis = mv.input_visualiser(
    input_plot_type="geo_points",
    input_longitude_values=gpt_sc.longitudes(),
    input_latitude_values=gpt_sc.latitudes(),
)

# define track date label plotting

# only extracts labels for the first date per day
label_vals = []
label_idx = []
prev_day = None
for i, d in enumerate(track_dates):
    if d.day is None or d.day != prev_day:
        label_vals.append(d.strftime("%d/%H"))
        label_idx.append(i)
        prev_day = d.day

# define visdef for labels
track_label_vd = mv.msymb(
    legend="off",
    symbol_type="text",
    symbol_table_mode="advanced",
    symbol_advanced_table_selection_type="list",
    symbol_advanced_table_level_list=[*label_idx, label_idx[-1] + 1],
    symbol_advanced_table_height_list=0.01,
    symbol_advanced_table_text_list=label_vals,
    symbol_advanced_table_text_font_size=0.4,
    symbol_advanced_table_text_font_style="bold",
    symbol_advanced_table_text_font_colour="navy",
    symbol_advanced_table_text_display_type="right",
)

# define visualiser for labels. Add an offset to coordinates
label_offset = 0.5
track_label_vis = mv.input_visualiser(
    input_plot_type="geo_points",
    input_longitude_values=track_lons[label_idx] + label_offset,
    input_latitude_values=track_lats[label_idx] - label_offset,
    input_values=label_idx,
)

# define wind plotting
wind_plotting = mv.mwind(
    wind_field_type="flags",
    wind_thinning_factor=1.0,
    wind_flag_calm_indicator="off",
    wind_flag_calm_below=0.1,
    wind_flag_colour="black",
    wind_flag_length=0.8,
    wind_flag_origin_marker="off",
)

# define simbol plotting for the wave height
symbol_plotting = mv.msymb(
    legend="on",
    symbol_type="marker",
    symbol_table_mode="advanced",
    symbol_outline="on",
    symbol_outline_colour="RGB(0.5804,0.5804,0.5804)",
    symbol_advanced_table_selection_type="list",
    symbol_advanced_table_level_list=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
    symbol_advanced_table_max_level_colour="red",
    symbol_advanced_table_min_level_colour="blue",
    symbol_advanced_table_colour_direction="clockwise",
    symbol_advanced_table_marker_list=19,
    symbol_advanced_table_height_list=0.7,
)

# define coastlines
land_sea_shade = mv.mcoast(
    map_coastline_land_shade="on",
    map_coastline_land_shade_colour="RGB(0.8,0.8,0.8)",
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="RGB(0.9236,0.9317,0.9352)",
    map_grid_longitude_increment=10,
)

# define view
view = mv.geoview(
    map_area_definition="corners", area=[25, -35, 52, 3], coastlines=land_sea_shade
)

# define legend
legend = mv.mlegend(legend_units_text="m", legend_text_font_size=0.3)

# define title
title = mv.mtext(
    text_lines="ERA5 wave height (m) and 10m wind along ship track",
    text_font_size=0.5,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="ship_track_era5"))

# generate plot
mv.plot(
    view,
    track_line_vis,
    track_line_vd,
    track_label_vis,
    track_label_vd,
    gpt_sc,
    symbol_plotting,
    gpt_wind,
    wind_plotting,
    title,
    legend,
)
