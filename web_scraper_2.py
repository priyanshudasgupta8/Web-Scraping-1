from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

start_link = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(start_link)
print(page)
soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

names = []
distance =[]
mass = []
radius =[]
lumo = []

for i in range(1,len(temp_list)):
    names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lumo.append(temp_list[i][7])
    
df_2 = pd.DataFrame(list(zip(names,distance,mass,radius,lumo)),columns=['names','distance','mass','radius','luminosity'])
print(df_2)
df_2.to_csv('stars_data.csv')