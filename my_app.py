import streamlit as st
import plotly.graph_objects as go
import my_app_module as sam

st.header("Bending Moment Resistance of a Glulam Beam over a Depth Range")

st.sidebar.subheader("Parameters")
min_depth = st.sidebar.number_input("Minimum beam depth (mm)", value=215)
max_depth = st.sidebar.number_input("Maximum beam depth (mm)", value=1000)
interval = st.sidebar.number_input("Depth step interval (mm)", value=100)
L = st.sidebar.number_input("Length (mm)", value=5000)
b = st.sidebar.number_input("Width (mm)", value = 315)
d = st.sidebar.number_input("Depth (mm)", value = 720)
fb = st.sidebar.number_input("Specified bending strength (MPa)", value = 30.6)

# K Factors
st.sidebar.subheader("K Factors")
kD = st.sidebar.number_input("Load Duration Factor, kD", value=1.0)
kH = st.sidebar.number_input("System Factor, kH", value=1.0)
ksb = st.sidebar.number_input("Service Condition Factor, ksb", value=1.0)
kT = st.sidebar.number_input("Treatment Factor, kT", value=1.0)
kx = st.sidebar.number_input("Curvature Factor, kx", value=1.0)
kL = st.sidebar.number_input("Lateral Stability Factor, kL", value=1.0)

# Calculation of "resistance lines"
results = sam.bending_capacity_vs_depth(
    min_depth,
    max_depth,
    interval,
    L,
    b,
    d,
    fb,
    kD,
    kH,
    ksb,
    kT,
    kx,
    kL,
)

depth_input = st.number_input(label="Depth", min_value=min_depth, max_value=max_depth)

# Calculation of individual point for plot marker and example calculations
example_latex, factored_load = sam.calc_mr_at_given_depth(
    L, 
    b, 
    d, 
    fb,
    1.0, 
    1.0, 
    1.0,
    1.0,
    1,0,
    1,0,
    )

fig = go.Figure()

# Plot lines
fig.add_trace(
    go.Scatter(
    x=results["Glulam Beam"][1], 
    y=results["Glulam Beam"][0],
    line={"color": "red"},
    name="Glulam Beam"
    )
)

fig.add_trace(
    go.Scatter(
        y=[depth_input],
        x=[factored_load],
        name="Example Calculation: Glulam Beam Moment Resistance"
    )
)

fig.layout.title.text = "Factored moment resistance of glulam beam"
fig.layout.xaxis.title = "Factored moment resistance, KNm"
fig.layout.yaxis.title = "Depth of beam, mm"


st.plotly_chart(fig)

calc_expander_a = st.expander(label="Sample Calculation, Glulam Beam Moment Resistance")
with calc_expander_a:
    for calc in example_latex:
        st.latex(
            calc
        )