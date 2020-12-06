import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit入門')

st.write('DateFlame')

#データフレーム読み込み
df = pd.DataFrame([[1,2,3,4],[10,20,30,40]])

#行と列を回転
df = df.T
#カラム指定
df.columns = ['1列目', '2列目']

#表示
st.table(df.style.highlight_max(axis=0))
#https://docs.streamlit.io/en/stable/api.html#display-data

