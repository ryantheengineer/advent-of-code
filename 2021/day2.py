# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:56:06 2022

@author: Ryan.Larson
"""
import pandas as pd

filename = "day_2_2021_input.txt"

##### Part 1 #####

with open(filename, "r") as f:
    lines = f.readlines()
    data = [line.split(" ") for line in lines]

direction = []
distance = []
for entry in data:
    direction.append(entry[0])
    distance.append(int(entry[1]))
    
df = pd.DataFrame({"Direction":direction, "Distance":distance})

forward = df[df["Direction"] == "forward"]
down = df[df["Direction"] == "down"]
up = df[df["Direction"] == "up"]

sumforward = forward["Distance"].sum()
sumup = up["Distance"].sum()
sumdown = down["Distance"].sum()

depth = sumdown - sumup

final_val = sumforward*depth

##### Part 2 #####

def part_2(df):
    
    def command(direction, distance, aim, horizontal, depth):
        if direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        else:
            horizontal += distance
            depth += aim*distance
            
        return aim, horizontal, depth
            
    aim = 0
    horizontal = 0
    depth = 0
    
    for i in range(len(df)):
        direction = df.loc[i,"Direction"]
        distance = df.loc[i,"Distance"]
        
        aim, horizontal, depth = command(direction, distance, aim, horizontal, depth)
        
    print("Aim:\t{}".format(aim))
    print("Horizontal:\t{}".format(horizontal))
    print("Depth:\t{}".format(depth))
    
    print("\nAnswer:\t{}".format(horizontal*depth))
    
part_2(df)
    