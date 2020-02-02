import requests
from bs4 import BeautifulSoup

URL = 'https://www.betexplorer.com/soccer/france/ligue-1/results/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('tr')

for tr in results:
    tds = tr.find_all('td')
    for td in tds:
        print(td.text)
    print("--")
    '''
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()
    '''
    
#print(results.length)
