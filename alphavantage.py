import streamlit as st
import streamlit.components.v1 as components
import requests
import streamlit as st

def alphavantage_test():
    url_top = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey= B8DRZT1OHQPV2UAV'
    r_top = requests.get(url_top)
    data = r_top.json()
    st.title('Top Gainers, Losers, and Most Actively Traded US Tickers')
    st.write(f"Last Updated: {data['last_updated']}")

    # Top Gainers 데이터프레임 생성 및 표시
    st.header('Top Gainers')
    df_gainers = pd.DataFrame(data['top_gainers'])
    st.dataframe(df_gainers)

    # Top Losers 데이터프레임 생성 및 표시
    st.header('Top Losers')
    df_losers = pd.DataFrame(data['top_losers'])
    st.dataframe(df_losers)

    # Most Actively Traded 데이터프레임 생성 및 표시
    st.header('Most Actively Traded')
    df_active = pd.DataFrame(data['most_actively_traded'])
    st.dataframe(df_active)