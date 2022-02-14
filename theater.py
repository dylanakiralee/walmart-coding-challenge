import sys

def parseFile(filename):
    print(filename)
    with open(filename, 'r') as f:
        lines = f.readlines()
        requests = [['' for _ in range(2)] for _ in range(len(lines))]
        for i, line in enumerate(lines):
            requests[i][0], requests[i][1] = line.split()
    return requests

def writeToOutput(assignments):
    pass

def assign():
    rows, cols = 20, 10
    numargs = len(sys.argv) - 1
    if numargs != 1:
        raise Exception('Error: {} arguments detected. Please enter 1 argument\n'.format(numargs))
    
    requests = parseFile(sys.argv[1])
    
    theater = [[False for _ in range(cols)] for _ in range(rows)]

    preferredRow = rows * 2 // 3 - 1
    for request in requests:
        numPeople = request[1]


def main():
    assign()

if __name__ == "__main__":
    main()