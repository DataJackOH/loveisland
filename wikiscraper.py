#!/usr/bin/env python
# coding: utf-8



import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

import plotly.express as px

from sklearn.metrics import confusion_matrix
import numpy as np



##scrape 3 tables from LI wikipedia
##candidates, couples and tv ratings
def candidate_scraper(url, series):
    ##find url
    wikiurl = url
    table_class="wikitable"
    response=requests.get(wikiurl)
    
    ##scrape
    soup = BeautifulSoup(response.text, 'html.parser')
    ## find all tables
    table=soup.find_all('table',{'class':"wikitable"})
    
    ##convert to df 
    df=pd.read_html(str(table))
    ##index 0 is candidates
    candidates=pd.DataFrame(df[0])
    candidates['series'] = series
    #index 1 is couples
    couples=pd.DataFrame(df[1])
    couples['series'] = series
    #index 3 is tv ratings
    ratings=pd.DataFrame(df[3])
    ratings['series'] = series
    return candidates, couples, ratings

##run for each wikipedia page

series1_candidates, series1_couples, series1_ratings = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_1)', series=1)
series2_candidates, series2_couples, series2_ratings = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_2)', series=2)
series3_candidates, series3_couples, series3_ratings  = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_3)', series=3)
series4_candidates, series4_couples, series4_ratings  = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_4)', series=4)
series5_candidates, series5_couples, series5_ratings  = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_5)', series=5)
series6_candidates, series6_couples, series6_ratings  = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_6)', series=6)
series7_candidates, series7_couples, series7_ratings  = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_7)', series=7)
series8_candidates, series8_couples, series8_ratings = candidate_scraper(url='https://en.wikipedia.org/wiki/Love_Island_(2015_TV_series,_series_8)', series=8)



##LIST OF DATAFRAMES
candidates = [series1_candidates,series2_candidates,series3_candidates,series4_candidates,series5_candidates,series6_candidates
             ,series7_candidates,series8_candidates]


couples = [series1_couples,series2_couples,series3_couples,series4_couples,series5_couples,series6_couples
             ,series7_couples,series8_couples]


ratings = [series1_ratings,series2_ratings,series3_ratings,series4_ratings,series5_ratings,series6_ratings
             ,series7_ratings,series8_ratings]



# concatenate each dataframe
candidates = pd.concat(candidates,axis=0)


couples = pd.concat(couples,axis=0)


ratings = pd.concat(ratings, axis=0)


candidates.to_csv('candidates.csv')
couples.to_csv('couples.csv')
ratings.to_csv('ratings.csv')

