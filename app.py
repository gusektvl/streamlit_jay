from pathlib import Path
import pandas as pd
import pandas_ta as ta
import numpy as np
import yfinance as yf
import plotly
import json
import requests
import base64
from datetime import datetime
import FinanceDataReader as fdr
import altair as alt
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import streamlit_lightweight_charts.dataSamples as data
from streamlit_option_menu import option_menu
from datetime import date
from datetime import timedelta
from fredapi import Fred
import pygwalker as pyg
from backtesting import backtesting_test
import streamlit.components.v1 as components
from reits import *
from econ import *
from settings import *

fred = Fred(api_key='adf294d9c5f0940de2dc75f248e017ae')

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Initial page config
st.set_page_config(
    page_title="Jay's Park",
    layout="wide",
    initial_sidebar_state="expanded")


styles = {
    "container": {"margin": "0px !important", "padding": "0!important", "align-items": "stretch", "background-color": "transparent"},
    "icon": {"color": "black", "font-size": "20px"},
    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "lightblue", "font-size": "20px", "font-weight": "normal", "color": "black", },
}

menu = {
    'title': 'Test',
    'items': {
        'Backtesting': {
            'action': None,
            'item_icon': 'rewind',
            'submenu': {
                'title': None,
                'items': {
                    'Test': {'action': backtesting_test, 'item_icon': 'list-task', 'submenu': None},
                },
                'menu_icon': None,
                'default_index': 0,
                'with_view_panel': 'main',
                'orientation': 'horizontal',
                'styles': styles
            }
        },
        "Markets" : {
            'action': None,
            'item_icon': 'building',
            'submenu': {
                'title': None,
                'items': {
                    'News' : {'action': news, 'item_icon': 'list-task', 'submenu': None},
                    'Sector' : {'action': reits_sector, 'item_icon': 'list-task', 'submenu': None},
                    'Stock' : {'action': reits_company, 'item_icon': 'graph-up', 'submenu': None},
                    'Screener' : {'action': reits_screener, 'item_icon': 'cart4', 'submenu': None},
                    'Backtesting' : {'action': reits_backtesting, 'item_icon': 'rewind', 'submenu': None},
                    },
                'menu_icon': None,
                'default_index': 0,
                'with_view_panel': 'main',
                'orientation': 'horizontal',
                'styles': styles
            }
        },
        'Economic Variables' : {
            'action': None,
            'item_icon': 'bank',
            'submenu': {
                'title': None,
                'items': {
                    'Calendar': {'action': macro_calendar, 'item_icon': 'calendar-event', 'submenu': None},
                    'Yield' : {'action': macro_FRED, 'item_icon': 'graph-up', 'submenu': None},
                    'Analysis': {'action': macro_analysis, 'item_icon': 'lightning', 'submenu': None}
                },
                'menu_icon': None,
                'default_index': 0,
                'with_view_panel': 'main',
                'orientation': 'horizontal',
                'styles': styles
            }
        },
        'Settings' : {
            'action': None, 'item_icon': 'gear', 'submenu': {
                'title': None,
                'items': {
                    'Manage Credentials' : {'action': settings_panel_1, 'item_icon': 'key', 'submenu': None},
                    'View Logs' : {'action': setting_panel_2, 'item_icon': 'journals', 'submenu': None},
                },
                'menu_icon': None,
                'default_index': 0,
                'with_view_panel': 'main',
                'orientation': 'horizontal',
                'styles': styles
            }
        }
    },
    'menu_icon': 'globe',
    'default_index': 0,
    'with_view_panel': 'sidebar',
    'orientation': 'vertical',
    'styles': styles
}

def show_menu(menu):
    def _get_options(menu):
        options = list(menu['items'].keys())
        return options

    def _get_icons(menu):
        icons = [v['item_icon'] for _k, v in menu['items'].items()]
        return icons

    kwargs = {
        'menu_title': menu['title'] ,
        'options': _get_options(menu),
        'icons': _get_icons(menu),
        'menu_icon': menu['menu_icon'],
        'default_index': menu['default_index'],
        'orientation': menu['orientation'],
        'styles': menu['styles']
    }

    with_view_panel = menu['with_view_panel']
    if with_view_panel == 'sidebar':
        with st.sidebar:
            menu_selection = option_menu(**kwargs)


    elif with_view_panel == 'main':
        menu_selection = option_menu(**kwargs)
    else:
        raise ValueError(f"Unknown view panel value: {with_view_panel}. Must be 'sidebar' or 'main'.")

    if menu['items'][menu_selection]['submenu']:
        show_menu(menu['items'][menu_selection]['submenu'])

    if menu['items'][menu_selection]['action']:
        menu['items'][menu_selection]['action']()



def main():
    show_menu(menu)

    components.html(
        """
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
          {
          "symbols": [
            {
              "description": "",
              "proName": "KRX:KOSPI"
            },
            {
              "description": "",
              "proName": "KRX:KOSPI200"
            },
            {
              "description": "",
              "proName": "KRX:KOSDAQ"
            },
            {
              "description": "",
              "proName": "KRX:KOSDAQ150"
            },
            {
              "proName": "FOREXCOM:SPXUSD",
              "title": "S&P 500"
            },
            {
              "proName": "FOREXCOM:NSXUSD",
              "title": "US 100"
            },
            {
              "description": "",
              "proName": "FX_IDC:USDKRW"
              }            
          ],
          "showSymbolLogo": true,
          "colorTheme": "light",
          "isTransparent": false,
          "displayMode": "adaptive",
          "locale": "en"
        }
          </script>
        </div>
        <!-- TradingView Widget END -->
    """
    )

    return None


##########################
# Main body of cheat sheet
##########################

if __name__ == '__main__':
    main()
