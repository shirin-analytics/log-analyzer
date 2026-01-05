from src.reader import LogReader

reader = LogReader("../data/app.log")
reader.load()

print(reader.lines)
