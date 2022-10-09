import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.wwe.com/titlehistory/wwe-championship"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("tr", class_="js-track")

#=============declearing the variables 
wrestler_name = []
wrestler_dates = []
wrestler_time= []

#=====collecting the data===============
for job_element in job_elements:
    name = job_element.find("td", class_="champ")
    dates = job_element.find("td", class_="reign-dates")
    time = job_element.find("td", class_="time-held")
    wrestler_name = wrestler_name + [name.text]
    wrestler_dates = wrestler_dates + [dates.text]
    wrestler_time = wrestler_time +[time.text]
#==================================

wrestler_data_into_json = {
    'wrestler_name': wrestler_name,
    'wrestler_dates': wrestler_dates,
    'wrestler_time': wrestler_time,
}
 
df_wrestlers = pd.DataFrame(wrestler_data_into_json)

df_wrestlers.to_csv('wwe_champions.csv', mode='w', index=False, header=False)

df_wrestlers_count = pd.DataFrame(df_wrestlers['wrestler_name'].value_counts().rename_axis('unique_values').reset_index(name='counts'))
print(df_wrestlers_count)
df_wrestlers_count.to_csv('wwe_champions_times.csv', mode='w', index=False, header=False)
