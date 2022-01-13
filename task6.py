import pprint
import json
from task5 import get_movie_list_details
movie_list=get_movie_list_details()
def analysis_movie_language():
    dic={}
    for i in movie_list:
        if "language" in i:
            a=i["language"]
            if a not in dic:
                dic[a]=1
            else:
                dic[a]+=1
        else:
            pass
    with open("task6.json","w+") as file:
        json.dump(dic,file,indent=4)  
    return dic
print(analysis_movie_language())