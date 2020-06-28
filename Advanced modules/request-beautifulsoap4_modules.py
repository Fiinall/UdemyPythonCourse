import requests

from bs4 import BeautifulSoup

url = input("Please enter the URL")

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

tag = input("You can enter the tag of what you look for")
clas = input("You can enter the class of the thing you look for")

thing = soup.find_all(tag,{"class":clas})
print("Now there is list called 'thing'")
for i in thing:
    print(i)


