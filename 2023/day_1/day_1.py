#%%
import glob
import os
import re

print(os.getcwd())

with open('input.txt') as f:
    lines = f.readlines()

#%% part one 
sum = 0
for line in lines:
    str_num = re.findall(r'\d', line)
    sum += int(str_num[0] + str_num[-1])

print(sum)
# %% part two

good_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
good_strings_values = [str(i) for i in list(range(1, 10))]
good_strings_combined = [] #good_strings.copy()
good_strings_combined_values = [] #good_strings_values.copy()

ditto = {}

for s1 in good_strings:
	for s2 in good_strings:
                print([s1, s2])
                el1 = s1[0:-1]+s2[:]
                el2 = s1[0:]+s2[1:]
                print([el1, el2])
                good_strings_combined.append(el1)
                good_strings_combined.append(el2)
                good_strings_combined_values.append(s1+s2)
                good_strings_combined_values.append(s1+s2)
#%%
good_pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"
corresp = dict(zip(good_strings, (range(1, 1+len(good_strings)))))
corresp2 = dict(zip([str(j) for j in range(1, 1+len(good_strings))], (range(1, 1+len(good_strings)))))
corresp.update(corresp2)
sum2 = 0
for line in lines:
        # str_num = re.findall(good_pattern, line)
        res = []
        lineTmp = line
        for key, val in zip(good_strings_combined, good_strings_combined_values):
             lineTmp = re.sub(key, val, lineTmp)
        str_num = re.findall(good_pattern, lineTmp)
        str_num = [(corresp.get(key)) for key in str_num]
        print(line[0:-1])
        print(lineTmp[0:-1])
        print(str_num)
        print(str(str_num[0]) + str(str_num[-1]))
        print(int(str(str_num[0]) + str(str_num[-1])))
        sum2 += int(str(str_num[0]) + str(str_num[-1]))



# %%
