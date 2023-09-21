import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

from utils import read_poverty_df

df = read_poverty_df("DP_LIVE_21092023020240010.csv")

st.subheader("Ratio de pobreza")

age = st.selectbox("Seleccione la edad", options=df["Edad"].unique())

df = df.loc[df["Edad"] == age] 

fig = px.line(x=df["Año"], y=df["Valor"], color=df["País"],
            labels={
                "x" : "Año",
                "y" : "Ratio de pobreza",
                "color" : "País"
            })

st.plotly_chart(fig)

st.subheader("Gap de pobreza por edad para un pais")

df2 = read_poverty_df("DP_LIVE_21092023020729129.csv")

pais = st.selectbox("Seleccione los paises a visualizar", options=df2["País"].unique())

df2 = df2.loc[df2["País"] == pais]

fig = px.line(x=df2["Año"], y=df2["Valor"], color=df2["Edad"],
            labels={
                "x" : "Año",
                "y" : "Ratio de desigualdad",
                "color" : "Edad",
            },
            title=f"Ratio de desigualdad por edad para {pais}"
            )

st.plotly_chart(fig)

st.subheader("Gap de pobreza por pais para adultos")

df3 = read_poverty_df("DP_LIVE_21092023020729129.csv")

df3 = df3.loc[df3["Edad"] == "adulto"]

paises = st.multiselect("Seleccione los paises a visualizar", options=df3["País"].unique(), default=["MEX"])

df3 = df3.loc[df3["País"].isin(paises)]

fig = px.line(x=df3["Año"], y=df3["Valor"], color=df3["País"],
            labels={
                "x" : "Año",
                "y" : "Ratio de desigualdad",
                "color" : "País",
            },
            title=f"Ratio de desigualdad para adultos en {', '.join(paises)}"
            )

st.plotly_chart(fig)

