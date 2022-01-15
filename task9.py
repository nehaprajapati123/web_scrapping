from http.client import ImproperConnectionState
import json
import requests
import os
import random
import time
with open("task1.json","r+") as file:
    task1_data=json.load(file)
    # task1 data store in variable
def movie_files():
    time_gap=random.randint(1,3)
    # random.randim for choosing random integer for time gap 
    for i in task1_data:
        address="/home/admin123/webscrapping/task8"+i["movie name"]+".text"
        # loop on data 
        # creation of files through the parent folder
        # naming it at the address+ movie name in text form
        if os.path.exists(address):
            pass
                # if file exist on that address then paas
        else:
            make=open(address,"w")
            # else open a file
            movie_url=requests.get(i["url"])
            # requesting the movie link for the content
            make.write(movie_url.text)
            # store the  movie data in file
            make.close()
    time.sleep(time_gap)
    # for gapping between the files opening
movie_files()
