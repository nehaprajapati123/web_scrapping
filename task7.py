import json
import pprint
from task5 import get_movie_list_details
movies=get_movie_list_details()
def analysis_movies_director():
    dic={}
    # print(movies)
    for i in movies:
        # print(i["director"])
        if "director" in i:
            a=i["director"]
            # print(a)
            for j in a:
                # print(j)
                if j not in dic:
                    a=j
                    dic[j]=1
                else:
                    dic[j]+=1
        else:
            continue
    with open("task7.json","w+") as file:
        json.dump(dic,file,indent=4)  
    return dic   
analysis_movies_director()
