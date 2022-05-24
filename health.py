import requests
from bs4 import BeautifulSoup
def health_news():
    url = "https://timesofindia.indiatimes.com/life-style/health-fitness"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    target= soup.find('div',attrs={'class':'fix_wrapper clearfix'})
    for news in target.find_all('div',attrs={'class': 'ent_middle clearfix'}):
        try:
            title = news.find('div',attrs= {'class': 'wht_box clearfix'}).text
        except:
            title = ""
        data.append(title)
    return data

if __name__ =="__main__":
    data = health_news()
    print(data)
