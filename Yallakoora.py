import csv
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# Get date 
while True:
    try:
        print("-" * 30)
        date = input("Enter date in the following format: MM/DD/YYYY: ")
        print("-" * 30)
        datetime.strptime(date, "%m/%d/%Y")
        break
    except ValueError:
        print("Invalid date format")

page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

if page.status_code != 200:
    print("Page Not Found. Try again later.")
    sys.exit()

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    match_details = []

    championships = soup.find_all("div", {"class": "matchCard"})

    for champ in championships:
        championship_title = champ.find("h2").text.strip()

        matches = champ.find_all("div", {"class": "item"})

        for match in matches:
            team_A = match.find("div", {"class": "teamA"}).find("p").text.strip()
            team_B = match.find("div", {"class": "teamB"}).find("p").text.strip()
            result = match.find("div", {"class": "MResult"})
            scores = result.find_all("span", {"class": "score"})

            match_score = f"{scores[0].text.strip()} - {scores[1].text.strip()}" 
            time = result.find("span", {"class": "time"}).text.strip()

            match_details.append({
                "البطولة": championship_title,
                "توقيت المباراة" : time,
                "الفريق الأول": team_A,
                "الفريق الثاني": team_B,
                "النتيجة": match_score
            })

    if match_details:
        with open("Today's matches.csv", "w", newline='', encoding='utf-8-sig') as file:
            keys = match_details[0].keys()
            dict_writer = csv.DictWriter(file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(match_details)
        print("Match data saved to 'Today's matches.csv'")
    else:
        print("No match data found for this date.")

main(page)
