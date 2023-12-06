#%%


with open("input.txt") as f:
        lines = f.readlines()
        
# %%

import re
import numpy as np

timesToBeat = [int(s) for s in re.findall("\d+", lines[0])]
distances = [int(s) for s in re.findall("\d+", lines[1])]

ways = []
for j in range(0, len(timesToBeat)):
        T = timesToBeat[j]
        d = distances[j]
        if((0.5*T)**2 >= d):
                x1 = int( np.ceil(0.5*T - np.sqrt((0.5*T)**2 - d)))
                x2 = int( np.floor(0.5*T + np.sqrt((0.5*T)**2 - d)))
                print(x1, x2, x2 - x1 + 1)
                ways.append(x2 - x1 + 1)

print(np.prod(np.asarray(ways)))


for j in range(0, len(timesToBeat)):
        T = timesToBeat[j]
        d = distances[j] 
        check = []
        for t in range(0, T):
                check.append(t**2 + d - T*t <= 0)


# %%

timesToBeat2 = int(re.findall("\d+", re.sub(" ", "", lines[0]))[0])

distances2 = int(re.findall("\d+", re.sub(" ", "", lines[1]))[0])

T = timesToBeat2
d = distances2
if((0.5*T)**2 >= d):
        x1 = int( np.ceil(0.5*T - np.sqrt((0.5*T)**2 - d)))
        x2 = int( np.floor(0.5*T + np.sqrt((0.5*T)**2 - d)))
        print(x1, x2, x2 - x1 + 1)



# %%
