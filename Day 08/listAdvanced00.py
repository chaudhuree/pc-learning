# nested list
nList = [
    ['sohan', 'chaudhuree'],
    ['kazi', 'sabrina'],
    ['sadia', 'shimla'],
]
# access nested lists
print(nList[0][0])
print(nList[1][1])

# iterate nested lists

for i in nList:
    for j in i:
        print(j)

for i in nList:
    print(i[0])
