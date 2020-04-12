
from bs4 import BeautifulSoup
import pandas as pd
import os

from selenium import webdriver

BASE = (os.path.dirname(os.path.realpath(__file__)))


def __win_rate__():
    driver = webdriver.Chrome(BASE + './chromedriver') 
    driver.get("https://www.dotabuff.com/heroes/winning?date=week")
    
    text = driver.page_source
    driver.quit()

    soup = BeautifulSoup(text, 'html.parser')
    
    article = soup.find("tbody")
    heros = article.find_all("tr")
    
    top_10 = []
    for hero in heros[:5]:
        td = hero.find_all("td")
        top_10.append([td[i]['data-value'] for i in range(1,5)])
    
    df = pd.DataFrame(top_10, columns=['Hero','Win Rate','Pick Rate','KDA Ratio'])
    df.to_csv(BASE +"/../App/assets/csv/hero_win_top5.csv", index=False)


def __most_played__():
    driver = webdriver.Chrome(BASE + './chromedriver') 
    driver.get("https://www.dotabuff.com/heroes/played?date=week")
    
    text = driver.page_source
    driver.quit()

    soup = BeautifulSoup(text, 'html.parser')
    article = soup.find("tbody")
    heros = article.find_all("tr")
    
    top_10 = []
    for hero in heros[:5]:
        td = hero.find_all("td")
        top_10.append([td[i]['data-value'] for i in range(1,6)])
    
    df = pd.DataFrame(top_10, columns=['Hero','Matches Played','Pick Rate','Win Rate','KDA Ratio'])
    df.to_csv(BASE +"/../App/assets/csv/hero_most_played_top5.csv", index=False)


def __meta__():
    driver = webdriver.Chrome(BASE + './chromedriver') 
    driver.get("https://www.dotabuff.com/heroes/meta")
    
    text = driver.page_source
    driver.quit()

    soup = BeautifulSoup(text, 'html.parser')
    article = soup.find("tbody")
    heros = article.find_all("tr")
    
    top_10 = []
    for hero in heros:
        td = hero.find_all("td")
        top_10.append([td[i]['data-value'] for i in range(1,12)])
    
    df = pd.DataFrame(top_10, columns=['Hero',
                                       'rank 123 pick','rank 123 win',
                                       'rank 4 pick','rank 4 win',
                                       'rank 5 pick','rank 5 win',
                                       'rank 6 pick','rank 6 win',
                                       'rank 78 pick','rank 78 win',
                                       ])
    df.to_csv(BASE +"/../App/assets/csv/hero_meta.csv", index=False)

__win_rate__()
__most_played__()
__meta__()
