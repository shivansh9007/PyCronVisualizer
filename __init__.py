import sys
from sys import argv
from file_parser.json_file_parser import JsonFileParser


def main():

    _, file_path = sys.argv

    # TODO: Write logic to implement smart file parser-selector.
    # GTHF (Good to Have Feature)
    fileParser = JsonFileParser(file_path)
    fileParser.parse()

    


if __name__ == "__main__":
    main()
