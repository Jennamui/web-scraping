#import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.stonybrook.edu/sb/bulletin/current/search/bysbc/index.php')

#create BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#print pretty
print(soup.prettify())

#Get Course Names
titles = soup.find_all('div',class_='webny-teaser-title')
output_titles = []
for i in titles: #for x in y: 
    print(i.text)
    data = i.text
    output_titles.append(data)

len(output_titles)

#Get Course Descriptions
descriptions = soup.find_all('div',class_='webny-card-description')
output_descriptions = []
for i in descriptions: 
    print(i.text)
    data = i.text
    output_descriptions.append(data)

#create lists
list1= output_titles
list2= output_descriptions

#create new dictionary with new lists
dictionary = {'names': list1, 'descriptions': list2}

#create new dataframe
df = pd.DataFrame({'names':output_titles,'descriptions': output_descriptions})

#save dataframe to csv file
df.to_csv('/Users/jennamui/Documents/GitHub/web-scraping/cdc_website_news.csv')
