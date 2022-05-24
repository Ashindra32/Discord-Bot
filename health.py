import requests
from bs4 import BeautifulSoup
def health_news():
    url = "https://timesofindia.indiatimes.com/life-style/health-fitness/health-news"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    news = soup.find_all('div',attrs={'class':'md_news_box'})
    for news_div in news:
        try:
            news_title = news_div.find('p').text
            news_link = news_div.find('p').a.get('href')
            data.append({"title":news_title,"link":f"{url}{news_link}"})
        except Exception as e:
            pass
    return data

if __name__ =="__main__":
    data = health_news()
    print(data)
