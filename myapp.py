
import streamlit as st
import pandas as pd
import requests
import plotly.express as px



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


data1=pd.read_csv(r"C:\Users\shaur\OneDrive\Desktop\cccc\mydata.csv")
df1=pd.DataFrame(data1)
df1 = df1.sort_values(by='Issued_Patents', ascending=False)
col1,col2 = st.columns([0.55,1.45])
with col2: 
 st.write('&nbsp;&nbsp;Total Issued Patents By Center')
 fig = px.bar(df1, x='center', y='Issued_Patents',
             labels={'center': 'Center', 'Issued_Patents': 'Issued Patents'},
             color_discrete_sequence=["Coral", "Coral", "Coral", "Coral"])
# Display the chart in Streamlit
 st.plotly_chart(fig, use_container_width=True)

with col1:  
 with st.container(height=300,border=True):
  st.write("&nbsp;&nbsp;&nbsp;Patents Status")
  st.write("&nbsp;Issued -", " 64.50%")
  st.write("&nbsp;Pending -", " 35.50%")
  st.write(" Patent Issuance #1 Ranking-")
  st.write("&nbsp;NASA Langley Research")
  

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






