from bs4 import BeautifulSoup

HTMLFile = open("bookmarks.html", "r")
html = HTMLFile.read()
soup = BeautifulSoup(html, 'html.parser')
anchors = soup.find_all('a')
linksWithNames = {}

for index, link in enumerate(anchors):
    if link.contents == []:
       link.contents = [f"This has no title ---- index={index}"] 
    linksWithNames[str(link.contents[0])] = link.get('href')
