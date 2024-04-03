# scraping to make our own BPI
# https://www.espn.com/mens-college-basketball/bpi/_/group/100

# https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100

# need to account for robots.txt since we are in a domain we don't know

# using team names as keys for the dictionary 
# value will be a list wins, losses, win percentage, sor
#imports
import sys
import os
import requests
from bs4 import BeautifulSoup


# this is a function to crawl the resume website of each team (https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100)
def crawl_resume():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_74; rv:12.0) Gecko/20100101 Firefox/12.0"}
    r = requests.get("https://www.espn.com/mens-college-basketball/bpi/_/view/resume/group/100", headers=headers, allow_redirects=False)
    data = BeautifulSoup(r.text, 'html.parser')
    # remove the sgml tags first
    print(type(data))
    # print(data)
    # get rid of everything above
    start = data.find('class="TABLE__TBODY"><tr')
    print(start)
    #data = data[start:]
    with open ("scrape_output.txt", 'w') as out:
        out.write(data)
    print("Hello2")
    # team_info = data.find('div', class_ = "theme-light")
    # print(team_info)
    # print(team)
    # teamDataDictionary = {}
    

# this is a function to create win percentages for every team (given a dictionary with team wins and loses)
# def create_win_percentage(teamDataDictionary):
#     for teams in teamDataDictionary:
        
# need to scrape sosrk not sor 
        
if __name__ == '__main__':
    print("Hello")
    crawl_resume()