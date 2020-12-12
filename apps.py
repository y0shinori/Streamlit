import streamlit as st

st.title('Streamlit動的')

#st.write('Interactive widgets')

#2カラム
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

#画像表示
from PIL import Image
#画像表示の可否
if st.sidebar.checkbox('画像を表示'):
    image = Image.open('sample.jpeg')
    st.image(image, caption='Sunrise by the mountains',use_column_width=True)

#テキストボックス
'あなたの趣味は', st.sidebar.text_input('あなたの趣味は何ですか'), 'です'

#セレクトボックス
option = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です'
#https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')