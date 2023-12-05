import sys
import pyperclip

def part1(file):
    
    pass



def part2(file):
    
    pass



if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("Error, requires two command lines arguments: s/i 1/2")
        exit()
    if (sys.argv[1] != 's' and sys.argv[1] != 'i') or (sys.argv[2] != '1' and sys.argv[2] != '2'):
        print("Error invalid command line args:", sys.argv[1], sys.argv[2])
        exit()

    filename = ""
    if sys.argv[1] == 's':
        filename = "sample.txt"
    elif sys.argv[1] == 'i':
        filename = "input.txt"

    result = ""
    if sys.argv[2] == '1':
        result = part1(filename)
    elif sys.argv[2] == '2':
        result = part2(filename)
    print(result)
    pyperclip.copy(result)
    