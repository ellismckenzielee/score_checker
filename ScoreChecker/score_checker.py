import requests
from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.theguardian.com/football/live'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(URL)

page_source = driver.page_source
#page = requests.get(URL, headers=headers)

#soup = BeautifulSoup(page.content, 'html.parser')

soup = BeautifulSoup(page_source, 'lxml')
teams = soup.findAll('div', {'class': ['football-team__name', 'team_name']})
goals = soup.findAll('div', {'class': 'football-team__score'})
home_teams = []
away_teams = []
home_team_goals = []
away_team_goals = []
print(len(goals))

#print(matches)
print(goals)
for i, team in enumerate(teams):
    print(team)
    if i % 2 == 0:
        home_teams.append(team.find('span').string)
    else:
        away_teams.append(team.find('span').string)
print(home_teams)
print(away_teams)

for i, goal in enumerate(goals):
    print(goal)
    if i % 2 == 0:
        home_team_goals.append(goal.getText())
    else:
        away_team_goals.append(goal.getText())

print(home_team_goals)
print(away_team_goals)

for i, score in enumerate(home_team_goals):
    if score == '':
        home_team_goals[i] = 'X'

for i, score in enumerate(away_team_goals):
    if score == '':
        away_team_goals[i] = 'X'


for i, team in enumerate(home_teams):
    print(team + '  ' + home_team_goals[i] + ' : ' + away_team_goals[i] + '  ' + away_teams[i])