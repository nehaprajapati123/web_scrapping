from bs4 import BeautifulSoup
import requests
import json
import pprint
RT_link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
# RT_link is your url or rotantomamto which we are requesting.
# print(RT_link):-its gives you <response[200]> due to success of sending request.
# by the use of content you will get the material in link in text form.
in_html=BeautifulSoup(RT_link.text,'html.parser')
# we are using beautifulsoup  for converting our RT.text into htlm form.
# print(in_html):- it will give you content in html form so that you can understand the code.
def scrap_top_list():
    div=in_html.find('div',class_="body_main container")
    # we scrape main div(the whole content),fine for search a particular class
    table=div.find('table',class_="table")
    # scrape the table from div
    tr=table.find_all('tr')
    # scrape all the tr(table row) by find_all from table, tr are the rows
    # take a dictionary for updating all the table data.
    details=[]
    for i in tr:
        tds=i.find_all('td')
        # scrape td(table data) from tr.
        dic={}
        for j in tds:
            rank=i.find('td',class_="bold").get_text()[:-1]
            # here "." after s.no is coming for avoinding i use slicing
            dic["rank"]=rank
            rating=i.find('span', class_="tMeterScore").get_text()[1:]
            dic["rating"]=rating
            title=i.find('a',class_="unstyled articleLink")["href"][3:]
            dic["movie name"]=title
            num_of_review=i.find('td',class_="right hidden-xs").get_text()
            dic["number of reviews"]=num_of_review
            url=i.find('a',class_="unstyled articleLink")["href"]
            link="https://www.rottentomatoes.com"+url
            dic["url"]=link
            year=i.find('a',class_="unstyled articleLink").get_text().strip()[-5:-1]
            dic["year"]=year
        if dic=={}:
            del dic
            # we took this condition here becuase here will be empty dictionary in your list it should be remove.
        else:
            details.append(dic)
            # aapend your 100dic one by one in the list
    with open("task1.json","w+") as file:
        json.dump(details,file,indent=4)
        return details
        # store the whole data in json file and use pprint for output in sequencial form.
    
pprint.pprint(scrap_top_list())

 
