import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import pandas as pd

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
                company_name = cells[1].get_text(strip=True)
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
    # Streamlit 앱
    st.title('DART Recent Disclosures')
    url = "https://dart.fss.or.kr/dsac001/mainAll.do"
    data = fetch_dart_disclosures(url)
    if not data.empty:
        st.dataframe(data)  # 데이터 프레임을 통해 상호작용 가능한 테이블 표시
    else:
        st.write("No data available")