from task1 import scrap_top_list
scrap=scrap_top_list()
# import data from task1.
from bs4 import BeautifulSoup
import requests
import json
import pprint
def scrap_movies_details(url1):
    page=requests.get(url1)
    soup=BeautifulSoup(page.text,'html.parser')
    dic={}
    # requests movie url and transforming in html form.
    movie_name=soup.find('h1',class_="scoreboard__title").get_text()
    dic["movie_name"]=movie_name
    # print(movie_name):-TOY STORY 4 (access the movie name.)
    li=soup.find_all('li',class_="meta-row clearfix")
    for i in li:
        data=(i.text.split())
        # print(data)li is the whole data iterate a loop.
        # out will be in htlm use text and space removing use slit for output in list.
        # print(data)
        if "Rating:" in data:
            dic["rating"]=data[1]
        elif "Genre:" in data:
            dic["Genre"]=data[1:]
        elif "Original" in data:
            dic["language"]=data[2]
        elif "Producer:" in data:
            dic["producer"]=data[1:]
        elif "Director:" in data:
            w=data[1:]
            # print(w) direct name and sirname in different strings
            h=" "
            for i in w:
                h=h+i
            # print(h) all name in single string    
            split=h.split(",")
            # print(split) split the character where (,)
            dic["director"]=split
        elif "Runtime:" in data:
            time=data[1:]
            # print(time) access time data
            for i in time:
                if "h" in i:
                    hour=(int(i[:-1]))*60
                elif "m" in i:
                    min=(int(i[:-1]))
            dic["runtime"]=hour+min
    with open("task4.json","w+") as file:
        json.dump(dic,file,indent=4)   
    return dic
url1="https://www.rottentomatoes.com/m/the_lego_movie"  
scrap_movies_details(url1)
