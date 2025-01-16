import requests
from bs4 import BeautifulSoup
import os 
page = requests.get("https://www.yallakora.com/match-center/مركز-المباريات?date=1/16/2025#days")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    championships = soup.find_all("div", {"class": "matchCard"})
    
    def get_match_info(championship):
        champoinship_title = championship.contents[1].find('h2').text.strip()
        matches = championship.contents[3].find_all("div", {"class": "item future liItem"})
        print(f"the num of matches = {len(matches)}")
        for match_ in matches:
            teamA = match_.find("div", {"class": "teamA"}).text.strip()
            teamB = match_.find("div", {"class": "teamB"}).text.strip()
            match_time = match_.find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()
            print(f"{teamA} against {teamB} the match time is {match_time}")
    x=1
    for championship in championships:
        print(f"===============\n champion ship num {x}\n ===============" )
        get_match_info(championship)
        x+=1

main(page)
