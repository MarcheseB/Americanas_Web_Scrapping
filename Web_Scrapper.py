import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/bravo/PycharmProjects/Web Scrapping Project/chromedriver.exe')
driver.get('https://www.americanas.com.br/')
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
driver.quit()
produtos = soup.find_all('div', class_='product__Wrapper-sc-vep9u6-1 kxgwlS')
for prod in produtos:
    path1 = prod.find('div', class_='product__WrapperProduct-sc-vep9u6-11 cIYrxw')
    name = path1.find('span').text
    price = path1.find('div', class_='product__Price-sc-vep9u6-6 hwhYar').text
    print(f'Produto: {name}\nPreço: {price}')
