import json
with open("task5.json","r+") as file:
    movies_list=json.load(file)
def analyse_movies_genre():
    dic={}
    for i in movies_list:
        if "Genre" in i:
            genre_list=i["Genre"] 
            for genre in genre_list:
                if genre=="&":
                    continue
                if genre not in dic:
                    dic[genre]=0
                else:
                     dic[genre]+=1
    with open("task11.json","w+") as file:
        json.dump(dic,file,indent=4)   
    return dic
analyse_movies_genre()