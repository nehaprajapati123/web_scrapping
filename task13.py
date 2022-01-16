from bs4 import BeautifulSoup
import requests
import json
import pprint
from task4 import scrap_movies_details

url=("https://www.rottentomatoes.com/m/the_lego_movie")
movie_link=requests.get(url)
soup=BeautifulSoup(movie_link.text,'html.parser')
div=soup.find('div',class_="castSection")

def scrape_movie_cast(div):
    list=[]
    for i in div:
        a=i.text
        b=a.split()
        dic={}
        for j in b:
            c=b[0]+" "+b[1]
            dic["cast name"]=c
        list.append(dic)
    for k in list:
        if k=={}:
            list.remove(k)
    # with open("task12.json","w+") as file:
    #     json.dump(list,file,indent=4)
    return list
task12=scrape_movie_cast(div)
task4=scrap_movies_details(url)
def cast_details(data):
    list1=[]
    list1.append(data)
    for i in range(len(task12)):
        list1.append(task12[i])
    
    with open("task13.json","w+") as file:
        json.dump(list1,file,indent=4)
    return list1
cast_details(task4)

