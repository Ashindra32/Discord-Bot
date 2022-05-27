from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
def business_news():
    url = "https://timesofindia.indiatimes.com/business/india-business"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    ultag = soup.find('ul',attrs={'class':'list5'})
    items = ultag.find_all('li')
    # print(len(items))
    for news in items:
        try:
            title=news.find("span").a.text
            link=news.find("span").a.attrs.get('href')
            if link.startswith('/'):
                link = "https://timesofindia.indiatimes.com"+link
            data.append({
                'title':title,
                'link':link,
            })
        except:
            pass    

    return data

if __name__ == "__main__":
    data = business_news()
    print(data)