import requests
from bs4 import BeautifulSoup

# Website URL
url = input("Enter website link: ")

# Add https if not present
if not url.startswith("http"):
    url = "https://" + url

# Get webpage content
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract links
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

# Save links to file
with open("myLinks.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

print("Links saved to myLinks.txt")
