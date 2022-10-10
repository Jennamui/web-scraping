#import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://classfind.stonybrook.edu/vufind/Search/Results?lookfor=&type=AllFields&submit=Find')

#create BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#print pretty
print(soup.prettify())

#Get Course Names
names = soup.find_all('div',class_='resultItemLine1')
course_names = []
for i in names: 
    print(i.text)
    data = i.text
    course_names.append(data)


len(course_names)

#Get Course Professor
professor = soup.find_all('div',class_='resultItemLine2')
course_professor = []
for i in professor: 
    print(i.text)
    data = i.text
    course_professor.append(data)

#create lists
list1= course_names
list2= course_professor

#create new dictionary with new lists
dictionary = {'names': list1, 'time': list2}

#create new dataframe
df = pd.DataFrame({'names':course_names,'descriptions': course_professor})

#save dataframe to csv file
df.to_csv('/Users/jennamui/Documents/GitHub/web-scraping/sbu_classfind.csv')
