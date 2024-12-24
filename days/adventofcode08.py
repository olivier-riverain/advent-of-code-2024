#with open("input08_example_mini2.txt") as f:
#with open("input08_example_mini.txt") as f:
#with open("input08_example.txt") as f:
with open("input08.txt") as f:
    contents = f.readlines()

nbLines = len(contents)
print("nb lines = ", nbLines)
sizeLine = len(contents[0])-1
print("sizeLine = ", sizeLine)
#print("contents = ", contents)

# part 1
print("part 1")

def retrieveAntennas(contents):
    dictionaryAnten = {}
    for line in range(nbLines):
        for col in range(sizeLine):
            if contents[line][col] != ".":
                if contents[line][col] in dictionaryAnten.keys():
                    dictionaryAnten[contents[line][col]].append([line, col])
                else:
                    list = []
                    list.append([line, col])
                    dictionaryAnten[contents[line][col]] = list

    return dictionaryAnten

def computeDistance(m,n):
    return abs(m[0]-n[0]) + abs(m[1]-n[1])

def computeVector(m,n):
    return [m[0]-n[0], m[1]-n[1]]

def createAntinode(antenna, vector):
    antiNode = []
    nodeX = antenna[0]+vector[0]
    nodeY = antenna[1]+vector[1]
    if nodeX >= 0 and nodeX < sizeLine and nodeY >= 0 and nodeY < nbLines:
        antiNode.append(nodeY)
        antiNode.append(nodeX)
    return antiNode

dictionaryAntenn = retrieveAntennas(contents)
#print("dictionaryAntenn = ", dictionaryAntenn)
antiNodes = []

for modelOfAntenna in dictionaryAntenn.keys():    
    for antenna1 in dictionaryAntenn[modelOfAntenna]:        
        for antenna2 in dictionaryAntenn[modelOfAntenna]:
            if antenna1[0] != antenna2[0] and antenna1[1] != antenna2[1]:                
                vector = computeVector(antenna1, antenna2)                
                antiNode = createAntinode(antenna1, vector)
                if len(antiNode) !=0:                   
                    if antiNode not in antiNodes:
                        antiNodes.append(antiNode)

#print("antiNodes = ", antiNodes)
print("total 1  = ",len(antiNodes))

# part 2
print("part2")

def createAntinode2(antenna, vector):
    antiNode = []
    antiNode.append([antenna[1], antenna[0]])
    k = 1
    nodeX = antenna[0]+ k *vector[0]
    nodeY = antenna[1]+ k * vector[1]
    
    while nodeX >= 0 and nodeX < sizeLine and nodeY >= 0 and nodeY < nbLines:    
        antiNode.append([nodeY, nodeX])
        k += 1
        nodeX = antenna[0]+ k * vector[0]
        nodeY = antenna[1]+ k * vector[1]

    return antiNode

antiNodes = []

for modelOfAntenna in dictionaryAntenn.keys():    
    for antenna1 in dictionaryAntenn[modelOfAntenna]:        
        for antenna2 in dictionaryAntenn[modelOfAntenna]:
            if antenna1[0] != antenna2[0] and antenna1[1] != antenna2[1]:                
                vector = computeVector(antenna1, antenna2)                
                antiNode = createAntinode2(antenna1, vector)
                if len(antiNode) !=0:                    
                    for node in antiNode:
                        if node not in antiNodes:
                            antiNodes.append(node)

#print("antiNodes = ", antiNodes)
print("total 2  = ",len(antiNodes))