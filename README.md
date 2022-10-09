# The Championship Material
Hello Everyone. This a project for Data Analysis that I have been studying for a long time now. The WWE Championship is widely recognized as the most historic championship in WWE. 

Dating back to 1963, the WWE Champions are picked by the company that could represent their status in the market and brings them the highest ratings. I am huge fan of wwe and wanted to create a dashboard which will show the trend of superstars being picked to represent the company on basis of their height and weight.


## Acknowledgements

 - [WWE](https://www.wwe.com/)
All the data, I have used in this project is picked form the official website of WWE and I have used it to create a personal portfolio project. I do not owe or pretend to owe any data copyrights.


## Collection of Data
First I went on to collect the data from WWE's [Website](https://www.wwe.com/titlehistory/wwe-championship) of the championship history with help of following python script. I used BeautifulSoup and pandas to retrieve and collect the data in my local CSV file.

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.wwe.com/titlehistory/wwe-championship"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
champ_elements = soup.find_all("tr", class_="js-track")


wrestler_name = []
wrestler_dates = []
wrestler_time= []


for champ_element in champ_elements:
    name = champ_element.find("td", class_="champ")
    dates = champ_element.find("td", class_="reign-dates")
    time = champ_element.find("td", class_="time-held")
    wrestler_name = wrestler_name + [name.text]
    wrestler_dates = wrestler_dates + [dates.text]
    wrestler_time = wrestler_time +[time.text]
#==================================

wrestler_data_into_json = {
    'wrestler_name': wrestler_name,
    'wrestler_dates': wrestler_dates,
    'wrestler_time': wrestler_time,
}

#saving the data retrived from the page
df_wrestlers = pd.DataFrame(wrestler_data_into_json)
df_wrestlers.to_csv('wwe_champions.csv', mode='w', index=False, header=False)

#===========saving the championship with their counts
df_wrestlers_count = pd.DataFrame(df_wrestlers['wrestler_name'].value_counts().rename_axis('unique_values').reset_index(name='counts'))
df_wrestlers_count.to_csv('wwe_champions_times.csv', mode='w', index=False, header=False)

```
The two CSV files name "wwe_champions.csv" and "wwe_champions_times.csv" will be the output of this script. 

### All superstar data

I went on to collect the data from WWE's [Website](https://www.wwe.com/titlehistory/wwe-championship) of all the wwe superstars with help of following python script. I used BeautifulSoup and pandas to retrieve and collect the data in my local CSV file.

I couldn't find data with easy way so I had to implement selenium package. 

```python 

# import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import html
  
# create webdriver object
driver = webdriver.Firefox(executable_path="C:/Users/JagatJungLakandriBK/Downloads/Programs/geckodriver.exe")

#souce to get all the superstars
driver.get("https://www.wwe.com/superstars")

#the code of whole page
soup = BeautifulSoup(driver.page_source, "html.parser")

#we extact all the option tags from the page
job_elements =soup.find_all("option")

driver.close()

mywrestlers = []
# now we get all the required data 
for a in job_elements:
    # print(a.getText())
    mywrestlers = mywrestlers + [str(a['value'])]

print(len(mywrestlers))
super_star_collections = []
sup_attribute= []
#getting data of each individual superstar

i = 0
for sups in mywrestlers:

    URL = "https://www.wwe.com"+sups    
    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        job_elements =soup.find("div", class_="wwe-talent__stats")

        super_name = "NA"
        super_height ="NA"
        super_weight = "NA"
        super_town = "NA"
        super_move = "NA"
        super_highlight = "NA"

        if(job_elements.find("div", class_="wwe-talent__stats--name") is not None):
            super_name = job_elements.find("div", class_="wwe-talent__stats--name").p.get_text()
        
        if(job_elements.find("div", class_="wwe-talent__stats-profile--height") is not None):
            super_height = job_elements.find("div", class_="wwe-talent__stats-profile--height").p.get_text()
        
        if(job_elements.find("div", class_="wwe-talent__stats-profile--weight") is not None):
            super_weight = job_elements.find("div", class_="wwe-talent__stats-profile--weight").p.get_text()

        if(job_elements.find("div", class_="wwe-talent__stats-profile--hometown") is not None):
            super_town = job_elements.find("div", class_="wwe-talent__stats-profile--hometown").p.get_text()
        
        if(job_elements.find("div", class_="wwe-talent__stats-profile--signature") is not None):
            super_move = job_elements.find("div", class_="wwe-talent__stats-profile--signature").p.get_text()
        
        if(job_elements.find("div", class_="wwe-talent__stats-profile--highlights") is not None):
            super_highlight = job_elements.find("div", class_="wwe-talent__stats-profile--highlights").p.get_text()
        
        # super_name = job_elements.find("div", class_="wwe-talent__stats-profile--highlights").p.get_text()
        sup_attribute =[super_name] + [super_height]+ [super_weight] + [super_move] + [super_town] + [super_highlight]
        super_star_collections = super_star_collections + [sup_attribute]
        sup_attribute =[]
        print(super_name)
    except:
        print("no data for")
        print(URL)
    i=i+1
    # print(i)
    # if(i>20):
    #     break

df_wrestlers = pd.DataFrame(super_star_collections)
print(df_wrestlers)
df_wrestlers.to_csv('wwe_superstar_data.csv', mode='w', index = False, encoding = 'utf-8-sig')

```

it took lots of time for me to extract data at first hand but I finally did it. The process is quite slow since each superstars site will be visited and the data will be extracted from that.


## Cleaning the data
After I collected the data, I had to prepare it. I went ahead and uploaded the data in my Google Sheet 
[Uncleaned Data from Web Scrapping](https://docs.google.com/spreadsheets/d/1q2JQJgYbR0KTkoeDBBwfMDnBdSY_U7mdwMui9LssnYg/edit?usp=sharing)

The, I cleaned the data and stored it in new sheet [cleaned Data from Web Scrapping](https://docs.google.com/spreadsheets/d/1bKzMvAisY098uhg1O0dt4Ts6N7iVLEozL4GmqZXRbNA/edit?usp=sharing)

## Visualization
I decided to go on with Tableau to visualize my cleaned data. And I create a dashboard [The WWE Championship Material](https://public.tableau.com/views/TheWWEChampionshipMaterial/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link) with the data.   

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)


[I wanted to do it with python or R but data was not that huge. Also, it is better to practise all the tools.]

## Conclusion
It was fun doing the project. I hope, I didn't made much mistakes. It is just my first project so, I am hoping lots of positive feedbacks.

## Feel Free to contact me
- [Twitter](https://twitter.com/DataLakandri)
- [Linkedin](https://www.linkedin.com/in/jagat-jung-lakandri-bk-361b94245/)
