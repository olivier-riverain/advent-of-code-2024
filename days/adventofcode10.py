#with open("input10_example_mini02.txt") as f:
#with open("input10_example_mini01.txt") as f:
#with open("input10_example.txt") as f:
with open("input10.txt") as f:
    contents = f.readlines()

nbLines = len(contents)
print("nb lines = ", nbLines)
sizeLine = len(contents[0])-1
print("sizeLine = ", sizeLine)
print("contents = ", contents)

# part 1
print("part 1")

def findPosStart(contents):
    listStart = []
    for y in range(nbLines):
        for x in range(sizeLine):
            if contents[y][x] == "0":
                listStart.append([y, x])
    return listStart

def findNeighbors(start, contents):
    listNeighbors = []
    next = int(contents[start[0]][start[1]]) + 1    
    if start[0]-1 >= 0: 
        n1 = [start[0]-1, start[1]]
        if contents[n1[0]][n1[1]] ==  str(next):
            listNeighbors.append(n1)
    if start[0]+1 < sizeLine:
        n2 = [start[0]+1, start[1]]
        if contents[n2[0]][n2[1]] ==  str(next):
            listNeighbors.append(n2)
    if start[1]-1 >= 0:
        n3 = [start[0], start[1]-1]
        if contents[n3[0]][n3[1]] ==  str(next):
            listNeighbors.append(n3)
    if start[1]+1 < nbLines:
        n4 = [start[0], start[1]+1]
        if contents[n4[0]][n4[1]] ==  str(next):
            listNeighbors.append(n4)
    return listNeighbors


def findPathRec(previous, step, contents, visited):    
    if step == 9:
        if previous not in visited:
            visited.append([previous[0], previous[1]])
        return 1
    listNeighbors = findNeighbors(previous, contents)
    nbNeighbors = len(listNeighbors)
    if nbNeighbors == 0:
        return 0
    total_path = 0
    for i in range(nbNeighbors):
        total_path += findPathRec(listNeighbors[i], step+1, contents, visited)
    return total_path

listStart = findPosStart(contents)
nbStart = len(listStart)
print("nbStart = ", nbStart)
print("listStart = ", listStart)

total2 =0
score = 0
for start in listStart:
    #print("start = ", start)   
    step = 0
    visited = []
    total = findPathRec(start, step, contents, visited)
    #print("visited = ", visited)
    #print("total = ", total)
    total2 += total
    score += len(visited)


print("total 1 = ", score)

# part 2
print("part 2")

print("total 2 = ", total2)