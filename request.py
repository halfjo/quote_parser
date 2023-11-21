import requests
import bs4
import random
from termcolor import colored
rand = random.randint(1,30)



r = requests.get("https://goodreads.com/tag/")


quote_need = input("what the quote you want about : science-life-love : ") 
if quote_need == "science":
    url = requests.get("https://goodreads.com/quotes/tag/science")
    html = url.text
    html_parser = bs4.BeautifulSoup(html, "html.parser")
    quotes = html_parser.findAll("div", {"class" : "quoteText"},limit=rand)
    quote3 = ""
    for quote in quotes:
        quote3 = quote
    print(colored(quote3.text, "blue" , "on_green"))
elif quote_need == "life":
    url = requests.get("https://www.goodreads.com/quotes/tag/life")
    html = url.text
    html_parser = bs4.BeautifulSoup(html, "html.parser")
    quotes = html_parser.findAll("div", {"class" : "quoteText"},limit=rand)
    quote3 = ""
    for quote in quotes:
        quote3 = quote
    print(colored(quote3.text, "green" , "on_blue"))
elif quote_need == "love":
    url = requests.get("https://www.goodreads.com/quotes/tag/love")
    html = url.text
    html_parser = bs4.BeautifulSoup(html, "html.parser")
    quotes = html_parser.findAll("div", {"class" : "quoteText"},limit=rand)
    quote3 = ""
    for quote in quotes:
        quote3 = quote
    print(colored(quote3.text , "red" , "on_white"))
else:
    exit()