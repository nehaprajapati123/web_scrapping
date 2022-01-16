
from bs4 import BeautifulSoup
import requests
import json
import pprint
url=("https://www.rottentomatoes.com/m/the_lego_movie")
movie_link=requests.get(url)
soup=BeautifulSoup(movie_link.text,'html.parser')
# requests link of a movie and convert it in text.
div=soup.find('div',class_="castSection")
def scrape_movie_cast(div):
    # scrap the section where we get the cast.
    list=[]
    for i in div:
        a=i.text
        b=a.split()
        # print(b)
        dic={}
        for j in b:
            # print(j)
            c=b[0]+" "+b[1]
            # print(c)
            dic["cast name"]=c
        list.append(dic)
    # print(list)
    for k in list:
        if k=={}:
            list.remove(k)
        # print(list)
    with open("task12.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
scrape_movie_cast(div)