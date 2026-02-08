


from src.logger import setup_logger
from src.analyzer import LogAnalyzer

setup_logger()

analyzer = LogAnalyzer("data/app.log")
analyzer.load()

stats = analyzer.count_levels()
print("Log stats:", stats)

common_error = analyzer.most_common_error()
print("Most common error:", common_error)
