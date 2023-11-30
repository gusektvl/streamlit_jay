import streamlit as st
import streamlit.components.v1 as components

dict_macro = {
    '주간실업수당청구':'FRED:ICSA',
    '소비자심리지수':'FRED:UMCSENT',
    '주택판매지수':'FRED:HSN1F',
    '실업률':'FRED:UNRATE',
    'M2':'FRED:M2SL',
    '하이일드 채권 스프레드':'FRED:BAMLH0A0HYM2',
}

def macro_FRED():
    st.selectbox(
        label = '지표 선택',
        options = list(dict_macro.keys())
    )

def macro_calendar():
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <div class="tradingview-widget-copyright"><a href="https://kr.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">트레이딩뷰에서 모든 시장 추적</span></a></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {
          "colorTheme": "light",
          "isTransparent": false,
          "width": "1200",
          "height": "2000",
          "locale": "en",
          "importanceFilter": "-1,0,1",
          "countryFilter": "us,eu,it,nz,ch,au,fr,jp,za,tr,ca,de,mx,es,gb"
        }
          </script>
        </div>
        <!-- TradingView Widget END -->
        <!-- TradingView Widget END -->
        """,
        width=1200, height=2000
    )


def macro_analysis():
    st.text('analysis')

