from task1 import scrap_top_list
content=scrap_top_list()
# import data from task1 and store in content variable.
def group_by_decates(movies):
    year_dic={}
    unique_years=[]
    for i in movies:
        for j in i:
            if j=="year":
                if (i[j]) not in unique_years:
                    unique_years.append(i[j])
        unique_years.sort()
        # access the years from the (key)year from the data.
        # append only unique years and sort it.
    decate_list=[]
    for k in unique_years:
        rem=int(k)%10
        decate=int(k)-rem
        if decate not in decate_list:
            decate_list.append(decate)
            # iterate a loop on unique years my using (%) take out the reminder.
            # minus reminder from the year it will give you a decate.
            # append unique decate in decate list.(you get decates here)
    for index in decate_list:
        year_dic[index]=[]
        #year_dic= {index(decate):list(movies's detail of that particulae decate)}  
    for index in year_dic:
        dec10=int(index)+9
        for i in movies:
            for j in i:
                if j=="year":
                    if (int(i[j]))<=dec10 and (int(i[j]))>=index:
                        year_dic[index].append(i)
                    # dacate+9 (it will be the limit) eg.1950(decate)+9=1959(limit of decate)
                    # iterate the loop on all the 100 movie's year.
                    # if year<=decate and year>=limit of decate.
                    # append all the movies according to there decates.
    import json
    with open("task3.json","w+") as file:
        json.dump(year_dic,file,indent=4)
    return year_dic
import pprint
pprint.pprint(group_by_decates(content))
# store your data in the json file 