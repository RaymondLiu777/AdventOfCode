from html.parser import HTMLParser
import re
import sys

STATES = ["Start", "Found PreText (for example)", "Found Code Tag", "Got Sample"]
regex = "for example"

class AoCParser(HTMLParser):
    def __init__(self):
        super().__init__()
        
        self.state = STATES[0]
        self.sample = ""

    def handle_starttag(self, tag, attrs):            
        if self.state == STATES[1] and tag == "code":
            self.state = STATES[2]

    def handle_data(self, data):
        if self.state == STATES[0] and re.search(regex, data, re.IGNORECASE) is not None:
            self.state = STATES[1]

        if self.state == STATES[2]:
            self.sample = data
            self.state = STATES[3]


filename = sys.argv[1] if len(sys.argv) > 1 else "website_data.txt"
with open(filename, 'r') as file:
    webpage = file.read()
    parser = AoCParser()
    parser.feed(webpage)
    print(parser.sample, end="")