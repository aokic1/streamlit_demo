import streamlit as st

st.write("This our first web app!")

from sklearn import datasets

data = datasets.load_iris()

tab1, tab2 = st.tabs(["Data", "Graphs"])

# st.write(data)
import pandas as pd
df = pd.DataFrame(data=data.data, columns=data.feature_names)


with tab1:

    df


with tab2:
    import plotly_express as px
    x = st.selectbox("Insert X axis:", df.columns.values)
    y = st.selectbox("Insert Y axis:", df.columns.values)

    fig = px.scatter(data_frame=df, x=x, y=y)

    st.plotly_chart(fig)