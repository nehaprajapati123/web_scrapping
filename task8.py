import os 
import json
import requests
with open("task1.json","r+") as file:
    task1_data=json.load(file)
def movie_files():
    for i in task1_data:
        address="/home/admin123/webscrapping/task8"+i["movie name"]+".text"
        if os.path.exists(address):
            pass
        else:
            make=open(address,"w")
            movie_url=requests.get(i["url"])
            make.write(movie_url.text)
            make.close()
movie_files()
