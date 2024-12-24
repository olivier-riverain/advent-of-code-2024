
#with open("input07_example.txt") as f:
with open("input07.txt") as f:
    contents = f.readlines()

nbLines = len(contents)

print("nb lines = ", nbLines)


# part 1
print("part 1")
calibration = []

def computeOperationRec(value, resultat, numbers, n):
    #print("ici value = ", value, " resultat = ", resultat, " n = ",n)
    if n+1==len(numbers):
        return resultat == value
   
    if computeOperationRec(value, resultat * numbers[n+1], numbers, n+1):
        return True 
    if computeOperationRec(value, resultat + numbers[n+1], numbers, n+1):
        return True
    
    return False 
    

for content in contents:
    value, right = content.split(":")
    #print("value = ", value)
    value = int(value)
    rightSplit = right.split(" ")
    numbers = []
    for i in range(1,len(rightSplit)):
        numbers.append(int(rightSplit[i]))
    n = len(numbers)-1    
    resultat = computeOperationRec(value, numbers[0], numbers, 0)
    #print("resultat = ", resultat)
    if resultat:
        calibration.append(value)    

print("calibration = ", calibration)
print("len(calibration) = ", len(calibration))
total1 = sum(calibration)
print("total 1 = ", total1)

# part 2
print("part 2")
calibration = []

def computeOperationRec2(value, resultat, numbers, n):
    #print("ici value = ", value, " resultat = ", resultat, " n = ",n)
    if n+1==len(numbers):
        return resultat == value
   
    if computeOperationRec2(value, resultat * numbers[n+1], numbers, n+1):
        return True 
    if computeOperationRec2(value, resultat + numbers[n+1], numbers, n+1):
        return True
    
    varAux = int(str(resultat) + str(numbers[n+1]))
    if computeOperationRec2(value, varAux, numbers, n+1):
        return True 
    
    return False 
    

for content in contents:
    value, right = content.split(":")
    #print("value = ", value)
    value = int(value)
    rightSplit = right.split(" ")
    numbers = []
    for i in range(1,len(rightSplit)):
        numbers.append(int(rightSplit[i]))
    n = len(numbers)-1    
    resultat = computeOperationRec2(value, numbers[0], numbers, 0)
    #print("resultat = ", resultat)
    if resultat:
        calibration.append(value)    

print("calibration = ", calibration)
print("len(calibration) = ", len(calibration))
total1 = sum(calibration)
print("total 2 = ", total1)

