
class TitanScraper():

    AUTHOR = "Emile DJIDA GONGDEBIYA"
    VERSION = "1.0.0"

    TARGET_WEBSITES = ()

    scraped_data = dict()

    def __init__(self, target_websites:tuple) -> None:
        print(f"TitanScraper version {self.VERSION}")
        self.TARGET_WEBSITES = target_websites

    def start(self):
        pass