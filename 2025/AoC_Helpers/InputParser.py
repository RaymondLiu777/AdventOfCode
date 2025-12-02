import re

# Usage:
# 1. InputParser(data) -> Probably open(filename).read()
# 2. readLines or readSections to parse out lines
# 3. Apply options to lines
#    a. split/format to parse lines into strings, 
#    b. regex/findNumbers to search for things
#    c. applyToLines to apply lambda directly to lines
# 4. cast to convert all items in a line into appropriate datatypes/any other lambda functions
#    a. You can provide multiple lambda functions and take turns applying them from the start of each line
# 5. getData to retrieve result

# Ex: to get data in the form: 1-3 with value 7 
# InputParser(open(filename).read()).readLines().format("-", "with value").cast(int).getData()

# Intermitten data can be retrieved directly and placed into another input parser, be careful of flags
class InputParser:
    def __init__(self, data):
        self.data = data.strip() if type(data) == str else data
        self.sections = False
        self.section_headers = False

    # Read as lines or sections (with headers)
    def readLines(self):
        self.data = self.data.split("\n")
        return self

    def readSections(self, withHeaders=False):
        self.data = self.data.split("\n\n")
        self.sections = True
        self.section_headers = withHeaders
        new_data = {} if withHeaders else []
        for section in self.data:
            lines = section.split("\n")
            if(withHeaders):
                new_data[lines[0]] = lines[1:]
            else:
                new_data.append(lines)
        self.data = new_data
        return self
    
    def readGrid(self):
        self.data = self.data.split("\n")
        new_data = []
        for line in self.data:
            new_data.append(list(line)) 
        self.data = new_data
        return self

    # Split line data (either by spliting on whitespace, based on a formatting)
    def split(self, delim=None):
        if(delim == None):
            self.applyToLines(lambda line: line.split())
        else:
            self.applyToLines(lambda line: line.split(delim))
        return self

    def __parseLine(string, *argv):
        string = string.strip()
        result = []
        start = 0
        for split in argv:
            location = string.find(split, start)
            if(location != start):
                result.append(string[start:location])
            start = location + len(split)
        if(start != len(string)):
            result.append(string[start:])
        return result

    def format(self, *argv):
        self.applyToLines(lambda line: InputParser.__parseLine(line, *argv))
        return self
    
    def regex(self, regExp):
        self.applyToLines(lambda line: re.search(regExp, line).groups())
        return self
    
    def findNumbers(self):
        self.applyToLines(lambda line: tuple(map(int, re.findall(r"-?\d+", line))))
        return self

    def applyToLines(self, func):
        if(self.sections):
            if(self.section_headers):
                new_data = {}
                print(self.data)
                for key, lines in self.data.items():
                    new_data[key] = []
                    for line in lines:
                        new_data[key].append(func(line))
                self.data = new_data
            else:
                new_data = []
                for section in self.data:
                    new_section = []
                    for line in section:
                        new_section.append(func(line))
                    new_data.append(new_section)
                self.data = new_data
        else:
            new_data = []
            for line in self.data:
                new_data.append(func(line))
            self.data = new_data
        return self

    # Apply operations to individual parts in a line
    def __modifyData(line, *argv):
        new_data = []
        for idx, val in enumerate(line):
            new_data.append(argv[idx%len(argv)](val))
        return new_data

    def cast(self, *argv):
        self.applyToLines(lambda line: InputParser.__modifyData(line, *argv))
        return self

    def getData(self):
        return self.data
