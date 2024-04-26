import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
#import fitz
#import matplotlib.pyplot as plt
import re

title_image = "./title.png"
st.image(title_image)
pio.templates.default = "plotly"

st.markdown("<div style='text-align: center; font-size: 18.4px;'><a href='https://www.li-lab-cat-design.com/'>Hao Li Lab@Advanced Institute for Materials Research (WPI-AIMR), Tohoku University, Japan</a></div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; font-size: 18.4px;'><a href='https://www.li-lab-cat-design.com/'>Please click here to access our new site", unsafe_allow_html=True)
