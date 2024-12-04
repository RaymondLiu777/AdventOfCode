class Directions:

    U = (0, 1)
    D = (0, -1)
    L = (-1, 0)
    R = (1, 0)
    UR = (1, 1)
    UL = (-1, 1)
    DR = (1, -1)
    DL = (-1, -1) 

    # Useful constants
    CARDINAL = {
        "U": U, "D": D, "L": L, "R": R
    }

    DIAGONAL = { 
        "UR": UR, "UL": UL, "DR": DR, "DL": DL 
    }

    ALL = { **CARDINAL, **DIAGONAL }


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
    
    def Get(self, location, *argv):
        new_location = TupleOps.Add(location, *argv)
        if not InGrid(new_location):
            print("Error invalid location", location, argv)
            raise Exception("Error invalid location")
        return self.grid[new_location[0]][new_location[1]]

    def InGrid(self, location):
        return location[0] >= 0 and location[1] >= 0 and location[0] < len(self.grid) and location[1] < len(self.grid[location[0]])

class TupleOps:
    def Add(tup1, *argv):
        value = tup1
        for arg in argv:
            value = tuple(map(lambda i, j: i + j, value, arg))
        return value

    def Multiply(tup1, multiple):
        return tuple(map(lambda i: i * multiple, tup1))

# Usage:
# 1. InputParser(data) -> Probably open(filename).read()
# 2. readLines or readSections to parse out lines
# 3. split or format to parse lines into strings
# 4. modifyData to convert strings into appropriate datatypes
# 5. getData to retrieve result
# Intermitten data can be retrieved directly and placed into another input parser, be careful of flags
class InputParser:
    def __init__(self, data):
        self.data = data
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

    # Apply operations to individual parts in a line
    def __modifyData(line, *argv):
        new_data = []
        for idx, val in enumerate(line):
            new_data.append(argv[idx%len(argv)](val))
        return new_data

    def modifyData(self, *argv):
        self.applyToLines(lambda line: InputParser.__modifyData(line, *argv))
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

    def getData(self):
        return self.data


