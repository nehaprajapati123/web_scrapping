import os 
# os:-operating system.
# the os module use for operating the creation and removal of folders.
import json
import requests
with open("task1.json","r+") as file:
    task1_data=json.load(file)
    # read the task1 data we want the movie's whole data through link.
def movie_files():
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
movie_files()

