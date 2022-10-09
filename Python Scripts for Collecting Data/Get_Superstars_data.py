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