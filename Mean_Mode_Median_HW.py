import pandas as pd
import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline = "")as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
total = 0

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))
    total = total + float(n_num)

#print(total)
n = len(new_data)

mean = total/n
print("The mean of the data is",mean)

new_data.sort()

if n%2==0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median =  (median1+median2) /2

else:
    median = new_data[n+1//2]

print("The median is",median)

data = Counter(new_data)
mode_data_for_range = {
                        "75-85": 0,
                        "85-95": 0,
                        "95-105": 0,
                        "105-115": 0,
                        "115-125": 0,
                        "125-135": 0,
                        "135-145": 0,
                        "145-155": 0,
                        "155-165": 0,
                        "165-175": 0
                        }
for weight, occurence in data.items():
      if 75 < weight < 85:
          mode_data_for_range["75-85"] += occurence
      elif 85 < weight < 95:
          mode_data_for_range["85-95"] += occurence           
      elif 95 < weight < 105:
          mode_data_for_range["95-105"] += occurence
      elif 105 < weight < 115:
          mode_data_for_range["105-115"] += occurence
      elif 115 < weight < 125:
          mode_data_for_range["115-125"] += occurence
      elif 125 < weight < 135:
          mode_data_for_range["125-135"] += occurence
      elif 135 < weight < 145:
          mode_data_for_range["135-145"] += occurence
      elif 145 < weight < 155:
          mode_data_for_range["145-155"] += occurence
      elif 155 < weight < 165:
          mode_data_for_range["155-165"] += occurence
      elif 165 < weight < 175:
          mode_data_for_range["165-175"] += occurence
      
mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
            
mode = float((mode_range[0] + mode_range[1]) / 2)
print("The mode is", mode)
