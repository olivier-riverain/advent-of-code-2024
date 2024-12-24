#with open("input10_example.txt") as f:
with open("input10.txt") as f:
    contents = f.readlines()

nbLines = len(contents)
print("nb lines = ", nbLines)
sizeLine = len(contents[0])-1
print("sizeLine = ", sizeLine)
#print("contents = ", contents)