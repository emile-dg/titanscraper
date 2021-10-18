TITANScraper 
=========
v0.0.1


Description
----------
This is a simple but quite usefull python library for scraping webpages easily and quickly. Give it a try!

Example
------
```python
from titanscraper import TitanScraper


RULES = [
    {
        "name": "article_data",
        "selector": "[class^='textnoir9bold']:nth-child(7)",
        "type": str,
    }
]
target_pages = [
    "https://www.target_website.fr/target_one",
    "https://www.target_website.fr/target_two",
    "https://www.target_website.fr/target_three",
    "https://www.target_website.fr/target_four",
]

scraper = TitanScraper()
data = scraper.scrap(target_pages, RULES)
print(data)
```
For more examples check the examples folder (coming soon)


Future Features
--------
- Javascript rendering support with selenium
- User agents support
- Proxy support and proxy rotation
- Captcha bypass
- JSON and YAML support for rules defintion
