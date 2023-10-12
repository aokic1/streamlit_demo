import streamlit as st
import sklearn.datasets as datasets
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px

st.header("This is data visualization web app!")

tab1, tab2 = st.tabs(["Data", "Graphs"])


with tab1:
    st.info("This is a Dataset:")



    data = datasets.load_iris()

    df = pd.DataFrame(data = data.data, columns = data.feature_names)
    st.write(df)

with tab2:
    x_axis = st.selectbox("Select x-axis:", df.columns.values)
    y_axis = st.selectbox("Select y-axis:", df.columns.values)

    if x_axis and y_axis:
        fig = px.scatter(data_frame=df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

# st.sidebar("")