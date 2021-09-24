
class TitanScraper():

    AUTHOR = "Emile DJIDA GONGDEBIYA"
    VERSION = "1.0.0"

    TARGETS = tuple()

    scraped_data = dict()

    def __init__(self, targets:tuple) -> None:
        print(f"TitanScraper version {self.VERSION}")
        self.TARGETS = targets

    def start(self):
        pass