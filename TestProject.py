import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
from PIL import Image

@st.cache
def get_data(csv_path):
    #read data from given csv path
    data= pd.read_csv(csv_path)
    #Code from Streamlit Uber Test App for writing column names to lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

st.set_page_config(page_title="Isabel's First Project",
page_icon=':star:')
st.title("Fun Facts about Isabel")
st.write("As I introduce myself to Streamlit, I've created this page to share a bit about me.")

