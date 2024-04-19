import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def fetch_dart_disclosures(url):
    response = requests.get(url)
    if response.status_code != 200:
        return pd.DataFrame()  # 데이터를 가져오는데 실패한 경우 빈 데이터프레임 반환

    soup = BeautifulSoup(response.text, 'html.parser')
    disclosures = []
    table = soup.find('table', {'summary': '시간,공시대상회사,보고서명,제출인,접수일자,비고 순으로 되어있습니다.'})
    if table:
        rows = table.find_all('tr')[1:]  # 첫 번째 헤더 행을 제외
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 4:
                time = cells[0].get_text(strip=True)
                company_name = cells[1].get_text(strip=True)[1:]
                report_name = cells[2].get_text(strip=True)
                submission_date = cells[4].get_text(strip=True)
                disclosures.append({
                    'Time': time,
                    'Company Name': company_name,
                    'Report Name': report_name,
                    'Submission Date': submission_date
                })
    return pd.DataFrame(disclosures)

def dart_test():
    st.title('DART Recent Disclosures')
    date = dt.datetime.today().strftime("%Y.%m.%d")
    url = "https://dart.fss.or.kr/dsac001/mainAll.do?selectDate="+date+"&sort=&series=&mdayCnt=0"
    data = fetch_dart_disclosures(url)

    if not data.empty:
        # 첫 번째 열을 숨기기 위해 첫 번째 열을 제외하고 데이터 프레임 생성
        data_display = data[['Company Name', 'Report Name', 'Submission Date']]

        # CSS를 사용하여 테이블 스타일을 조정
        st.markdown("""
            <style>
            .dataframe th, .dataframe td {
                text-align: left;
                min-width: 150px;  /* 셀 최소 너비 조정 */
                max-width: 300px;  /* 셀 최대 너비 조정 */
            }
            </style>
            """, unsafe_allow_html=True)

        st.dataframe(data_display)  # 데이터 프레임을 통해 상호작용 가능한 테이블 표시
    else:
        st.write("No data available")