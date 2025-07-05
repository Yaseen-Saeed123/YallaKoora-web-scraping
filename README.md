# This is a web scraping project
Languages used: Python

Modules used: BeautifulSoup, requests & csv

# Simple description of how the program works
#### 1- The program asks the user to enter a certain date in the format (MM/DD/YYYY) and validates the input
#### 2- Then, the program injects the input into the url of YallaKoora page
#### 3- Then use the requests module to get the page, and beautiful soup to parse the contents
#### 4- Scrap the soup for: Championship title, Team A, Team B, Time, Score
#### 5- Save the previous info for each match in a dictionary
#### 6- Write these data in a csv file
