import requests
from bs4 import BeautifulSoup
def get_headlines(url = "https://www.hindustantimes.com/latest-news"):
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    target = soup.find('section',attrs={'id':'dataHolder'})
    for divtag in target.find_all('div', {'class': 'cartHolder listView track'}):
        category = divtag.find('div',attrs={'class':'catName'}).text
        title = divtag.find('h3',attrs={'class':'hdg3'}).text
        data.append({
            'title':title,
            'category':category,
        })
    return data
                    
print(get_headlines())