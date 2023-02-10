import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

with open('datas.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)


URL = ""  # url of website
HEADERS = {}  # user-agent

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('div', class_='item product_listbox oh')
bags = []

for item in items:
    bags.append({
        'Title': item.find('div', class_='listbox_title oh').get_text(strip=True),
        'Description': item.find('div', class_='product_text pull-left').get_text(strip=True),
        'Price': item.find('div', class_='listbox_price text-center').get_text(strip=True)
    })

for bag in bags:
    print(f"{bag['Title']}; {bag['Description']}; {bag['Price']}")
    with open('datas.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([f"{bag['Title']}; {bag['Description']}; {bag['Price']}"])