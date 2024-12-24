
#with open("input05_exemple.txt") as f:
with open("input05.txt") as f:
    contents = f.readlines()

print("contents size = ", len(contents))
orders = []
updates = []

for content in contents:
    if content.find("|") != -1:
        splitOrder = content.split("|")
        orders.append([splitOrder[0], splitOrder[1][:-1]])
    if content.find(",") != -1:
        content = content.strip("\n")
        splitUpdate = content.split(",")               
        updates.append(splitUpdate)

print("orders length = ", len(orders))
print("updates length = ", len(updates))

# part 1
print("part 1")
def createDictonary(orders):
    dictionary = {}
    for order in orders:
        if order[0] in dictionary.keys():
            dictionary[order[0]].append(order[1])
        else:
            dictionary[order[0]] = [order[1]]
    
    return dictionary

def isUpdateCorrect(update, dictionaryOrders):    
    for i in range(len(update)):
        if  i!=len(update)-1:
            if update[i] in  dictionaryOrders.keys():
                for j in range(i+1,len(update)):
                    if update[j] not in dictionaryOrders[update[i]]:
                        return False
            else:
                return False
    return True

dictionaryOrders = createDictonary(orders)

middles = []
for update in updates:
    if isUpdateCorrect(update, dictionaryOrders):
        middles.append(update[len(update)//2])
total1 = 0
for middle in middles:
    total1 += int(middle)
print("size of middle = ", len(middles))
print("total1 = ", total1)

#part 2
print("part 2")
def createNewUpdate(dictionaryUpdate):
    newUpdate = []
    sortedDictionary = dict(sorted(dictionaryUpdate.items(), key=lambda item: item[1], reverse=True))
    for key in sortedDictionary.keys():
        newUpdate.append(key)    
    return newUpdate

def correctUpdate(update, dictionaryOrders):
    newUpdate = []    
    dictionaryUpdate = {}
    for item in update:
        dictionaryUpdate[item] = 0
    
    for i in range(len(update)):            
        if update[i] in  dictionaryOrders.keys():
                for j in range(len(update)):
                    if update[j]  in dictionaryOrders[update[i]]:
                        dictionaryUpdate[update[i]] += 1                           
        else:
            dictionaryUpdate[update[i]] = 0
    newUpdate = createNewUpdate(dictionaryUpdate)
    return newUpdate

middlesCorrected = []
for update in updates:
    if not isUpdateCorrect(update, dictionaryOrders):
        newUpdate = correctUpdate(update, dictionaryOrders)        
        middlesCorrected.append(newUpdate[len(newUpdate)//2])

total2 = 0
for middle in middlesCorrected:
    total2 += int(middle)
print("size of middle = ", len(middlesCorrected))
print("total2 = ", total2)