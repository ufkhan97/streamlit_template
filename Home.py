import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import utils

st.set_page_config(
    page_title="Gitcoin Data Analysis",
    page_icon="assets/favicon.png",
    layout="wide",
    menu_items={
        'Report a bug': "https://www.github.com/ufkhan97/streamlit_template/issues", # REPLACE WITH YOUR REPO URL
        'About': "## This is a template for Gitcoin Streamlit apps!" # REPLACE WITH YOUR DESCRIPTION
    }
)

st.image('assets/GITCOIN-Logotype-Dark.png', width = 300)
st.header("🎉 Congrats! You deployed the template! Now let's fill it in like a mad lib!")


