import streamlit as st
import streamlit.components.v1 as components

dict_reits = {
    '마스턴프리미어리츠':'357430','맥쿼리인프라':'088980','제이알글로벌리츠':'348950','TIGER 리츠부동산인프라':'329200','ESR켄달스퀘어리츠':'365550','롯데리츠':'330590','SK리츠':'395400','코람코라이프인프라리츠':'357120','신한알파리츠':'293940','이리츠코크렙':'088260','신한서부티엔디리츠':'404990','디앤디플랫폼리츠':'377190','NH올원리츠':'400760','미래에셋글로벌리츠':'396690','NH프라임리츠':'338100','미래에셋맵스리츠':'357250','이지스밸류리츠':'334890','이지스레지던스리츠':'350520','TIGER 미국MSCI리츠(합성 H)':'182480','코람코더원리츠':'417310','KB스타리츠':'432320','한화리츠':'451800','삼성FN리츠':'448730'
}
def news():
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
  {
  "feedMode": "market",
  "market": "index",
  "isTransparent": false,
  "displayMode": "adaptive",
  "width": "100%",
  "height": "100%",
  "colorTheme": "light",
  "locale": "en"
}
  </script>
</div>
<!-- TradingView Widget END -->
        """,
        width=1200, height=2000
    )

def reits_sector():
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js" async>
  {
  "title":"REITs",
  "width": 1200,
  "height": 1200,
  "symbolsGroups": [
    {
      "name": "K REITs",
      "symbols": [
          {"name": "357430", "displayName": "마스턴프리미어리츠"},
          {"name": "088980", "displayName": "맥쿼리인프라"},
          {"name": "348950", "displayName": "제이알글로벌리츠"},
          {"name": "365550", "displayName": "ESR켄달스퀘어리츠"},
          {"name": "330590", "displayName": "롯데리츠"},
          {"name": "395400", "displayName": "SK리츠"},
          {"name": "357120", "displayName": "코람코라이프인프라리츠"},
          {"name": "293940", "displayName": "신한알파리츠"},
          {"name": "088260", "displayName": "이리츠코크렙"},
          {"name": "404990", "displayName": "신한서부티엔디리츠"},
          {"name": "377190", "displayName": "디앤디플랫폼리츠"}, 
          {"name": "400760", "displayName": "NH올원리츠"},
          {"name": "396690", "displayName": "미래에셋글로벌리츠"},
          {"name": "338100", "displayName": "NH프라임리츠"},
          {"name": "357250", "displayName": "미래에셋맵스리츠"},
          {"name": "334890", "displayName": "이지스밸류리츠"},
          {"name": "350520", "displayName": "이지스레지던스리츠"},
          {"name": "417310", "displayName": "코람코더원리츠"},
          {"name": "432320", "displayName": "KB스타리츠"},
          {"name": "451800", "displayName": "한화리츠"},
          {"name": "448730", "displayName": "삼성FN리츠"},
          {"name": "182480", "displayName": "TIGER 미국MSCI리츠(합성 H)"}, 
          {"name": "329200", "displayName": "TIGER 리츠부동산인프라"}
      ]
    },
    {
    "name": "US REITs",
    "symbols": [
        {"name": "NYSE:PLD", "displayName": "Prologis"},
        {"name": "NYSE:AMT", "displayName": "American Tower Crop"},
        {"name": "NASDAQ:EQIX", "displayName": "Equinix Inc"},
        {"name": "NYSE:CCI", "displayName": "Crown Castle Inc"}
        ]
    }
    ],
  "showSymbolLogo": true,
  "colorTheme": "light",
  "isTransparent": false,
  "locale": "en"
}
  </script>
</div>
<!-- TradingView Widget END -->
    """,
        width=1200, height=1200
    )

def reits_company():
    list_reits = ['삼성FN리츠', '한화리츠', 'KB스타리츠', '마스턴프리미어리츠', '코람코더원리츠', '신한서부티엔디리츠', '미래에셋글로벌리츠', 'NH올원리츠', 'SK리츠','디앤디플랫폼리츠', 'ESR켄달스퀘어리츠', '코람코라이프인프라리츠', '제이알글로벌리츠', '미래에셋맵스리츠', '이지스레지던스리츠', '이지스밸류리츠', 'NH프라임리츠', '롯데리츠', '신한알파리츠', '이리츠코크렙', '모두투어리츠', '케이탑리츠', '에이리츠']
    st.write("총 " + str(len(list_reits)) + " 종목")
    select_reit = st.selectbox(label='종목', options=sorted(list_reits))
    code_reit = dict_reits[select_reit]

    ticker = "KRX:"+code_reit
    components.html(
        f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div id="tradingview_dc0b5"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
          "width": "1350",
          "height": "700",
          "symbol": "{ticker}",
          "interval": "D",
          "timezone": "Asia/Seoul",
          "theme": "light",
          "style": "1",
          "locale": "en",
          "enable_publishing": false,
          "allow_symbol_change": true,
          "details": true,
          "studies": ["STD;RSI"],
          "container_id": "tradingview_dc0b5"
        }}
          );
          </script>
        </div>
        <!-- TradingView Widget END -->""",
        height=700,
        width=1350
    )

def reits_screener():
    components.html(
        """
        <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-screener.js" async>
      {
      "width": 1200,
      "height": 1500,
      "defaultColumn": "overview",
      "defaultScreen": "most_capitalized",
      "market": "korea",
      "showToolbar": true,
      "colorTheme": "light",
      "locale": "en"
    }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """,
        width=1200, height=1500
    )

def reits_backtesting():
    st.text('backtester...')

