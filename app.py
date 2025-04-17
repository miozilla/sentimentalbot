import streamlit as st
from transformers import pipeline

pipe = pipeline('sentiment-analysis')
text = st.text_area('Hi, I am SentimentalBot, How do you experience about our Customer Service...?')

if text :
    out = pipe(text)
    st.json(out)