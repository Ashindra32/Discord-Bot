import requests
from bs4 import BeautifulSoup
def sports_news():
    url = "https://timesofindia.indiatimes.com/sports"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    target= soup.find('div',attrs={'id':'c_sport_wdt_1'})
    newslist = target.find_all('ul',attrs={'class':'cvs_wdt'})
    data = []
    for news_ul in newslist:
        for news_li in news_ul.find_all('li'):
            try:
                news_title = news_li.find('a').text
                news_link = news_li.find('a').get('href')
                if news_link.startswith('/'):
                    news_link = "https://timesofindia.indiatimes.com" + news_link
                if len(news_title) > 20:
                    data.append({"title":news_title,"link":news_link})
            except:
                pass
    return data

if __name__ =="__main__":
    data = sports_news()
    print(data)

