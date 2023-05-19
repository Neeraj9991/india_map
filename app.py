import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

sheet_id = '1dSLYc8HggtZy-Liji30eBydU4WhFUVgMaZQV3JCP2_U'
df = pd.read_csv(
    f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

states_list = list(df['State'].unique())
states_list.insert(0, 'Overall India')

st.sidebar.title('India Data')

selected_state = st.sidebar.selectbox('Select a state', states_list)
primary = st.sidebar.selectbox(
    'Select primary parameter', list(df.columns[5:]))
secondary = st.sidebar.selectbox(
    'Select secondary parameter', list(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Colour represents secondary parameter')

    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=4, size_max=40,width=1200, height=700, size=primary, color=secondary, mapbox_style='carto-positron', hover_name='District')

        st.plotly_chart(fig, use_container_width=True)

    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, size_max=40,width=1200, height=700, size=primary, color=secondary, mapbox_style='carto-positron', hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
