import json
with open("task5.json","r+") as file:
    movies_list=json.load(file)
def analyse_language_and_directors():
    dic={}
    for i in movies_list:
        # pprint.pprint(i) here am getting all the data in dic.
        if "director" in i:
            director_list=i["director"]
            for director in director_list:
                if director not in dic:
                    dic[director]={}
                    if "language" in i:
                        language=i["language"]
                        if language not in dic[director]:
                            dic[director][language]=0
                        else:
                            dic[director][language]+=1
                    else:
                        pass
                else:
                    if "language" in i:
                        language=i["language"]
                        if language not in dic[director]:
                            dic[director][language]=0
                        else:
                            dic[director][language]+=1
                    else:
                        pass
        else:
            continue
    with open("task10.json","w+") as file:
        json.dump(dic,file,indent=4)  
    return dic 
(analyse_language_and_directors())