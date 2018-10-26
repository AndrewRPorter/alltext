import abc

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def context_interface(self):
        self.strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def algorithm_interface(self):
        return self.text


class TabsToSpaces(Strategy):
    def algorithm_interface(self):
        return ""


class RemoveWhitespace(Strategy):
    def algorithm_interface(self):
        return ""


class Reverse(Strategy):
    def algorithm_interface(self):
        return ""
