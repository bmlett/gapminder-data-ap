#app.py
import streamlit as st
import pandas as pd
import plotly.express as px
# Config page
st.set_page_config(layout='wide')
st.title("Interact with Gapminder Data")

df = pd.read_csv("Data/gapminder_tidy.csv")
# Updated version 

# add lists of continent and metric
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())
# add map for metric labels 
metric_labels={"gdpPercap": "GDP per Capita", "lifeExp": "Average Life Expectancy", "pop":"Population"}

# helper function 
def formate_metric(metric_raw):
    return metric_labels[metric_raw]

## select the contient and metric
with st.sidebar:
    st.subheader("Configure the plot")
#continent = "Europe"
    continent = st.selectbox(label = 'Choose a contnent', options = continent_list)
#metric = 'pop'
    metric = = st.selectbox(label = 'Choose a metric', options = metric_list, format_func=format_metric)

query=f"continent=='{continent}' & metric=='{metric}'"

df_filtered = df.query(query)

title=f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_gdp_o, x = "year", y="value", color='country', title=title, labels={'value':f'{metric_labels[metric]}'})

st.plotly_chart(fig, use_container_width=True)
st.markdown(f"This is a figure of {metric_labels[metric]} in the countries found in the continent region {continent}.")

show_data = True
if show_data: 
    st.dataframe(df_filtered)




## Initial pass 
#df_gdp_o = df.query("continent=='Oceania' & metric=='gdpPercap'")
#title = "GDP for countries in Oceania"
#fig = px.line(df_gdp_o, x = "year", y="value", color='country', title=title, labels={'value':'GDP Percap'})
## Stremlit app function to show fig 
#st.plotly_chart(fig, use_container_width=True)
## make figure wider --> use_container_width=True based on set_page_config 
### Exercise add caption under the figure
#st.caption('This is a figure of gdp percap in the countries found in the continent region Oceania.', unsafe_allow_html=False, *, help=None)
#st.markdown("This is a figure of gdp percap in the countries found in the continent region Oceania.")
### Exercise disply the data from plot
#st.write(df_gdp_o)
#st.dataframe(df_gdp_o)

