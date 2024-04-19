import streamlit as st
import streamlit.components.v1 as components

def alphavantage_test():
    url_top = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
    r_top = requests.get(url_top)
    data_top = r_top.json()
    st.title('Stock Market Updates')
    st.subheader(data_top['metadata'])
    st.write('Last Updated:', data_top['last_updated'])

    st.dataframe(data_top['top_gainers'])
    # Convert lists of dictionaries to pandas DataFrame and display them
    if 'top_gainers' in data_top:
        st.subheader('Top Gainers')
        df_gainers = pd.DataFrame(data_top['top_gainers'])
        st.dataframe(df_gainers, hide_index=True)

    if 'top_losers' in data_top:
        st.subheader('Top Losers')
        df_losers = pd.DataFrame(data_top['top_losers'])
        st.dataframe(df_losers, hide_index=True)

    if 'most_actively_traded' in data_top:
        st.subheader('Most Actively Traded')
        df_traded = pd.DataFrame(data_top['most_actively_traded'])
        st.dataframe(df_traded, hide_index=True)
