import requests
from bs4 import BeautifulSoup
def timesofindia():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")
    data = []
    counter = 0
    for divtag in soup.find_all('div', {'class': 'headlines-list'}):
        for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
            if (counter <= 10):
                for litag in ultag.find_all('li'):
                    counter = counter + 1
                    link = "https://timesofindia.indiatimes.com" + litag.find('a')['href']
                    title = litag.find('a').text
                    # time = litag.find('span',attrs={'class':'w_bylinec'}).text
                    data.append({
                        'title':title,
                        'link': link,
                        #'time':time
                    })
    return data
                    

if __name__ == "__main__":
    out = timesofindia()
    for row in out:
        print(row)
        print()
