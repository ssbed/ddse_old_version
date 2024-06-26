import streamlit as st
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

title_image = "./title.png"
st.image(title_image)
pio.templates.default = "plotly"
finger_ion = "👉"

st.markdown("<div style='text-align: center; font-size: 18.4px;'><a href='https://www.li-lab-cat-design.com/'>Hao Li Lab@Advanced Institute for Materials Research (WPI-AIMR), Tohoku University, Japan</a></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: left; font-size: 30px; color: red;'>Please click <a href='https://ddse-database.streamlit.app/'>here</a> to access our new site</div>", unsafe_allow_html=True)
