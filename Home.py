from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("Yonlada")
st.image("./pic/beam.jpg")

with col1:
   st.header("Versicolor")
   st.image("./pic/iris1.jpg")

with col2:
   st.header("Verginiga")
   st.image("./pic/iris2.jpg")

with col3:
   st.header("Setosa")
   st.image("./pic/iris3.jpg")