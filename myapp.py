
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime

st.set_page_config(layout="wide")
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


data1=pd.read_csv(r"mydata.csv")
df1=pd.DataFrame(data1)
df1 = df1.sort_values(by='Issued_Patents', ascending=True)

col1,col2,col3 = st.columns([0.3,0.3,0.3])

with col1:
 with st.container(height=400,border=True):
  
  fig = px.bar(df1, x='Issued_Patents', y='center',
             labels={'center': 'Center', 'Issued_Patents': 'Number of Patents Issued'},
             color_discrete_sequence=["Coral"])
# Display the chart in Streamlit
  fig.update_layout(title=dict(
        text='Total Patents Issued by each Center',  # Title text
        font=dict(size=25, color='Coral')  # Set font size and color
    ),
    height=360,  
    width=500, 
    margin=dict(l=20, r=20, t=30, b=20),
    font=dict(size=25),
     yaxis=dict(
        title=dict(font=dict(size=18)),  # Font size for the y-axis title
        tickfont=dict(size=18)           # Font size for y-axis tick labels
    ),
     xaxis=dict(
        title=dict(font=dict(size=18)),  # Font size for the y-axis title
        tickfont=dict(size=18)           # Font size for y-axis tick labels
    )
) 
 
  st.plotly_chart(fig, use_container_width=True)
with col2:
  df_status = pd.read_csv('output1.csv')  # Replace 'filename.csv' with the path to your file
  with st.container(height=400,border=True):
    fig1 = px.pie(df_status,
    names='status',  
    values='count',   
    title='Patents Status', 
    color_discrete_sequence=px.colors.sequential.RdBu  # Custom color palette
)

# Display the pie chart in Streamlit
    fig1.update_layout(title=dict(
        text='Patents Status',  # Title text
        font=dict(size=25, color='Coral')) ,
    height=360,  
    width=400, 
    margin=dict(l=20, r=20, t=30, b=20),
    font=dict(size=18)
     )
    st.plotly_chart(fig1)

with col3:
 df_cat = pd.read_csv('output2.csv') 
 df_cat = df_cat.sort_values(by='count', ascending=True)
 with st.container(height=400,border=True):
  
  fig3 = px.bar(df_cat, x='count', y='Patent_Category',
             labels={'count': 'Number of Patents', 'Patents Categories': 'Patent_Category'},
             color_discrete_sequence=["Coral"])
# Display the chart in Streamlit

  fig3.update_layout(title=dict(
        text='Total Patents by Category',  # Title text
        font=dict(size=25, color='Coral')) ,
    height=370,  
    width=400, 
    margin=dict(l=20, r=20, t=30, b=20),
    font=dict(size=30),
     yaxis=dict(
        title=dict(font=dict(size=18)),  # Font size for the y-axis title
        tickfont=dict(size=18)           # Font size for y-axis tick labels
    ),
     xaxis=dict(
        title=dict(font=dict(size=18)),  # Font size for the y-axis title
        tickfont=dict(size=18)           # Font size for y-axis tick labels
    )
)
  st.plotly_chart(fig3, use_container_width=True)
  

  

  

st.markdown("""
    <style>
        [data-testid="column"]:nth-child(1){
            background-color: #494949;
        }
    </style>
""", unsafe_allow_html=True)
# Patents expiring soon
df['patent_expiration_date']=pd.to_datetime(df['patent_expiration_date'])


st.write('Patents Expiring in 2024:')

df_exp = df[(df['status'] == 'Issued') & (df['patent_expiration_date'].dt.year == 2024)]

df_html = df_exp.to_html(index=False)
st.write(df_html, unsafe_allow_html=True)

df_catt = pd.read_csv('output4.csv') 
    
     
selected_cat = st.selectbox('Filter Patents by Patent Category:',df_catt['Patent_Category'])
filtered_dat = df_catt[df_catt['Patent_Category'] == selected_cat]
small_df=filtered_dat.head(5)
    
    
    # Display the table

st.dataframe(small_df)







 
 

# Data filtering by status
status_options = df['status'].unique()
selected_status = st.selectbox('Filter by Patent Status:', status_options)
filtered_data = df[df['status'] == selected_status]
st.write(filtered_data)
# Show raw data
if st.checkbox('Show Patents data'):
      st.write("")
      st.write("")
      st.write(df)
if st.checkbox('Show Summary Statistics'):
      st.subheader('Summary Statistics')
      st.write(df.describe())
     






