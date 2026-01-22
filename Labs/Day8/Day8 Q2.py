# 1. Fetches an HTML webpage using the requests library
from bs4 import BeautifulSoup
import requests
import json

from Day8.TC_Beautifulsoap import pagetitle

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
# 2. Parses the HTML using BeautifulSoup with the lxml parser
soup = BeautifulSoup(response.text, "lxml")

# 3. Extracts:Page title
pagetitle = soup.title.string if soup.title else "No title"

print(pagetitle)

# All hyperlinks
for links in soup.find_all("a"):
    href = links.get("href")
    print(href)

# Specific table or list data
data = []
table = soup.find("table")
if table:
    rows = table.find_all("tr")
    for row in rows[1:]:
        columns = row.find_all("td")
        row_data = [col.text.strip() for col in columns]
        print(row_data)
        data.append(row_data)

# 4. Converts the extracted data into JSON format
extracted_data = {
    "page_title": pagetitle,
    "total_links": len(href),
    "links": href,
    "table_data": data
}

with open("extracted_data.json", 'w', encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)

