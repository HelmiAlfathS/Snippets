import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Total Kasus', 'Total Kematian', 'Angka Kesembihan'])

data = soup.find_all("div", class_= "maincounter-number")
total_cases = data[0].text.strip()
total_death = data[1].text.strip()
total_rocovered = data[2].text.strip()

csv_writer.writerow([total_cases, total_death, total_rocovered])

csv_file.close()
