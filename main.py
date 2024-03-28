
from bs4 import BeautifulSoup
import requests
import sqlite3
import re
import os

def get_teams_playing(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    titles = soup.find_all('table')
    East_reg = titles[12].find_all('a')
    West_reg = titles[18].find_all('a')
    South_reg = titles[24].find_all('a')
    Midwest_reg = titles[30].find_all('a')
    teams = []
    team_id = 1
    for link in South_reg:
        tup = (link.get('title'), team_id, "West Region", link.get('href'))
        teams.append(tup)
        team_id +=1 
    for link in East_reg:
        tup = (link.get('title'), team_id, "East Region",link.get('href'))
        teams.append(tup)
        team_id +=1 
    for link in Midwest_reg:
        tup = (link.get('title'), team_id, "South Region", link.get('href'))
        teams.append(tup)
        team_id +=1 
    for link in West_reg:
        tup = (link.get('title'), team_id, "Midwest Region", link.get('href'))
        teams.append(tup)
        team_id +=1 
    return teams


if __name__ == '__main__':
    print('running :) ...')
    teams = get_teams_playing('https://en.wikipedia.org/wiki/2024_NCAA_Division_I_men%27s_basketball_tournament')
    print("Hello")