from task1 import scrap_top_list
import json
details=scrap_top_list()
# import all the details from task1 and stored in a valiable named details.
def group_by_year(movies):
    # in the function the parameter contain the details of task1..
    unique_years=[]
    for i in movies:
        # iterate the loop on all the keys. 
        year=i["year"]
        # i is iterating on years and storin the year in variable called year.
        if year not  in unique_years:
            unique_years.append(year)
            # here removing duplicate years by storing unique year in years.
    dic_of_movie={i:[] for i in unique_years}
    # loop in unique year + (key)i=unique year:[](year's detain in list will be value) 
    # dic of movie is a dic of unique year: year's detail
    for i in movies:
        year=i['year']
        for j in dic_of_movie:
            if str(j)==str(year):
                # if unique year== year in variable (detail).
                dic_of_movie[j].append(i)
                # append all the detail of the year in list and be the value of the year in dic of movie.
    with open("task2.json","w+") as file:
        json.dump(dic_of_movie,file,indent=4)
        # output in json file.
    return (dic_of_movie)
import pprint
pprint.pprint(group_by_year(details))
