import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/History_of_Mexico"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
data = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")


def get_citations_needed_count(link):

    print("How many count citations? \nCount of the Citations =",len(data))
    return len(data)    

def  get_citations_needed_report(link):
    ct =[]
    for ele in data:
        a = ele.parent.text.strip()
        if ele not in ct:
            print(f'Citation needed for: "{a}" ')
        ct.append(ele)
        print()
    return a

if __name__ == "__main__":
    get_citations_needed_count(url)
    get_citations_needed_report(url)