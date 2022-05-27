import requests
from bs4 import BeautifulSoup
def lifestyle_news():
    url = "https://indianexpress.com/section/lifestyle/"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    news = soup.find('div',attrs={'class':'nation'})
    # print(news)
    articles = news.find_all('div',attrs={'class':'articles'})
    print(len(articles))
    data = []
    for article in articles:
        try:
            news_title = article.find('h2').text.strip('\n\r')
            news_link = article.find('h2').a.get('href')
            data.append({"title":news_title,"link":f"{news_link}"})
        except Exception as e:
            pass
    return data


if __name__ =="__main__":
    data = lifestyle_news()
    print(data)