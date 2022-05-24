import requests
from bs4 import BeautifulSoup
def sports_news():
    url = "https://timesofindia.indiatimes.com/sports"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    target= soup.find('div',attrs={'id':'c_sport_wdt_1'})
    for divtag in target.find('div',attrs={'class':'news-section clearfix'}):
        try:
            title = divtag.find('div').text
        except:
            title = ""
        data.append(title)
    return data

if __name__ =="__main__":
    data = sports_news()
    print(data)

