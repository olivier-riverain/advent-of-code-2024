#with open("input09_example.txt") as f:
with open("input09.txt") as f:
    contents = f.readlines()

nbLines = len(contents)
print("nb lines = ", nbLines)
sizeLine = len(contents[0])-1
print("sizeLine = ", sizeLine)
#print("contents = ", contents)

# part 1
print("part 1")

def convertToBlocks(contents):
    blocks = []
    id = 0
    k = 0
    char = "."
    for i in range(sizeLine):        
        char = "."
        if k%2 == 0:
            char = str(id)
            id += 1
        for j in range(int(contents[0][i])):
            blocks.append(char)
        k += 1
    return blocks

def deFrag(block):
    posLeft = 0
    posRight = len(block)-1    
    while block[posRight] == ".":
        posRight -= 1    
    while posLeft < posRight:
        if block[posLeft] == ".":
            while block[posRight] == ".":
                posRight -= 1
            block[posLeft] = block[posRight]
            block[posRight] = "."            
            posRight -= 1
        posLeft += 1    
    return block

block = convertToBlocks(contents)
print("block = ", block)
print("block size = ", len(block))
newBlock = deFrag(block)
#print("newBlock = ", newBlock)
total1 = 0
id =0
for bloc in newBlock:
    if bloc != ".":
        total1 += id * int(bloc)
        id +=1

print("total 1 = ", total1)

# part 2
print("part 2")

def findFreePos(block, sizeFile, posRight):
    posLeft = 0
    sizeDispo = 0       
    while posLeft < posRight and sizeDispo < sizeFile:        
        while posLeft < len(block) and block[posLeft] != ".":
            posLeft += 1        
        posLeftTemp = posLeft
        sizeDispo = 0
        while posLeftTemp < len(block) and block[posLeftTemp] == ".":
            sizeDispo += 1
            posLeftTemp += 1        
        if  sizeDispo < sizeFile:
            posLeft += sizeDispo
    if posLeft >= posRight: # teste si l'espace disponible est après le fichier
        posLeft =  -1    
    return posLeft

def writeFile(block, posLeft, sizeFile, idFile):
    for i in range(posLeft, posLeft+sizeFile):
        block[i] = idFile

def eraseFile(block, sizeFile, posRight):
    for i in range(posRight-sizeFile+1, posRight+1):
        block[i] = "."

def maxKey(dict):
    for key in dict.keys():
        max = -1
        if int(key) > max:
            max = int(key)
    return max

def findPosRight(idFile, block):
    posRight = -1
    sizeBlock = len(block)
    for i in range(len(block)):
        if block[sizeBlock-1-i] == str(idFile):
            posRight = sizeBlock-1-i
            return posRight
    return posRight

def deFrag(block, dicoSize):    
    lastId = maxKey(dicoSize)    
    print("lastId = ", lastId)    
    for id in range(lastId+1):
        idFile = lastId - id        
        posRight = findPosRight(idFile, block)              
        sizeFile = dicoSize[str(idFile)]
        posLeft = findFreePos(block, sizeFile, posRight)       
        if posLeft != -1:
            writeFile(block, posLeft, sizeFile, idFile)
            eraseFile(block, sizeFile, posRight)            
    return block


def createDico(block):
    dico = {}
    for item in block:
        if item != ".":
            if item in dico.keys():
                dico[item] +=1
            else:
                dico[item] = 1    
    return dico

block = convertToBlocks(contents)
#print("block = ", block)
dicoSize = createDico(block)
#print("dicoSize = ", dicoSize)

newBlock = deFrag(block, dicoSize)
#print("newBlock = ", newBlock)

total2 = 0

for i in range(len(newBlock)):
    val = 0
    if newBlock[i] != ".":
        val = int(newBlock[i])
    total2 += i * val    

print("total 2 = ", total2)
