from bs4 import BeautifulSoup

html = """
<table>
<tr><td>Akash</td><td>22</td><td>Fever</td><td>Dr. Smith</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")

for r in rows:
    cols = r.find_all("td")
    print(
        cols[0].text,
        cols[1].text,
        cols[2].text,
        cols[3].text
    )
