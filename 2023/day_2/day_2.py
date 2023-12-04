


# %%



with open("input.txt") as f:
        lines = f.readlines()
# %%
import re

def fixNone(a):
        if(a is None):
                return ['0']
        else:
                return a

def searchColor(stringa, color):
        res = fixNone(re.search(" \d+ " + color, stringa))[0]
        res = fixNone(re.search("\d+", res))[0]
        return int(res)

sumz = 0
allGroups = []
for line in lines:
        firstSep = line.split(":")
        id = int(re.findall("\d+", firstSep[0])[0])
        secondSep = firstSep[1].split(";")
        # redList = []
        # greenList = []
        # blueList = []
        groupsRes = []
        allChecked = True
        print(line)
        for group in secondSep:

                redNum = searchColor(group, "red")
                # redList.append(redNum)
                greenNum = searchColor(group, "green")
                # greenList.append(greenNum)
                blueNum = searchColor(group, "blue")
                # blueList.append(blueNum)
                groupsRes.append([redNum, greenNum, blueNum])

                print(([redNum, greenNum, blueNum]))

                allChecked = allChecked and ( redNum <= 12 and  greenNum <= 13 and blueNum <= 14)

        allGroups.append(groupsRes)
        if(allChecked == True):
                sumz += id
        # print(groupsRes)
        # print("\n")
        # checkRes = lambda x, Ns : all(i < Ns[idx] for idx, i in enumerate(x))
        # if(checkRes(redList, 12) and checkRes(greenList, 13) and checkRes(blueList, 14)):
        #         sumz += id




print(sumz)
# %%

setPower = 0
for group in allGroups:
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        for trip  in group:
                maxRed = max(maxRed, trip[0])
                maxGreen = max(maxGreen, trip[1])
                maxBlue = max(maxBlue, trip[2])

        setPower += maxRed*maxGreen*maxBlue
        print(maxRed, maxGreen, maxBlue)

print(setPower)
# %%
