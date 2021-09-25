from os import execle
from titanscraper import TitanScraper


scraper = TitanScraper()
RULES = [
    {
        "name": "price",
        "selector": "span[itemprop='price']",
        "type": float,
        "attribute": "content"
    },
    {
        "name": "currency",
        "selector": "span[itemprop='priceCurrency']",
        "type": str,
        "attribute": "content"
    },
    {
        "name": "neigborhood",
        "selector": "span[itemprop='addressLocality']",
        "type": str
    },
    {
        "name": "rooms",
        "selector": ".new-attr-style>h3:nth-child(1)>span",
        "type": int
    },
    {
        "name": "surface",
        "selector": ".new-attr-style>h3:nth-child(2)>span",
        "type": str
    }
]
PAGINATION_START = 532
PAGINATION_LIMIT = 6919
BASE_WEBSITE = "https://www.jumia.cm"
 
with open('data.csv', 'a+') as csv_file:

    # for every page, get the links in the page
    for page in range(PAGINATION_START, PAGINATION_LIMIT):
        print(f"#--- Scraping page {page} ---#")

        webpage = f"/en/douala/real-estate?page={page}"
        link_filter_rule = ".product-click:not(.vip) a.post-link"
        
        targets = scraper.get_links_from_page(BASE_WEBSITE, webpage, rule=link_filter_rule)

        try:
            rows = scraper.scrap(targets, RULES)
        except Exception as e:
            print(f"""!!---- \nUnexpected error occured\n------------------------\n{e}.\nSkipping page!""")
        else:
            for row in rows:
                row_tuple =  scraper.dict_to_datalist(row)
                # for every value in the row, write it to the csv file
                for value in row_tuple:
                    csv_file.write(str(value))
                    csv_file.write(",")
                # move to the next line
                csv_file.write('\n')

        print("-"*50)