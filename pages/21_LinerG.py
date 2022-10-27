import streamlit as st
import pandas as pd
import numpy as np
dataset=st.file_uploader("Dataset")
if dataset is not None:
    dataframe = pd.read_csv(dataset)
    if st.button("View dataset"):
        d=st.write(dataframe)
        if st.button("Close View"):
            d=st.close()
st.write("**Input Feature**")
if dataset is not None:
    a = dataframe.columns.values
    col= st.columns(np.shape(a)[0])
    cb=[None]*np.shape(a)[0]
    b=0
    while b<np.shape(a)[0]-1:
        with col[b]:
            cb[b]=st.checkbox(a[b])
        b=b+1
    st.write("**Output**")
    st.checkbox(a[b],value=True,disabled=True)
    st.write("**Train/Test Split**")
    split = st.slider('v', 0, 100,80,label_visibility="hidden")
    col2=st.columns([2,1,1])
    with col2[0]: kfold= st.checkbox("KFold")
    if kfold:
        with col2[1]: st.write("**K_value=**")
        with col2[2]:
            kfnum=st.number_input("K:",step=1,min_value=1,label_visibility="collapsed")
    st.button("Run")




