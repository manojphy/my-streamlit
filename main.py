import streamlit as st
import time


st.title('first streamlit app')

st.write('プレぐレスバーの表示')

'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


'done!!'

left_coloumn,right_coloumn= st.columns(2)
button=left_coloumn.button('右コラムに文字表示')
if button:
    right_coloumn.write('ここは右コラムです。')


expander=st.expander('問い合わせ')
expander.write('問い合わせ')
expander2=st.expander('営業時間')
expander2.write('営業時間')
expander2.write('ラストオーダー')
expander3=st.expander('アクセス')
expander3.write('アクセス')



#text = st.text_input('あなたの趣味')
#'あなたの趣味',text ,'です。'