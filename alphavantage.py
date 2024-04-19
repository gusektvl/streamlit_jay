import streamlit as st
import streamlit.components.v1 as components

def alphavantange_test():
    st.markdown('test')
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=B8DRZT1OHQPV2UAV'
    r = requests.get(url)
    data = r.json()

    print(data)

