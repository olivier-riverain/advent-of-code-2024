
#with open("input06_example.txt") as f:
with open("input06.txt") as f:
    contents = f.readlines()

ySize = len(contents)
xSize = len(contents[0])-1
print("y size = ", ySize)
print("x size = ", xSize)

# part 1
print("part 1")

def findGuardian(contents):
    position = []
    position.append(0)
    position.append(0)
    for i in range(len(contents)):
        if "^" in contents[i]:
            #print("gardian found")
            position[0] = contents[i].index("^")
            position[1] = i
            break

    return position

def canMove(position, map, deplacement):    
    return not map[position[1]+ deplacement[1]] [position[0]+ deplacement[0]] == "#"
    

positions = []
deplacements = [[0,-1], [1,0], [0,1], [-1,0]] # haut ^, droite >, bas v, gauche <
indiceDeplacement =0
deplacement = deplacements[indiceDeplacement]
position = findGuardian(contents)
print("x = ", position[0], " y = ", position[1])
print("deplacement = ", deplacement)
positions.append([position[0], position[1]])
print("positions 1 = ", positions)

while position[0] + deplacement[0] >= 0 and position[0] + deplacement[0] < xSize and position[1] + deplacement[1] >= 0 and position[1] + deplacement[1] < ySize:
    if canMove(position, contents, deplacement):
        position[0] += deplacement[0]
        position[1] += deplacement[1]
        if position not in positions:        
            positions.append([position[0], position[1]])        
    else:
        indiceDeplacement = (indiceDeplacement + 1)%len(deplacements)
        deplacement = deplacements[indiceDeplacement]

print("guardian exit at position = ", position)
print("total 1 = ", len(positions))

# part 2
print("part 2")
def initializeNewContents(contents, newObstacle):
    newContents = []    
    for y in range(ySize):        
        line = ""
        for x in range(xSize):
            if y == newObstacle[1] and x == newObstacle[0]:
                line += "#"
            else:
                line += contents[y][x]
        newContents.append(line)
    return newContents    


obstructions = []

for i in range(1,len(positions)):
    newObstacle = positions[i]    
    newContents = initializeNewContents(contents, newObstacle)    
    position = findGuardian(contents)    
    indiceDeplacement =0
    deplacement = deplacements[indiceDeplacement]        
    visited = []
    visited.append([position[0], position[1], deplacement])     
    loop = False
    while not loop and position[0] + deplacement[0] >= 0 and position[0] + deplacement[0] < xSize and position[1] + deplacement[1] >= 0 and position[1] + deplacement[1] < ySize:
        if canMove(position, newContents, deplacement):
            position[0] += deplacement[0]
            position[1] += deplacement[1]
            if [position[0], position[1], deplacement] in visited:
                obstructions.append([newObstacle[0], newObstacle[1]])                
                loop = True       
            visited.append([position[0], position[1], deplacement])              
        else:        
            indiceDeplacement = (indiceDeplacement + 1)%len(deplacements)
            deplacement = deplacements[indiceDeplacement]        




print("obstructions = ",obstructions)

print("total 2 = ", len(obstructions))