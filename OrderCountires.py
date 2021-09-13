file=open('input.txt', 'r')
lines = file.readlines()
cleanList = []
for element in lines:
    cleanList.append(element.strip())

currentCountry = "Norway"
lastChar = currentCountry[-1]
print("Starting country: " + currentCountry)

visited = []

i = 0
while i < 12:
        res = [idx for idx in cleanList if idx[0].lower() == lastChar.lower()]
        #print("The list of matching first letter : " + str(res))
        foundNew = False
        foo = 0
        while (foundNew == False):
            if res[foo] not in visited:
                foundNew = True
                currentCountry = res[foo]
            foo += 1
        
        visited.append(currentCountry)
        print(currentCountry)
        lastChar = currentCountry[-1]
        i += 1

print(str(visited))
