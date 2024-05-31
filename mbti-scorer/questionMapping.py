#parse questionMapping.csv,extract personality aspect and coefficient
import csv

mapping = {}

with open('questionMapping.csv',"r") as cFile:
    reader = csv.reader(cFile)
    for i,row in enumerate(reader):
        if i == 0:
            continue
        question,p_idx,C = row[0],row[1],row[2]
        mapping[question] = [p_idx,C]

