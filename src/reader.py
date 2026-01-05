class LogReader:
    def __init__(self, path: str):
        self.path = path
        self.lines = []

    def load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            self.lines = file.readlines()
