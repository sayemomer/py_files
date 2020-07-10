import requests
from colorama import Fore,Style
from bs4 import BeautifulSoup

response = BeautifulSoup(requests.get('https://www.thedailystar.net/').content,'html.parser')
#print(response.title)
#print(response.get_text())

a_tags= response.select('h1 a ')[0]

print(Fore.RED + a_tags.get_text());

latest_news = response.select('h5 a')
number = 1

for news in latest_news:
	print(Fore.BLUE + str(number) +' : '+ news.get_text())
	number=number+1

#print(a_tags[0])
# for link in a_tags:
# 	print(link.get_text())

