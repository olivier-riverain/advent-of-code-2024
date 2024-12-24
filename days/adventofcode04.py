import re

#with open("input04_example.txt") as f:
with open("input04.txt") as f:
    contents = f.readlines()

print("contents size = ", len(contents))
# part 1

# on travaille sur les lignes
def matchPattern(contents):
    total  =0
    for content in contents:    
        result = re.findall(r'XMAS', content)        
        total += len(result)
        result = re.findall(r'SAMX', content)
        total += len(result)
    return total
total = matchPattern(contents)
print("après lignes")
print("total = ", total)


# on travaille sur les colonnes
def convertTranspose(contents):
    newContents = []
    for i in range(lengthLine):
        newContents.append('')
    for content in contents:        
        for i in range(lengthLine):
            newContents[i] +=  content[i]
    return newContents


lengthLine = len(contents[0])-1
print("lengthLine = ", lengthLine)

contentsTranspose = convertTranspose(contents)
total += matchPattern(contentsTranspose)
print("après colonnes")
print("total = ", total)

# on travaille sur les diagonales \
def convertToDiagonaleD(contents, contentsTranspose):
    newContents = []
    for i in range(lengthLine*2-1):
        newContents.append('')
    # pour les diagonales supérieures
    k=0 # gere le decalage pour avoir la diagonale
    for i in range(lengthLine): #chaque ligne        
        for j in range(lengthLine): # chaque colonne
            if (i+j) < lengthLine:
                newContents[j] += contents[i] [j+k]                
        k += 1
    # pour les diagonales inférieures    
    k=0 # gere le decalage pour avoir la diagonale
    for i in range(lengthLine): #chaque ligne        
        for j in range(lengthLine): # chaque colonne
            if (i+j+1) < lengthLine:
                newContents[j+lengthLine] += contentsTranspose[i] [j+1+k]                
        k += 1

    return newContents

newContents = convertToDiagonaleD(contents, contentsTranspose)
print("après diagonales \\")
total += matchPattern(newContents)
print("total = ", total)

# on travaille sur les diagonales /
def rotation(contents):
    newContents = []
    for i in range(lengthLine):
        newContents.append('')   
    
    for i in range(lengthLine): #chaque ligne       
        for j in range(lengthLine): # chaque colonne            
            newContents[j] += contents[lengthLine-1-i] [j]           

    return newContents

contentsRotation = rotation(contents)
contentsRotationTranspose = convertTranspose(contentsRotation)
newContents = convertToDiagonaleD(contentsRotation, contentsRotationTranspose)
print("après diagonales /")
total += matchPattern(newContents)
print("total part 1 = ", total)

# part 2
total2  =0
def findCross(contents):
    total =0    
    for i in range(lengthLine):
        for j in range(lengthLine):
            if contents[i] [j] == 'A': # cherche le centre de la croix               
                ok1 = False
                ok2 = False
                if i-1 >= 0 and j-1 >= 0 and i+1 < lengthLine and j+1 < lengthLine:
                    if contents[i-1] [j-1] == 'M' and contents[i+1] [j+1] == 'S':
                        ok1 = True
                    if contents[i-1] [j-1] == 'S' and contents[i+1] [j+1] == 'M':
                        ok1 = True
                    if contents[i+1] [j-1] == 'M' and contents[i-1] [j+1] == 'S':
                        ok2 = True
                    if contents[i+1] [j-1] == 'S' and contents[i-1] [j+1] == 'M':
                        ok2 = True
                    if ok1 and ok2:
                        total +=1               
    
    return total

print("part 2 cross")
total2 = findCross(contents)   
print("total2 = ", total2)
    