from bs4 import BeautifulSoup
import requests
import json
import pprint
url=("https://www.rottentomatoes.com/m/the_lego_movie")
# whatever movie link will given that's cast we are scrapping.
movie_link=requests.get(url)
# requesting link data
soup=BeautifulSoup(movie_link.text,'html.parser')
#convert it in text.
div=soup.find('div',class_="castSection")
# scrapping cast section.
def scrape_movie_cast(div):
    list=[]
    for i in div:
        a=i.text
        b=a.split()
        # print(b) names in list
        # print(b) loop in the data(div) convert it in text form(.text), split(.split) it for removal of white spaces.
        dic={}
        for j in b:
            # pprint.pprint(j)
            c=b[0]+" "+b[1]
            # print(c) we want only 1&2 element of b.
            dic["cast name"]=c
        list.append(dic)
    # print(list) store names in dic and append dics in list.
    for k in list:
        if k=={}:
            list.remove(k)
        # print(list) remove empty dics from the data in list.
    with open("task12.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
scrape_movie_cast(div)
