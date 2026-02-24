import requests as rq
from bs4 import BeautifulSoup
url = input("Enter Link: ")
if ("https" or "http") in url:
data = rq.get(url)
else:
data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
50-useful-python-scripts-free-pdf-download.md 12/05/2022
5 / 65
links = []
for link in soup.find_all("a"):
links.append(link.get("href"))
# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("myLinks.txt", 'a') as saved:
print(links[:10], file=saved)
