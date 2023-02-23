import streamlit as st
import pandas as pd
from backend import build_merit_function
from PIL import Image

st.title('Zemax Merit Function Builder')
col01,col02=st.columns(2)
col01.markdown('''
Generate a merit function to fit the lens Power Profile.
A power profile file, in CSV file format, is required.

* First Column: position
* Second Column: power
* No header
''')
col02.image(image=Image.open('demo.png'), caption="CSV demo", width=275)
power_profile_file=st.file_uploader("Upload Power Profile file", type="csv")
if power_profile_file is not None:
    power_profile=pd.read_csv(power_profile_file, header=None)


col1,col2,col3,col4,col5=st.columns(5)

lens_front_rowIndex=col1.number_input("Lens Front Row Index", value=1)
lens_back_rowIndex=col2.number_input("Lens Back Row Index", value=2)

lens_diameter=col3.number_input("Lens Diameter", value=6.0)

thickness_min=col4.number_input("Thickness Min", value=0.05)
thickness_max=col5.number_input("Thickness Max", value=0.5)

if_1st_differential=st.checkbox("Fit 1st Differential", value=True)

col11,col12,col13=st.columns(3)
thickness_weight=col11.number_input("Thickness Weight", value=1.0)
power_weight=col12.number_input("Power Weight", value=1.0)
if if_1st_differential:
    differential_weight=col13.number_input("Differential Weight", value=1.0)

build_button=st.button("Build Merit Function")
MF_file=None
if build_button and power_profile_file is not None:
    MF_file=build_merit_function(
        power_profile, 
        lens_front_rowIndex,
        lens_back_rowIndex,

        lens_diameter,
        thickness_min, 
        thickness_max, 
        
        if_1st_differential)

if MF_file is not None:
    st.download_button("Dowload Merit Function", MF_file, file_name="MeritFunction.MF")
