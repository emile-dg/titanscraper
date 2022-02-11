from os import curdir
from posixpath import abspath
from titanscraper import TitanScraper
from pprint import pprint


scraper = TitanScraper()

targets = [
    "https://www.google.com/search?q=hello"
]

print(abspath(curdir))

rules = scraper.load_rules("rules-1.json")
pprint(rules)

data = scraper.scrap(targets, rules)
pprint(data)