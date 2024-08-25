import requests
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
import streamlit as st
import numpy as np


book_list = []

for page in range(1, 6):
    url = 'https://search.kyobobook.co.kr/search?keyword=python&target=total&gbCode=TOT&page='+str(page)
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')
    if res.status_code == 200:
        # 여기에서 추가 작업을 수행
        #book_list = [0]*20
        books = soup.select('div.prod_info_box')
        #prices = soup.select('div.prod_info_box')
    
        for book in books[:20]:
            titles = book.select_one('a.prod_info').select('span')[-1].string
            prices = book.select_one('span.val').text
            autors = book.select_one('a.author.rep').string
            publisher = book.select_one('a.text').string
            publish_year = book.select_one('span.date').string
        
            book_list.append({
                'Title': titles,
                'Price': prices,
                'Author': autors,
                'Publish': publisher,
                'Publish Date': publish_year
            })
    
        for book in book_list:
            print(book['Title'], book['Price'], book['Author'], book['Publish'], book['Publish Date'])
    
        
        #st.header('st.dataframe')
        #st.dataframe(data=df, width=1000, height=1000)
        df = pd.DataFrame(book_list)
        df.to_csv('data.csv')
        
        st.header('교보문고 책 정보 (20개씩 증가 보이도록 하였습니다!)')
        st.dataframe(data=df, width=1000, height=1000)
        #df = pd.DataFrame(book_list)
        #st.dataframe(book_list)