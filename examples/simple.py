from src import TitanScraper
from pprint import pprint


scraper = TitanScraper()

targets = [
    "https://www.jumia.cm/toyota-aygo-2008-occasion-pid10918856"
]

rules = [
    {
        "name": "article_name",
        "selector": ".heading-area",
    },
    {
        "name": "article_description",
        "selector": "div[itemprop='description']",
    }
]

data = scraper.scrap(targets, rules)
pprint(data)