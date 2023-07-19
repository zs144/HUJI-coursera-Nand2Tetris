import os

class Parser:
    def __init__(self, filename) -> None:
        path = os.path.dirname(__file__)
        filename = os.path.join(path, filename)
        self.f
        f = open(filename, 'r')