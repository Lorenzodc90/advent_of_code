# %%



with open("input.txt") as f:
        lines = f.readlines()
        
# %%
import re

totalPoints = 0
for line in lines:
        splitty1 = line.split(":")
        splitty2 = splitty1[1].split("|")
        
        winningNums = re.findall("\d+", splitty2[0])
        hadNums = re.findall("\d+", splitty2[1])

        matching = []
        for n in hadNums:
                for nn in winningNums:
                        if(n == nn):
                                matching.append(n)
        # stringHad = " | ".join(hadNums)
        # stringWinning = " " + " ".join(winningNums) + " "
        # matching = re.findall(stringHad, stringWinning)
        
        if(matching != None):
                points = int(2**(len(matching) - 1))
        else:
                points = 0
        
        totalPoints += points

print(totalPoints)

# %% part 2
import numpy as np

idList = list(range(0, len(lines)))
id = 0

multipliers = np.ones(shape = (len(lines,)))
for idx, line in enumerate(lines):

        splitty1 = line.split(":")
        splitty2 = splitty1[1].split("|")
        
        winningNums = re.findall("\d+", splitty2[0])
        hadNums = re.findall("\d+", splitty2[1])

        matching = []
        for n in hadNums:
                for nn in winningNums:
                        if(n == nn):
                                matching.append(n)
        # stringHad = " | ".join(hadNums)
        # stringWinning = " " + " ".join(winningNums) + " "
        # matching = re.findall(stringHad, stringWinning)
        
        if(matching != None):
                points = len(matching)
                for i in range(1, points + 1):
                        multipliers[idx + i] += multipliers[idx]
               

print(multipliers.sum())
# %%
