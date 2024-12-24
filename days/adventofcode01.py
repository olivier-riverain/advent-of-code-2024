with open("input01.txt") as f:
    contents = f.readlines()

print("contents size", len(contents))
left =[]
right= []
for content in contents:
    content = content.strip("\n")
    item = content.split("   ")
    print("item = ", item)
    left.append(item[0])
    right.append(item[1])
# part 01
left.sort()
right.sort()
print("left[0]", left[0])
print("right[0]", right[0])
total1 =0
for i in range(len(left)):
    total1 = total1 + abs(int(left[i])- int(right[i]))
print("total 1 = ", total1)

# part 02
print("left[0]", left[0])
print("right[0]", right[0])
dictionary = {}
total2 =0
for item in right:
    if item in dictionary.keys():
        dictionary[item] = dictionary[item] +1
    else:
        dictionary[item] = 1

print(dictionary)

for item in left:
    if item in dictionary.keys():
        total2 = total2 + int(item) * dictionary[item]    
   
print("total 2 = ", total2)

