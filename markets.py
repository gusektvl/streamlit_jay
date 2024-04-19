import requests
import streamlit as st
import streamlit.components.v1 as components

def news():
    url = "https://newsapi.org/v2/top-headlines?country=kr&apiKey=79fc0e8d84134b8e896750585f7192e4"
    r = requests.get(url)
    data = r.json()
    articles = data['articles']
    components.html(
        st.dataframe(articles), width=1200, height=2000
    )


def sector():
    components.html(
        width=1200, height=1200
    )


def company():
    html_code ="""
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
                <!--header-->
                    <!--a id="site-logo" href="#">Test...</a-->
                    <!--input type="search" placeholder="Search..." /-->
                <!--/header-->
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
        """
    components.html(html_code, height=3000, width=1350)


def screener():
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

def backtesting():
    st.text('backtester...')

