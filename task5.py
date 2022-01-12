
import json
import pprint
from task4 import scrap_movies_details
from task1 import scrap_top_list
all_data=scrap_top_list()
movie_details=scrap_movies_details
list=[]
def get_movie_list_details(all_data):
    for i in all_data:
        # loop iterating on keys of task1.
        # print(i["url"]):- loop on url in all data getting urls.
        all_movie_data=(scrap_movies_details(i["url"]))
        # (i["url"]):-link 
        # contaning movie data stored in variable.
        list.append(all_movie_data) 
        # appending the data of given link  of i iterating on task1 and taking data from task4.
    with open("task5.json","w+") as file:
        json.dump(list,file,indent=4)   
    return list
get_movie_list_details(all_data)
# pprint.pprint(get_movie_list_details(all_data))


# loop on task1 url
# that url link taking data from task4
# data append in list and return it

