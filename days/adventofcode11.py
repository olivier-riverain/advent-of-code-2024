import time

#with open("input11_example_mini.txt") as f:
#with open("input11_example.txt") as f:
with open("input11.txt") as f:
    contents = f.readlines()

nbLines = len(contents)
print("nb lines = ", nbLines)
sizeLine = len(contents[0])-1
print("sizeLine = ", sizeLine)
print("contents = ", contents)

listStones = contents[0].strip("\n")
print("listStones = ", listStones)
listStones = listStones.split(" ")
print("listStones = ", listStones)

# part 1
print("part 1")

def isEvenDigit(stone):
    nb = 0   
    nb = len(stone)    
    return nb%2 == 0

def splitStone(stone):    
    length = len(stone)
    stone1 = stone[0: length//2]
    stone1 = str(int(stone1))
    stone2 = stone[length//2 :]
    stone2 = str(int(stone2))
    return stone1, stone2

def applyRules(listStones):
    newList = []
    for stone in listStones:
        if stone == "0":
            newList.append("1")
        elif isEvenDigit(stone):
            stone1,stone2 = splitStone(stone)
            newList.append(stone1)
            newList.append(stone2)
        else:
            newStone = int(stone) * 2024
            newStone = str(newStone)
            newList.append(newStone)
    return newList    

newList =listStones
startTime = time.time()

for i in range(25):
    newList = applyRules(newList)    
    
endTime = time.time()
print("time = ",(endTime-startTime)*10000, " ms")


print("total1 = ", len(newList))

# part 2
print("part 2")
print(" length listStones = ", len(listStones))

def createNbStone(listStones):
    list = []
    for i in range(len(listStones)):
        list.append([listStones[i], 1])
    return list

def listToDict(list):    
    dict = {}
    for l in list:
        if l[0] in dict.keys():
            dict[l[0]] += l[1]
        else:
            dict[l[0]] = l[1]
    return dict

def dictToList(dict):
    list = []
    for key in dict.keys():
        list.append([key, dict[key]])
    return list 

def applyRules2(listStones):
    newList = []
    for stone in listStones:
        if stone[0] == "0":
            newList.append(["1", stone[1]])
        elif isEvenDigit(stone[0]):            
            stone1,stone2 = splitStone(stone[0])
            newList.append([stone1, stone[1]])
            newList.append([stone2, stone[1]])
        else:
            newStone = int(stone[0]) * 2024
            newStone = str(newStone)
            newList.append([newStone,stone[1]])
    return newList    

def countStones(list):
    count = 0
    for stone in list:
        count += stone[1]
    return count

startTime = time.time()
newList = createNbStone(listStones)
print("newList = ", newList)
for i in range(75):
    newList = applyRules2(newList)    
    dict = listToDict(newList)    
    newList = dictToList(dict)   

endTime = time.time()
print("time rec = ",(endTime-startTime)*10000, " ms")
total2 = countStones(newList)
print("total2 = ", total2)

