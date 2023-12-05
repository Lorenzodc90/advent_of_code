#%%


with open("input.txt") as f:
        lines = f.readlines()
        
#%%
import re
seedStr = lines[0]
seeds = [int(r) for r in re.findall("\d+", seedStr)]

parts = []
j = 1
while( j < len(lines)-2):
        j += 1
        print(j)
        print(lines[j][0])
        if(lines[j][0].isalpha()):
                j += 1
                subPart = []
                while(j < len(lines) and lines[j][0].isnumeric()) :
                        print("subsetting", j)
                        subPart.append(lines[j])
                        j += 1
                        
                parts.append(subPart)
import numpy as np

matrices = []
for subPart in parts:
        parsed = []
        for line in subPart:
                nums = re.findall("\d+", line)
                parsed.append([int(n) for n in nums])
        matr = np.matrix(parsed)
        matrices.append(matr)


#%%
def interrogateMatrix(v, M):
        q = v
        # print(q)
        # print(M[:, 2])
        qq = np.multiply(q >= M[:, 1], q < M[:, 1] + M[:, 2])
        qq = np.squeeze(np.array(qq))
        qi = np.where(qq)
        # print(qi)

        if(qi[0].shape[0] == 0):
                return v
        else:
                return M[qi[0][0], 0] + (v -  M[qi[0][0], 1])

locations = []
for seed in seeds:
        v = seed
        for M in matrices:
                v = interrogateMatrix(v, M)
        locations.append(v)


print(min(locations))

#%%

# def interrogateMatrixList(seedStart, seedRange, M):
#         minLoc = np.Inf
#         for j in range(seedStart, seedStart + seedRange):
#                 print(j, seedStart + seedRange - j)
#                 v = j
#                 for M in matrices:
#                         q = v
#                         # print(q)
#                         # print(M[:, 2])
#                         qq = np.multiply(q >= M[:, 1], q < M[:, 1] + M[:, 2])
#                         qq = np.squeeze(np.array(qq))
#                         qi = np.where(qq)
#                         # print(qi)

#                         if(qi[0].shape[0] == 0):
#                                 None
#                         else:
#                                 v = M[qi[0][0], 0] + (v -  M[qi[0][0], 1])
#                 minLoc = min([minLoc, v])
#         return minLoc

# allLocs = []
# for seedStart, seedRange in zip(seeds[0::2], seeds[1::2]):
#         tLoc = interrogateMatrixList(seedStart, seedRange, M)
#         allLocs.append(tLoc)



# %%

def intervalIntersection(interval1, interval2):
        if(interval2[0] > interval1[1] or interval1[0] > interval2[1]):
                return []
        else:
                a = max([interval1[0], interval2[0]])
                b = min([interval1[1], interval2[1]])
                return [a, b]
        # if(interval1[1] > interval2[0]):
        #         return []
        # elif(interval1[0] <= interval2[0] and interval1[1] >= interval2[1]):
        #         return interval2
        # elif(interval2[0] <= interval1[0] and interval2[1] >= interval1[1]):
        #         return interval1
        # elif(interval1[1] >= interval2[0]):
        #         return [interval1[1], interval2[0]]

def intervalDiffWithInter(interval, intersection):
        res = []
        if(interval[0] != intersection[0]):
                res.append([interval[0], intersection[0]])
        if(interval[1] != intersection[1]):
                res.append([intersection[1], interval[1] ])
        return res

def intervalDifference(interval, intervalToSub):
        intr = intervalIntersection(interval, intervalToSub)
        if len(intr) == 0:
                return [interval]
        else:
                return intervalDiffWithInter(interval, intr)
                # res = []
                # if(interval[0] != intr[0]):
                #         res.append([interval[0], intr[0]])
                # if(interval[1] != intr[1]):
                #         res.append([intr[1], interval[1] ])
                # return res

def interrogateMatrixRange(inputInterval, M):
        #get intervals
        # inputInterval = [min([v1, v2]), max([v1, v2])]
        # intervals = []
        # for i in range(0, M.shape[0]):
        #         intervals.append([[M[i, 1], M[i, 1] + M[i, 2] - 1], [M[i, 0], M[i, 0] + M[i, 2] - 1]])
        
        outputIntervals = []
        intrrs = []
        for i in range(0, M.shape[0]):
                intervalSource = [M[i, 1], M[i, 1] + M[i, 2] -1]
                intersection = intervalIntersection(inputInterval, intervalSource)
                intrrs.append(intersection)
                if(len(intersection) > 0):
                        out1 = intersection[0] - M[i, 1] + M[i, 0]
                        out2 = intersection[1] - M[i, 1] + M[i, 0]
                        outputIntervals.append([out1, out2])

        inputIntervalCopy = [inputInterval.copy()]
        for i in range(0, M.shape[0]):
                intervalSource = [M[i, 1], M[i, 1] + M[i, 2] -1]
                oo = []
                for ii in inputIntervalCopy:
                        # print(ii)
                        eu = intervalDifference(ii, intervalSource)
                        # print(eu)
                        oo.extend(eu)
                inputIntervalCopy = oo
        
        outputIntervals.extend(inputIntervalCopy)

        return outputIntervals
        # for intr in intervals:
        #         intersection = intervalIntersection(inputInterval, intr[0])
        #         intrrs.append(intersection)
        #         if(len(intersection) > 0):
        #                 rg = intr[1][0] - intr[0][0]
        #                 outputIntervals.append([intersection[0] + rg, intersection[1] + rg])


def getLoc(seed):
        v = seed
        for M in matrices:
                v = interrogateMatrix(v, M)
        return v

plausibleSeeds = []

allOuts = []
for seedStart, seedRange in zip(seeds[0::2], seeds[1::2]):


        inputIntervals = [[seedStart, seedStart + seedRange - 1]]
        
        for M in matrices:
                outs = []
                for inInt in inputIntervals:
                        outs.extend(interrogateMatrixRange(inInt, M))
                inputIntervals = outs
        
        allOuts.extend(inputIntervals)
        

        # s1 = seedStart
        # s2 = seedStart + seedRange - 1
        # r = 0.2
        # while(np.abs(s1 - s2) > 1000):
        #         print([s1, s2])
        #         s1c = int(s1 + r*(s2 - s1))
        #         s2c = int(s1 + (1-r)*(s2 - s1))

        #         f1c = getLoc(int(s1c))
        #         f2c = getLoc(int(s2c))

        #         if(f1c < f2c):
        #                 s2 = s2c
        #                 s2c = s1
        #         else:
        #                 s1 = s1c
        #                 s1c = s2
        # plausibleSeeds.append(list(range(s1, s2)))
        # for seed in [seedStart, seedStart + seedRange-1]:
        #         v = seed
        #         for M in matrices:
        #                 v = interrogateMatrix(v, M)
        #         locationPlus.append(v)
# locs = []
# for seedGroup in plausibleSeeds:
#         for seed in seedGroup:
#                 loc = getLoc(seed)
#                 locs.append(loc)

# print(min(locs))
print(np.min( np.asarray(allOuts)[:, 0]))
# %%
# mins = []
# for a, b in zip(plausibleSeeds[0::2], plausibleSeeds[1::2]):
#         mins.append(min([a, b]))

# print(min(mins))
# %%
