import random

rand = random.randint(1,30) 
import requests
import bs4
url = requests.get("https://www.goodreads.com/quotes/tag/love")
html = url.text
html_parser = bs4.BeautifulSoup(html, "html.parser")
quotes = html_parser.findAll("div", {"class" : "quoteText"},limit=rand)
quote1 = quotes
for quote in quote1:
    quote3 = quote
    
print(quote3.text)