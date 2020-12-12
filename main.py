import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit超入門')

st.write('DateFlame')

#データフレーム読み込み
df = pd.DataFrame([[1,2,3,4],[10,20,30,40]])

#行と列を回転
df = df.T
#カラム指定
df.columns = ['1列目', '2列目']

#画像表示
from PIL import Image
image = Image.open('sample.jpeg')
st.image(image, caption='Sunrise by the mountains',
          use_column_width=True)

#新宿の緯度経度をOSM上にプロット
np.random.seed(1)
chart_data = pd.DataFrame(
    np.random.randn(100, 2)/[50, 50] + [35.69, 139.70], 
    columns=['lat', 'lon'])

#地図の表示
st.map(chart_data)

#st.bar_chart(chart_data)
#https://docs.streamlit.io/en/stable/api.html#display-charts

#表示
st.dataframe(chart_data.style.highlight_max(axis=0))
#https://docs.streamlit.io/en/stable/api.html#display-data

"""
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# #ラテフ
# st.latex(r'''
#  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#  \sum_{k=0}^{n-1} ar^k =
#  a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')

#https://docs.streamlit.io/en/stable/api.html#display-text

