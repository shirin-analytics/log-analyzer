import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")

    parser.add_argument("--path", required=True, help="Path to log file")
    parser.add_argument("--from", dest="date_from", help="Start date YYYY-MM-DD")
    parser.add_argument("--to", dest="date_to", help="End date YYYY-MM-DD")
    parser.add_argument("--out", help="Output CSV file")

    return parser.parse_args()
