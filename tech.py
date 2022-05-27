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
        link = news.find('span',{'class': 'w_tle'}).find('a').get('href') 
        if 'https://www.gadgetsnow.com/tech-news' not in link:
            link = 'https://www.gadgetsnow.com/tech-news'+link
        data.append({
            'title':title,
            'link':link
        })
    return data
  
if __name__ == "__main__":
    data = tech_news()
    print(data)
