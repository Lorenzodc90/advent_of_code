# %%



with open("input.txt") as f:
        lines = f.readlines()
# %%

import numpy as np
workingMat = []
allPoints = ['.' for _ in range(0, 142)]
workingMat.append(allPoints)

for line in lines:
        workingMat.append(list("." + line[0:140] + "."))


workingMat.append(allPoints)

workingMat = np.matrix(workingMat)

checkMat = np.zeros_like(workingMat)


def checkSurroundings(ii, jj):
        allCheck = False
        for i in range(ii-1, ii+2):
                for j in range(jj-1, jj+2):
                        allCheck = allCheck or ( (workingMat[i, j] != '.') and (not workingMat[i, j].isnumeric()) )
        return allCheck

sumzz = 0
for i in range(1, 141):
        print(i)
        j = 1
        wrkStr = ""
        chk = False
        while(j < 142):

                wrkStr = ""
                chk = False
                
                while(workingMat[i, j].isnumeric()):
                        wrkStr += workingMat[i, j]
                        chk = chk or checkSurroundings(i, j)
                        j += 1
                
                if(chk == True):
                        sumzz += int((wrkStr))
                else:
                        j += 1

                print(wrkStr)
                print(chk)

                
print(sumzz)
                
                

# %%

X, Y = np.where(workingMat == '*')
starsIDX = [[x, y] for x, y in zip(X, Y)]

words = []

sumzz = 0
for i in range(1, 141):
        print(i)
        j = 1
        wrkStr = ""
        chk = False
        while(j < 142):

                wrkStr = ""
                chk = False
                localWord = []
                localIdx = []
                while(workingMat[i, j].isnumeric()):
                        wrkStr += workingMat[i, j]
                        chk = chk or checkSurroundings(i, j)
                        localIdx.append( [i, j])
                        j += 1
                
                if(chk == True):
                        sumzz += int((wrkStr))
                        words.append([wrkStr, localIdx])
                        print(words[-1])
                else:
                        j += 1

                print(wrkStr)
                print(chk)


augmentedNumPos = []
augmentedNumIdx = []
for idx, word in enumerate(words):
        for numPos in word[1]:
                for q1 in [-1, 0, 1]:
                        for q2 in [-1, 0, 1]:
                                if(q1 != 0  or q2 != 0):
                                        q = np.asarray([q1, q2])
                                        print(q)
                                        augmentedNumPos.append(list(numPos + q))
                                        augmentedNumIdx.append(idx)


sumzzz = 0
addedNumbers = []
for starPos in starsIDX:
        print("\n")
        print(starPos)
        chosenIdx = np.where( [starPos == numPos for numPos in augmentedNumPos])
        chosenIdx = chosenIdx[0]
        iddx = np.unique([augmentedNumIdx[l] for l in chosenIdx])
        # print(chosenIdx)
        print(iddx)
        if(iddx.shape[0] >= 2):
                print(int(words[iddx[0]][0]), int(words[iddx[1]][0]) )
                addedNumbers.append([int(words[iddx[0]][0]), int(words[iddx[1]][0]) ])
                sumzzz += int(words[iddx[0]][0])*int(words[iddx[1]][0]) 
        # if(chosenIdx.shape[0] >= 2):

        #         iddx = np.unique([augmentedNumIdx[l] for l in chosenIdx])
                
        #         idx1 = augmentedNumIdx[chosenIdx[0]]
        #         num1 = words[idx1][0]
        #         k = 0
        #         while( k < chosenIdx.shape[0] and augmentedNumIdx[chosenIdx[k]] == idx1):
        #                 k += 1
                
        #         if(k == chosenIdx.shape[0]):
        #                 k = k-1
                
        #         idx2 = augmentedNumIdx[chosenIdx[k]]
                
        #         if(idx1 != idx2):
                        
        #                 num2 = words[idx2][0]
        #                 print(idx1, idx2, num1, num2)
        #                 sumzzz += int(num1)*int(num2)
                

print(sumzzz)
# for pos in starsIDX:
#         for word in words:
#                 cchk = False
#                 for q1 in [-1, 0, 1]:
#                         for q2 in [-1, 0, 1]:
#                                 q = np.asarray([q1, q2])
#                                 cchk = cchk or any([ all(numPos == pos +q) for numPos in word[1]])
#                 print(cchk)


# %%
