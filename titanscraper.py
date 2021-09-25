import requests
from bs4 import BeautifulSoup


class TitanScraper():

    AUTHOR = "Emile DJIDA GONGDEBIYA"
    VERSION = "1.0.0"

    TARGETS = tuple()
    HTML_PARSER = "lxml"

    def __init__(self) -> None:
        print(f"TitanScraper version {self.VERSION}")

    def __get_raw_html(self, link:str, timeout=5) -> tuple:
        """Gets the raw html of a given link.
        
        Arguments:
        `link` -- the actual webpage address to get\n
        `timeout` -- time in seconds to wait for the resource

        Return -- (response_status_code:int, html_doc:str|None)
        
        Error -- in case of a timeout or connection error, it returns (0, None)
        """
        try:
            response = requests.get(link, timeout=timeout)
        except requests.Timeout as error:
            print("Timeout error")
            return (0, None)
        else:
            return (response.status_code, response.content)


    def __parse_data(self, html_doc:str, rules:tuple) -> dict:
        """Parse a given html document following a given set of rules and return the data"""
        soup = BeautifulSoup(html_doc, self.HTML_PARSER)
        data = {}
        for rule in rules:
            temp = soup.select(rule.get('selector'))
            if temp:
                temp = temp[0]
                # create an entry with the rule name as key and the selected 
                # element's attribute value of text content
                value = temp.get(rule['attribute']) if rule.get("attribute") else str(temp.contents[0])
                # cast the value to the given type else just leave it as string  
                try:
                    data[rule.get('name')] = rule['type'](value) if rule.get('type') else value
                except:
                    raise
        return data


    def scrap(self, targets:tuple, rules:dict) -> list:
        """Scraps a list of target webpages and returns the data.
        
        Arguments:\n
        `targets` -- the target webpages to scrap\n
        `rules` -- list of DOM selector rules to extract the data from.
            The format is as follows 
            [
                {
                    "name": str,
                    "selector": str,
                    "type": int | str | bool | float , ! defualt str | None
                    "default": Any,
                    "attribute": str !if given, it will get the data from the given attribute
                },
                ...
            ]
        """
        results = []
        for target in targets:
            print("- processing ", target)
            _ , raw_html = self.__get_raw_html(target)
            if raw_html:
                try:
                    data = self.__parse_data(raw_html, rules)
                    print(data)
                except Exception as e:
                    print(e, "occured, skipping page!")
                else:
                    results.append(data)
        return results

    
    def get_links_from_page(self, target, page, rule=''):
        """Get all links in a given page if no rule is passed, else based on the css selector"""
        _, raw_html = self.__get_raw_html(target+page)
        soup = BeautifulSoup(raw_html, self.HTML_PARSER)
        if rule:
            return [ target + link.get('href') for link in soup.select(f'{rule}') ] 
        else:
            return [ target + link.get('href') for link in soup.select('a') ] 

    def dict_to_datalist(self, _dict:dict) -> tuple:
        """returns a tuple of values from a dict"""
        return tuple( _dict.values() )