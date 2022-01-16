import pprint
import json
with open("task5.json","r+") as file:
    movies_list=json.load(file)
def analysis_movies_language():
    dic={}
    for i in movies_list:
        if "language" in i:
            a=i["language"]
            if a not in dic:
                dic[a]=0
            else:
                dic[a]+=1
        else:
            pass
        #  loop moving on the dics containing all data
        # if dic contain language if language is not dic so language count=1
        # f language is in dic so language count will increment
    with open("task6.json","w+") as file:
        json.dump(dic,file,indent=4)  
    return dic
print(analysis_movies_language())
