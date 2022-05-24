import requests
from bs4 import BeautifulSoup

def science_news():
    url = "https://www.sciencenews.org/topics"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    sectionList = soup.find_all('section',attrs={'class':'term-feature__wrapper___1AHJX'})
    for section in sectionList:
        headingList = section.find_all('h3')
        for heading in headingList:
            try:
                news_title = heading.text.strip('\n\t\r')
                news_link = heading.a.get('href')
                data.append({"title":news_title,"link":f"{news_link}"})
            except Exception as e:
                pass
    return data

if __name__ =="__main__":
    data = science_news()
    print(data)