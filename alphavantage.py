import streamlit as st
import streamlit.components.v1 as components
import requests
impot streamlit as st

def alphavantage_test():
    url_top = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey= B8DRZT1OHQPV2UAV'
    r_top = requests.get(url_top)
    data_top = r_top.json()
    st.title('Stock Market Updates')
    st.subheader(data_top['metadata'])
    st.write('Last Updated:', data_top['last_updated'])
    st.dataframe(data_top['top_gainers'])