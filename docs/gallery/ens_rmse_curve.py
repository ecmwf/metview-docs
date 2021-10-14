"""
GRIB - ENS RMSE Curve 
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

# getting data
use_mars = False

# getting forecast data from MARS
if use_mars:
    ret_core = {
        "date": 20171016,
        "time": 0,
        "param": "z",
        "step": list(range(0, 132, 12)),
        "levtype": "pl",
        "levelist": 500,
        "grid": [0.5, 0.5],
        "area": [45, -10, 55, 5],
    }

    # perturbed ENS members
    pf = mv.retrieve(stream="enfo", type="pf", number=list(range(1, 51)), **ret_core)

    # control member
    cf = mv.retrieve(stream="enfo", type="cf", **ret_core)

    # high-res deterministic
    hr = mv.retrieve(type="fc", **ret_core)

    # analysis
    ret_core["date"] = mv.valid_date(
        base=mv.date(20171016), step=list(range(0, 132, 24))
    )
    ret_core["time"] = [0, 12]
    ret_core["step"] = 0
    an = mv.retrieve(type="an", **ret_core)
    an = an[:-1]

    f = mv.merge(pf, cf, hr, an)

# read data from file
else:
    filename = "ens_z_rmse.grib"
    if mv.exist(filename):
        f = mv.read(filename)
    else:
        f = mv.gallery.load_dataset(filename)

# define colours for the curves
col_pert = "RGB(0.3,0.3,0.3)"
col_control = "RED"
col_oper = col_control
col_mean = "BLUE"

# define the steps we have in fc and ens
steps = list(range(0, 132, 12))

# extract the fields
en = f.select(type=["cf", "pf"])
fc = f.select(type="fc")
an = f.select(type="an")

# get metadata for the title
meta = mv.grib_get(fc[0], ["name", "level", "date", "time"])[0]

# get the valid times for the time series points
d_times = mv.valid_date(fc)

# the plot objects will be added to this list
gr_lst = []

# ens - perturbed forecast members
for i in range(1, 51):
    d = en.select(type="pf", number=i)
    d = mv.sqrt(mv.integrate((d - an) ** 2))
    d = np.array(d) / (9.81 * 10)  # scale to dkm

    gr_lst.append(
        mv.input_visualiser(
            input_x_type="date", input_date_x_values=d_times, input_y_values=d
        )
    )
    # we only add legend to one of the pf members
    if i == 1:
        pf_style = mv.mgraph(
            graph_line_thickness=1,
            graph_line_colour=col_pert,
            legend="on",
            legend_user_text="PF",
        )
    else:
        pf_style = mv.mgraph(
            graph_line_thickness=1, graph_line_colour=col_pert, legend="off"
        )
    gr_lst.append(pf_style)

# ens mean
en_mean = mv.Fieldset()
for s in steps:
    en_mean.append(mv.mean(en.select(step=s)))

d = mv.sqrt(mv.integrate((en_mean - an) ** 2))
d = np.array(d) / (9.81 * 10)  # scale to dkm
gr_lst.append(
    mv.input_visualiser(
        input_x_type="date", input_date_x_values=d_times, input_y_values=d
    )
)

mean_style = mv.mgraph(
    graph_line_thickness=4,
    graph_line_colour=col_mean,
    graph_line_style="solid",
    legend="on",
    legend_user_text="ENS Mean",
)

gr_lst.append(mean_style)

# ens - control forecast member
d = f.select(type="cf")
d = mv.sqrt(mv.integrate((d - an) ** 2))
d = np.array(d) / (9.81 * 10)  # scale to dkm
gr_lst.append(
    mv.input_visualiser(
        input_x_type="date", input_date_x_values=d_times, input_y_values=d
    )
)

cf_style = mv.mgraph(
    graph_line_thickness=4,
    graph_line_colour=col_control,
    graph_line_style="dash",
    legend="on",
    legend_user_text="Control",
)

gr_lst.append(cf_style)

# high res forecast
d = mv.sqrt(mv.integrate((fc - an) ** 2))
d = np.array(d) / (9.81 * 10)  # scale to dkm
gr_lst.append(
    mv.input_visualiser(
        input_x_type="date", input_date_x_values=d_times, input_y_values=d
    )
)
gr_lst.append(
    mv.mgraph(
        graph_line_thickness=4,
        graph_line_colour=col_oper,
        graph_line_style="solid",
        legend="on",
        legend_user_text="OPER",
    )
)

# set up the Cartesian view to plot into
# including customised axes so that we can change the size
# of the labels and add titles
haxis = mv.maxis(
    axis_type="date",
    axis_tick_size=0.4,
    axis_date_type="days",
    axis_years_label_height=0.3,
    axis_months_label_height=0.3,
    axis_days_label_height=0.4,
    axis_hours_label="on",
    axis_hours_label_colour="white",
    axis_hours_label_height=0.3,
    axis_tip_title="on",
    axis_minor_tick="on",
    axis_minor_tick_count=4,
)

vaxis = mv.maxis(
    axis_title_text="dkm", axis_title_height=0.5, axis_tick_label_height=0.4
)

view = mv.cartesianview(
    x_automatic="on",
    x_axis_type="date",
    y_automatic="on",
    horizontal_axis=haxis,
    vertical_axis=vaxis,
)

# define legend
legend = mv.mlegend(legend_display_type="disjoint", legend_text_font_size=0.4)

# define title
title = mv.mtext(
    text_lines=f"RMSE {meta[0]} {meta[1]} hPa Run: {meta[2]} {meta[3]} UTC",
    text_font_size=0.5,
)

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="ens_rmse_curve"))

# plot everything into the Cartesian view
mv.plot(view, gr_lst, legend, title)
