from bs4 import BeautifulSoup
import requests
import json
import pprint
from task4 import scrap_movies_details

url=("https://www.rottentomatoes.com/m/wall_e")
# url of given movie.
movie_link=requests.get(url)
# request that link data to server.
soup=BeautifulSoup(movie_link.text,'html.parser')
# convert the data in html form.
div=soup.find('div',class_="castSection")
# scrap the cast section where the names are there.
def scrape_movie_cast(div):
    list=[]
    for i in div:
        a=i.text
        b=a.split()
        # i in cast section, convert the data (i) in text form, and split(remove white spaces).
        # b=list(output) names is b.
        dic={}
        for j in b:
            c=b[0]+" "+b[1]
            dic["cast name"]=c
        list.append(dic)
        # j in b(list), want only 1&2 element= name
        # update name in dics, append all dic in list.
    for k in list:
        if k=={}:
            list.remove(k)
            # remove all empty dics in list of dic
    return list
task12=scrape_movie_cast(div)
# rask12=list of cast names.
task4=scrap_movies_details(url)
# task4=data of the given url.
def cast_details(task4):
    list1=[]
    list1.append(task4)
    for i in range(len(task12)):
        list1.append(task12[i])
        # append the data of movie through task4
        # append all dic from task12
    with open("task13.json","w+") as file:
        json.dump(list1,file,indent=4)
    return list1
cast_details(task4)

