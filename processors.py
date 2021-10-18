from os import replace


class BasicProcessors:

    def __init__(self) -> None:
        pass

#  Post Processors
class Integer(BasicProcessors):
    """Removes whatever whitespace to make a string valid for int casting but does not cast to integer. Characters and symbols are removed are ignored"""
    def __init__(self, initial_value:str) -> None:
        super().__init__()
        self.__value = initial_value

    def get_value(self) -> str:
        return "".join(self.__value.split())

class StringStripper(BasicProcessors):

    def __init__(self, initial_value:str) -> None:
        super().__init__()
        self.__value = initial_value

    def get_value(self) -> str:
        return str(self.__value.strip())

class ReplaceWith(BasicProcessors):

    def __init__(self, replace_item:str, with_item:str) -> None:
        super().__init__()
        self.__value = ""
        self.__first_item = str(replace_item)
        self.__second_item = str(with_item)

    def set_value(self, value:str):
        self.__value = str(value)
        return self

    def get_value(self) -> str:
        return self.__value.replace(self.__first_item, self.__second_item)


#  Evaluators
# NB: Evaluators evaluate() method always return a boolean value
class EqualsTo(BasicProcessors):
    """This conditional processor is used to evaluate if a value is equals to another or not"""


    def __init__(self, conditional_value) -> None:
        super().__init__()
        self.__conditional_value = conditional_value

    
    def evaluate(self, comparative) -> bool:
        """evaluates the equals to condition"""
        return self.__conditional_value == comparative