from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

my_url = 'https://www.medicalnewstoday.com/articles/321533.php'
# data taken from

# Opening URl and grabbing content
Page = uopen(my_url)
page_html = Page.read()
Page.close()

# HTML parsing
page_soup = soup(page_html,"html.parser")#parses html data


body = page_soup.find("div",{"class":"article_body"})#finds all div tags with class = article_body
f = open("Could gut bacteria cause joint pain?.txt", "w") #opens a file and writes content to it

f.write(body.text)


f.close()  # Close the file
