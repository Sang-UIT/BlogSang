
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
import csv

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold

def mean_squared_error(y_true, y_pred):
      return np.mean((y_true - y_pred) ** 2)
dataset=st.file_uploader("Dataset")
if dataset is not None:
    dataframe = pd.read_csv(dataset)
    if st.button("View dataset"):
        d=st.write(dataframe)
        st.button("Close View")
    a = dataframe.columns.values
    col= st.columns(np.shape(a)[0])
    cb=[None]*np.shape(a)[0]
st.write("**Input Feature**")
if dataset is not None:
    b=0
    while b<np.shape(a)[0]-1:
        with col[b]:
            cb[b]=st.checkbox(a[b])
        b=b+1
    st.write("**Output**")
    st.checkbox(a[b],value=True,disabled=True)
    st.write("**Train/Test Split**")
    aa=False
    split = st.slider('v', 10, 100,80,label_visibility="hidden",disabled =aa,step =10)
    col2=st.columns([2,1,1])
    with col2[0]: kfold= st.checkbox("KFold")
    if kfold:
        with col2[1]: st.write("**K_value=**")
        with col2[2]:
            kfnum=st.number_input("K:",step=1,min_value=2,label_visibility="collapsed")
    
    if st.button("Run"):
        b=0
        bb=0
        data = dataframe.to_numpy()
        while b<np.shape(a)[0]-1:
            if not(cb[b]):
                data = np.delete(data,bb,axis=1)
                bb=bb-1
            b=b+1
            bb=bb+1
        b=0
        n= data.shape[1]
        y = data[:,n-1]
        x= np.delete(data,n-1,axis=1)
        #scale= StandardScaler()
        #x= scale.fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(
        x, y, train_size=split/100, random_state=1234)
        model_ne = LinearRegression() # MLE
        if not(kfold):
            model_ne.fit(x_train,y_train)
            y_pre=model_ne.predict(x_test)
            mse = mean_squared_error(y_test, y_pre)
            mae = mean_absolute_error(y_test, y_pre)
            st.write("MSE:", mse)
            st.write("MSE:", mae)
            accu = r2_score(y_test, y_pre)
            st.write("Accuracy:", accu)
        else:
            kf = KFold(n_splits=kfnum)
            kf.get_n_splits(x)
            cv = KFold(n_splits=kfnum, random_state=1, shuffle=True)
            coll = st.columns(3)
            with coll[0]:
                st.write("**Scores**")
                scores = cross_val_score(model_ne, x, y, scoring='r2', cv=cv)
                st.write(scores)
            with coll[1]:
                st.write("**MSE**")
                mse = -1*cross_val_score(model_ne, x, y, scoring='neg_mean_squared_error', cv=cv)
                st.write(mse)
            with coll[2]:
                st.write("**MAE**")
                mae = -1*cross_val_score(model_ne, x, y, scoring='neg_mean_absolute_error', cv=cv)
                st.write(mae)


