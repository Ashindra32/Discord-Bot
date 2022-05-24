import requests
from bs4 import BeautifulSoup
def tech_news():
    url = "https://www.gadgetsnow.com/tech-news"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    target = soup.find('div',attrs={'class':'tech_list ctn_stories'})
    for news in target.find('ul').find_all('li'):
        title = news.find('span',{'class': 'w_tle'}).text 
        info = news.find('span',{'class': 'w_desc'}).text
        data.append({
            'title':title,
            'description': info,
        })
    return data
  
if __name__ == "__main__":
    data = tech_news()
    print(data)
