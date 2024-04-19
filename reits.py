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
          "width": "1200",
          "height": "1000",
          "colorTheme": "light",
          "locale": "en"
        }
          </script>
        </div>
        <!-- TradingView Widget END -->
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {
          "feedMode": "market",
          "market": "stock",
          "isTransparent": false,
          "displayMode": "adaptive",
          "width": "1200",
          "height": "1000",
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

def company():
    list_reits = ['삼성FN리츠', '한화리츠', 'KB스타리츠', '마스턴프리미어리츠', '코람코더원리츠', '신한서부티엔디리츠', '미래에셋글로벌리츠', 'NH올원리츠', 'SK리츠','디앤디플랫폼리츠', 'ESR켄달스퀘어리츠', '코람코라이프인프라리츠', '제이알글로벌리츠', '미래에셋맵스리츠', '이지스레지던스리츠', '이지스밸류리츠', 'NH프라임리츠', '롯데리츠', '신한알파리츠', '이리츠코크렙', '모두투어리츠', '케이탑리츠', '에이리츠']
    st.write("총 " + str(len(list_reits)) + " 종목")
    select_reit = st.selectbox(label='종목', options=sorted(list_reits))
    code_reit = dict_reits[select_reit]
    ticker = "KRX:"+code_reit
    components.html(
        """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Stock Details</title>
                <style>
                    :root {
                        --gap-size: 32px;
                        box-sizing: border-box;
                        font-family: -apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto,
                            Ubuntu, sans-serif;
                        color: #000;
                    }
        
                    * {
                        box-sizing: border-box;
                    }
        
                    body {
                        margin: 0;
                        padding: 0;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        background: #fff;
                    }
        
                    header,
                    footer {
                        display: flex;
                        width: 100%;
                        align-items: center;
                        background: rgba(0, 0, 0, 0.05);
                        gap: 12px;
                    }
        
                    header {
                        justify-content: space-between;
                        padding: 0 var(--gap-size);
                        gap: calc(var(--gap-size) * 2);
                        box-shadow: rgba(0, 0, 0, 0.05) 0 2px 6px 0;
                        flex-direction: row;
                        z-index: 1;
                    }
        
                    header #site-logo {
                        font-weight: 590;
                        font-size: 32px;
                        padding: 16px;
                        background: var(
                            --18-promo-gradient-02,
                            linear-gradient(90deg, #00bce5 0%, #2962ff 100%)
                        );
                        -webkit-text-fill-color: transparent;
                        -webkit-background-clip: text;
                        background-clip: text;
                    }
        
                    header input[type='search'] {
                        padding: 10px;
                        width: 100%;
                        height: 32px;
                        max-width: 400px;
                        border: 1px solid #ccc;
                        border-radius: 20px;
                    }
        
                    footer {
                        flex-direction: column;
                        padding: calc(var(--gap-size) * 0.5) var(--gap-size);
                        margin-top: var(--gap-size);
                        border-top: solid 2px rgba(0, 0, 0, 0.1);
                        justify-content: center;
                    }
        
                    footer p,
                    #powered-by-tv p {
                        margin: 0;
                        font-size: 12px;
                        color: rgba(0, 0, 0, 0.6);
                    }
        
                    main {
                        display: grid;
                        width: 100%;
                        padding: 0 calc(var(--gap-size) * 0.5);
                        max-width: 960px;
                        grid-template-columns: 1fr 1fr;
                        grid-gap: var(--gap-size);
                    }
        
                    .span-full-grid,
                    #symbol-info,
                    #advanced-chart,
                    #company-profile,
                    #fundamental-data {
                        grid-column: span 2;
                    }
        
                    .span-one-column,
                    #technical-analysis,
                    #top-stories,
                    #powered-by-tv {
                        grid-column: span 1;
                    }
        
                    #ticker-tape {
                        width: 100%;
                        margin-bottom: var(--gap-size);
                    }
        
                    #advanced-chart {
                        height: 500px;
                    }
        
                    #company-profile {
                        height:390px;
                    }
        
                    #fundamental-data {
                        height: 490px;
                    }
        
                    #technical-analysis,
                    #top-stories {
                        height: 425px;
                    }
        
                    #powered-by-tv {
                        display: flex;
                        background: #f8f9fd;
                        border: solid 1px #e0e3eb;
                        text-align: justify;
                        flex-direction: column;
                        gap: 8px;
                        font-size: 14px;
                        padding: 16px;
                        border-radius: 6px;
                    }
        
                    #powered-by-tv a, #powered-by-tv a:visited {
                        color: #2962ff;
                    }
        
                    @media (max-width: 800px) {
                        main > section,
                        .span-full-grid,
                        #technical-analysis,
                        #top-stories,
                        #powered-by-tv {
                            grid-column: span 2;
                        }
                    }
                </style>
            </head>
            <body>
                <header>
                    <a id="site-logo" href="#">TradingVista</a>
                    <input type="search" placeholder="Search..." />
                </header>
                <nav id="ticker-tape"></nav>
                <main>
                    <section id="symbol-info">
                    </section>
                    <section id="advanced-chart">
                    </section>
                    <section id="company-profile">
                    </section>
                    <section id="fundamental-data">
                    </section>
                    <section id="technical-analysis">
                    </section>
                    <section id="top-stories">
                    </section>
                    <section id="powered-by-tv">
                        <svg xmlns="http://www.w3.org/2000/svg" width="157" height="21">
                            <use href="/widget-docs/tradingview-logo.svg#tradingview-logo"></use>
                        </svg>
                        <p>
                            Charts and financial information provided by TradingView, a popular
                            charting & trading platform. Check out even more
                            <a href="https://www.tradingview.com/features/">advanced features</a>
                            or <a href="https://www.tradingview.com/widget/">grab charts</a> for
                            your website.
                        </p>
                    </section>
                </main>
                <footer>
                    <p>
                        This example page is part of a tutorial for integrating TradingView
                        widgets into your website.
                    </p>
                    <p><a href="/widget-docs/tutorials/build-page/">View the tutorial</a></p>
                </footer>
            </body>
            <template id="ticker-tape-widget-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js"
                        async
                    >
                        {
                        "symbols": [
                          {
                            "description": "",
                            "proName": "NASDAQ:TSLA"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:AAPL"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:NVDA"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:MSFT"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:AMZN"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:GOOGL"
                          },
                          {
                            "description": "",
                            "proName": "NASDAQ:META"
                          },
                          {
                            "description": "",
                            "proName": "NYSE:BRK.B"
                          },
                          {
                            "description": "",
                            "proName": "NYSE:LLY"
                          },
                          {
                            "description": "",
                            "proName": "NYSE:UNH"
                          },
                          {
                            "description": "",
                            "proName": "NYSE:V"
                          },
                          {
                            "description": "",
                            "proName": "NYSE:WMT"
                          }
                        ],
                        "showSymbolLogo": true,
                        "colorTheme": "light",
                        "isTransparent": false,
                        "displayMode": "adaptive",
                        "locale": "en",
                        "largeChartUrl": "#"
                         }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <template id="symbol-info-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js"
                        async
                    >
                        {
                        "symbol": "NASDAQ:AAPL",
                        "width": "100%",
                        "locale": "en",
                        "colorTheme": "light",
                        "isTransparent": true
                         }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/tv.js"
                    ></script>
            <template id="advanced-chart-template">
                <!-- TradingView Widget BEGIN -->
                <div
                    class="tradingview-widget-container"
                    style="height: 100%; width: 100%"
                >
                    <div
                        id="tradingview_ae7da"
                        style="height: calc(100% - 32px); width: 100%"
                    ></div>
        
                    <script type="text/javascript">
                        new TradingView.widget({
                            autosize: true,
                            symbol: 'NASDAQ:AAPL',
                            interval: 'D',
                            timezone: 'Etc/UTC',
                            theme: 'light',
                            style: '1',
                            locale: 'en',
                            enable_publishing: false,
                            hide_side_toolbar: false,
                            allow_symbol_change: true,
                            studies: ['STD;MACD'],
                            container_id: 'tradingview_ae7da',
                        });
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <template id="company-profile-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js"
                        async
                    >
                          {
                          "width": "100%",
                          "height": "100%",
                          "colorTheme": "light",
                          "isTransparent": true,
                          "symbol": "NASDAQ:AAPL",
                          "locale": "en"
                        }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <template id="fundamental-data-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js"
                        async
                    >
                          {
                          "colorTheme": "light",
                          "isTransparent": true,
                          "largeChartUrl": "",
                          "displayMode": "adaptive",
                          "width": "100%",
                          "height": "100%",
                          "symbol": "NASDAQ:AAPL",
                          "locale": "en"
                        }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <template id="technical-analysis-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js"
                        async
                    >
                        {
                        "interval": "15m",
                        "width": "100%",
                        "isTransparent": true,
                        "height": "100%",
                        "symbol": "NASDAQ:AAPL",
                        "showIntervalTabs": true,
                        "displayMode": "single",
                        "locale": "en",
                        "colorTheme": "light"
                         }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <template id="top-stories-template">
                <!-- TradingView Widget BEGIN -->
                <div class="tradingview-widget-container">
                    <div class="tradingview-widget-container__widget"></div>
                    <script
                        type="text/javascript"
                        src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js"
                        async
                    >
                          {
                          "feedMode": "symbol",
                          "symbol": "NASDAQ:AAPL",
                          "colorTheme": "light",
                          "isTransparent": true,
                          "displayMode": "regular",
                          "width": "100%",
                          "height": "100%",
                          "locale": "en"
                        }
                    </script>
                </div>
                <!-- TradingView Widget END -->
            </template>
            <script>
                function getQueryParam(param) {
                    let urlSearchParams = new URLSearchParams(window.location.search);
                    return urlSearchParams.get(param);
                }
                function readSymbolFromQueryString() {
                    return getQueryParam('tvwidgetsymbol');
                }
        
                function cloneTemplateInto(templateId, targetId, rewrites) {
                    const tmpl = document.querySelector(`#${templateId}`);
                    if (!tmpl) return;
                    const target = document.querySelector(`#${targetId}`);
                    if (!target) return;
                    target.innerText = '';
                    const clone = tmpl.content.cloneNode(true);
                    if (rewrites) {
                        const script = clone.querySelector('script');
                        script.textContent = rewrites(script.textContent);
                    }
                    target.appendChild(clone);
                }
                function currentPage() {
                    const l = document.location;
                    if (!l) return;
                    if (l.origin && l.pathname) return l.origin + l.pathname;
                    return l.href;
                }
                cloneTemplateInto('ticker-tape-widget-template', 'ticker-tape', function(scriptContent) {
                    const currentPageUrl = currentPage();
                    if (!currentPageUrl) return scriptContent;
                    return scriptContent.replace('"largeChartUrl": "#"', `"largeChartUrl": "${currentPageUrl}"`)
                });
                const symbol = readSymbolFromQueryString() || 'NASDAQ:AAPL';
                function setSymbol(scriptContent) {
                    return scriptContent.replace(/"symbol": "([^"]*)"/g, () => {
                        return `"symbol": "${symbol}"`;
                    });
                }
                cloneTemplateInto('symbol-info-template', 'symbol-info', setSymbol);
                cloneTemplateInto('advanced-chart-template', 'advanced-chart');
                cloneTemplateInto('company-profile-template', 'company-profile', setSymbol);
                cloneTemplateInto('fundamental-data-template', 'fundamental-data', setSymbol);
                cloneTemplateInto('technical-analysis-template', 'technical-analysis', setSymbol);
                cloneTemplateInto('top-stories-template', 'top-stories', setSymbol);
                if (symbol) {
                    document.title = `Stock Details - ${symbol}`;
                }
            </script>
        </html>
        """,
        height="100%",
        width="100%"
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

