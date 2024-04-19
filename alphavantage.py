import streamlit as st
import streamlit.components.v1 as components

def alphavantage_test():
    st.markdown('test')
    url_topgainer = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
    r_topgainer = requests.get(url_topgainer)
    data_topgainer = r_topgainer.json()
    st.title('Stock Market Updates')
    st.subheader(data['metadata'])
    st.write('Last Updated:', data['last_updated'])

    # Convert lists of dictionaries to pandas DataFrame and display them
    if 'top_gainers' in data:
        st.subheader('Top Gainers')
        df_gainers = pd.DataFrame(data['top_gainers'])
        st.dataframe(df_gainers.style.hide_index())

    if 'top_losers' in data:
        st.subheader('Top Losers')
        df_losers = pd.DataFrame(data['top_losers'])
        st.dataframe(df_losers.style.hide_index())

    if 'most_actively_traded' in data:
        st.subheader('Most Actively Traded')
        df_traded = pd.DataFrame(data['most_actively_traded'])
        st.dataframe(df_traded.style.hide_index())
