"""
This is a simple example dashboard on Kenyan Employment Data and Labor force
Link to the deployed steeamlit application - https://employment-trends-analysis-dashboard-knpdpxybknqhnwduu8bnpq.streamlit.app/

"""
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/FazeJ99/Employment-trends-Analysis-Dashboard/refs/heads/main/dataset.csv')

data = load_data()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard on Kenyan Employment Data")
st.write("This is a simple example dashboard on Kenyan Employment Data and Labor force")

# Sidebar for selection
st.sidebar.title("Select a Visual")
visualization_options = [
    "Unemployment Rate Over Time by Sex and Age Group",
    "Total Employed Population by Age Group across the employed",
    "Population Pyramid of the Total Population by Age Group and Sex",
    "Sector-Wise Employment Over Time",
    "Inactive Population vs Unemployed Population Over Time",
    "Distribution of Unemployed Population by Age Group",
    "Employment Distribution Across Sectors",
    "Distribution of Unemployment Rate",
    "Unemployment Rate by Age Group"
]

selected_visualization = st.sidebar.selectbox("Choose a visual from the sidebar below", visualization_options)

# Display the selected visualization
if selected_visualization == "Unemployment Rate Over Time by Sex and Age Group":
    fig = px.line(data, 
                   x='year', 
                   y='ILO_unemployed_rate', 
                   color='sex', 
                   line_group='age_group', 
                   title='Unemployment Rate Over Time by Sex and Age Group', 
                   labels={'ILO_unemployed_rate':'Unemployment Rate (%)', 'year':'Year'},
                   markers=True)
    st.plotly_chart(fig)

elif selected_visualization == "Total Employed Population by Age Group across the employed":
    fig2 = px.bar(data, 
                   x='age_group', 
                   y='total_employed_population', 
                   title='Total Employed Population by Age Group across the employed',
                   color='sex',
                   labels={'total_employed_population': 'Total Employed Population', 'age_group': 'Age Group'})
    st.plotly_chart(fig2)

elif selected_visualization == "Population Pyramid of the Total Population by Age Group and Sex":
    fig3 = px.bar(data, 
                  x='population', 
                  y='age_group', 
                  color='sex', 
                  orientation='h', 
                  title='Population Pyramid of the Total Population by Age Group and Sex', 
                  labels={'population':'Population', 'age_group':'Age Group'})
    st.plotly_chart(fig3)

elif selected_visualization == "Sector-Wise Employment Over Time":
    sectors = ['Human health', 'Arts $ entertainment', 'Other services', 'Activities of households']
    fig4 = px.bar(data, 
                  x='year', 
                  y=sectors, 
                  title='Sector-Wise Employment Over Time', 
                  labels={'value':'Employment', 'year':'Year'},
                  barmode='stack')
    st.plotly_chart(fig4)

elif selected_visualization == "Inactive Population vs Unemployed Population Over Time":
    fig5 = px.bar(data, 
                  x='year', 
                  y=['total_inactive_population', 'total_unemployed_population'], 
                  barmode='group',
                  title='Inactive Population vs Unemployed Population Over Time',
                  labels={'value':'Population', 'year':'Year'})
    st.plotly_chart(fig5)

elif selected_visualization == "Distribution of Unemployed Population by Age Group":
    fig6 = px.pie(data, 
                  names='age_group', 
                  values='total_unemployed_population', 
                  title='Distribution of Unemployed Population by Age Group',
                  labels={'total_unemployed_population':'Total Unemployed Population'})
    st.plotly_chart(fig6)

elif selected_visualization == "Employment Distribution Across Sectors":
    sectors = ['Human health', 'Arts $ entertainment', 'Other services', 'Activities of households']
    total_employment = data[sectors].sum()
    fig8 = px.pie(values=total_employment, 
                  names=sectors, 
                  title='Employment Distribution Across Sectors',
                  hole=0.4)
    st.plotly_chart(fig8)

elif selected_visualization == "Distribution of Unemployment Rate":
    fig10 = px.histogram(data, 
                         x='ILO_unemployed_rate', 
                         title='Distribution of Unemployment Rate',
                         labels={'ILO_unemployed_rate':'Unemployment Rate (%)'},
                         nbins=20)
    st.plotly_chart(fig10)

elif selected_visualization == "Unemployment Rate by Age Group":
    fig11 = px.box(data, 
                   x='age_group', 
                   y='ILO_unemployed_rate', 
                   color='age_group', 
                   title='Unemployment Rate by Age Group',
                   labels={'ILO_unemployed_rate':'Unemployment Rate (%)', 'age_group':'Age Group'})
    st.plotly_chart(fig11)
