import sys
from collections import defaultdict

# Converts row and column value to movie theater seat designation
def indToSeat(coord):
    r = chr(ord('A') + coord[0])
    c = str(coord[1] + 1)
    return r + c

# Gets input from file and places it in a 2D array
def parseFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        requests = [['' for _ in range(2)] for _ in range(len(lines))]
        for i, line in enumerate(lines):
            requests[i][0], requests[i][1] = line.split()
    return requests

# Writes output to file given assignment dictionary
def writeToOutput(assignments):
    out = list()
    for key, values in assignments.items():
        seats = ','.join([indToSeat(coord) for coord in values])
        out.append(key + " " + seats)

    with open("output.txt", "w") as f:
        f.writelines("\n".join(out))

# Sets assigned seats and three seat buffer to True
def setSeats(row, i, j):
    length = len(row)
    for k in range(i - 3, j + 3):
        if k >= 0 and k < length:
            row[k] = True
    return row

# Checks and assigns party to seats in a particular row
# Returns a changed theater and assignments variables if successful, None if not
def checkRow(theater, rowNum, request, assignments):
    i = j = 0
    row = theater[rowNum]
    numPeople = int(request[1])
    length, count = len(row), numPeople
    while j < length:
        while i < length and row[i] == True: i += 1 # Sets left side of sliding window
        j = i
        while j < length and count > 0 and row[j] == False: # Attempts to find the requested number of seats
            j += 1
            count -= 1
        if count == 0:
            row = setSeats(row, i, j)
            theater[rowNum] = row
            for ind in range(i, j):
                assignments[request[0]].append((rowNum, ind))
            return (theater, assignments)
        i = j
        count = numPeople
    return None


def assign():
    rows, cols = 20, 10
    numargs = len(sys.argv) - 1
    if numargs != 1:
        raise Exception('Error: {} arguments detected. Please enter 1 argument\n'.format(numargs))
    requests = parseFile(sys.argv[1])
    theater = [[False for _ in range(cols)] for _ in range(rows)]

    # Order in which the rows are checked for seats
    priority = [12, 10, 14, 8, 16, 6, 18, 4, 2, 0] # Starts at 2/3 away from screen, goes to 1/2, and then alternates above and below
    assignments = defaultdict(list)
    for request in requests:
        assigned = False
        for p in priority:
            assignment = checkRow(theater, p, request, assignments)
            if assignment is not None:
                theater, assignments = assignment
                assigned = True
                break
        
        if not assigned:
            raise Exception("Error: Could not accomodate all requests\n")
    
    writeToOutput(assignments)

def main():
    assign()
    

if __name__ == "__main__":
    main()