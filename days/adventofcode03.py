import re

with open("input03.txt") as f:
    contents = f.readlines()

print("contents size = ", len(contents))
# part 1
total1  =0
for content in contents:    
    result = re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)', content)
    #print("result = ", result)
    #lenResult = len(result)
    #print("lenResult = ", lenResult)
    for item in result:
        total1 = total1 + int(item[0]) * int(item[1])
    
print("total1 = ", total1)

# part 2
total2  =0
do = True
for content in contents:    
    result = re.findall(r'(don\'t\(\))|mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))', content)
    #print("result = ", result)    
    for item in result:
        if item[3]== "do()":
            do = True
        if item[0]== "don't()":
            do = False
        if do == True and item[1] != '' and item[2] != '':
            #print("mul(", item[1],",", item[2],")")
            total2 = total2 + int(item[1]) * int(item[2])
    
print("total2 = ", total2)
    