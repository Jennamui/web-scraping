# web-scraping

1. Begin by importing the following packages:

import requests

from bs4 import BeautifulSoup

import pandas as pd

2. Find a website for the scraping and use the requests package to bring it into the python file

3. Create a beautiful soup object

4. For the CDC news site, I used the div tag and class="webny-teaser-title" to obtain all the titles of news statements

5. To obtain the descriptions of the articles, I used the div tage and class="webny-card-description"

6. After extracting all the information, I created two lists with the titles and descriptions

7. Create a new dictionary with the two lists

8. Create a new dataframe

9. Save the dataframe to a csv file