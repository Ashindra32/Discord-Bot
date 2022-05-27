import requests
from bs4 import BeautifulSoup
def enter_news():
    url = "https://timesofindia.indiatimes.com/etimes/etbriefs"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    ultag = soup.find('ul',{'class': 'briefitemlist'})
    for litag in ultag.find_all('li'):
        try:
            title = litag.find('h2').text
        except:
            title = ""
        try:
            link = litag.find('a').attrs.get('href')
            if link.startswith('/'):
                link = "https://timesofindia.indiatimes.com/etimes/etbriefs" + link
        except:
            link = ""
        data.append({
            'title':title,
            'link':link
        })
    return data

if __name__ =="__main__":
    data = enter_news()
    print(data)
