# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:23:58 2022

@author: Ryan.Larson
"""

import numpy as np

filename = "day_1_2021_input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()
    data = [int(entry) for entry in lines]
    
prev = data[0]
increase = 0
decrease = 0
# for pt in data[1:]:
#     if pt > prev:
#         increase += 1
#     prev = pt

for i,pt in enumerate(data):
    if i == 0:
        continue
    elif data[i] > data[i-1]:
        increase += 1
    else:
        decrease += 1

window = 3

sliding_windows = np.convolve(data, np.ones(3), 'valid')

increase = 0
decrease = 0
for i,pt in enumerate(sliding_windows):
    if i == 0:
        continue
    elif sliding_windows[i] > sliding_windows[i-1]:
        increase += 1
    else:
        decrease += 1

# df = pd.read_csv(filename)

# increase = 0
# decrease = 0

# for i in range(len(df)):
#     if i == 0:
#         continue
#     elif df.loc[i,"127"] > df.loc[i-1,"127"]:
#         increase += 1
#     else:
#         decrease += 1
        
# print("increase:\t{}".format(increase))
# print("decrease:\t{}".format(decrease))
