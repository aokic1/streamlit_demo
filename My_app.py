import streamlit as st
import numpy as np
import pandas as pd

st.header("My app")
st.write("Welcome to my new app!")

import sklearn.datasets as datasets

tab1, tab2, tab3 = st.tabs(['Data', 'Plotly Charts', 'Upload data'])

with tab1:


    data = datasets.load_iris()
    # st.write(data)
    st.info("This is dataframe overview of the data.")
    df = pd.DataFrame(data=data['data'], columns=data['feature_names'])
    df

with tab2:
    import plotly_express as px

    x_axis = st.selectbox("Select x-axis:", df.columns.values)
    y_axis = st.selectbox("Select y-axis:", df.columns.values)

    fig = px.scatter(data_frame=df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)

with tab3:
    uploaded_data = st.file_uploader("Upload data: ", type=['csv', 'xlsx'])

    if uploaded_data:
        st.write(pd.read_csv(uploaded_data))
    else:
        st.warning("**File Not uploaded! Please upload it to continue!**")
        st.write("Testing!")