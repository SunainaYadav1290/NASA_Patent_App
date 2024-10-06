
import streamlit as st
import pandas as pd
import numpy as np
import requests

import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
# Assuming you've extracted the NASA patent data and saved it as a CSV or you can load it directly from a DataFrame

def fetch_nasa_data(api_endpoint):
    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_endpoint)
        response.raise_for_status()
        # Parse the response data (assuming JSON)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
# Define the API endpoint for NASA data
api_endpoint = "https://data.nasa.gov/resource/gquh-watm.json"
data = fetch_nasa_data(api_endpoint)
print(data)
df=pd.DataFrame(data)

# Streamlit App Title

#st.title('NASA Patent Data Analysis')
st.markdown("<h1 style='text-align: center; color: white; background-color: Coral; padding: 10px; border-radius: 10px;'>NASA Patent Data Analysis</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

col1,col2=st.columns([1.05,2.95])
with col2:
  data1=pd.read_csv(r"C:\Users\shaur\OneDrive\Desktop\cccc\mydata.csv")
  df1=pd.DataFrame(data1)
  df1 = df1.sort_values(by='Issued_Patents', ascending=False)
  st.write('&nbsp;&nbsp;Total Issued Patents By Center')
  fig = px.bar(df1, x='center', y='Issued_Patents',
             labels={'center': 'Center', 'Issued_Patents': 'Issued Patents'},
             color_discrete_sequence=["Coral", "Coral", "Coral", "Coral"])
# Display the chart in Streamlit
  st.plotly_chart(fig, use_container_width=True)
with col1:
  
  st.subheader("&nbsp;Patents Status")
  st.metric("&nbsp;Issued", " 64.50%")
  st.metric("&nbsp;Pending", " 35.50%")
  st.write("___________________")
  st.metric("Patent Issuance Ranking", "#1", delta="Top in Innovation")
  
from rich import print

# Create a vertical line
print("[coral]━━━━━━━━━━━━━━━━━━━[/coral]")
st.markdown("""
    <style>
        [data-testid="column"]:nth-child(1){
            background-color: #494949;
        }
    </style>
""", unsafe_allow_html=True)

# Show raw data
if st.checkbox('Show Patents data'):
    st.write("")
    st.write("")
    st.write(df)
if st.checkbox('Show Summary Statistics'):
    st.subheader('Summary Statistics')
    st.write(df.describe())

# Summary statistics
 
 

# Data filtering by status
status_options = df['status'].unique()
selected_status = st.selectbox('Filter by Patent Status:', status_options)
filtered_data = df[df['status'] == selected_status]
st.write(filtered_data)






