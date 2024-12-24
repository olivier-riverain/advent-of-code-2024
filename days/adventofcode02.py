with open("input02.txt") as f:
    contents = f.readlines()

print("contents size = ", len(contents))


def isSafe(item):     
    if item[0]-item[1] < 0:
        increase = True
    elif item[0]-item[1] > 0:
        increase = False
    else:               
        return False
    safe = True
    for i in range(1,len(item)):
        diff = item[i]-item[i-1]
        if increase and diff <=0:
            safe = False
            break
        if not increase and diff >=0:
            safe = False
            break
        if abs(diff) <1 or abs(diff) >3:
            safe = False
            break
    return safe
    

totalSafe = 0

for content in contents:    
    item = content.split(" ")
    listItems = []
    for c in item:
        listItems.append(int(c))
    if isSafe(listItems):
        totalSafe = totalSafe + 1
    else: # part 2       
        for i in range(len(listItems)):
            listItemsTemp = []            
            for c in listItems:                
                listItemsTemp.append(c)
            listItemsTemp.pop(i)            
            if isSafe(listItemsTemp):
                totalSafe = totalSafe + 1
                break
     
print("totalSafe = ", totalSafe)

