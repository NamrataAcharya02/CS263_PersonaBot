## Script to score an entire batch of json files ##

import os
from settings import config
from scorer import runScorer
import csv

directory = os.fsencode(config['SRC_DIR'])
csv_filename = "./results.csv"

fields = ["filename","prompt","Scorer result"]

with open(csv_filename,'w') as csvFile:
    writer = csv.DictWriter(csvFile,fieldnames=fields,lineterminator="\n")
    writer.writeheader()
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not filename.endswith(".json"):
            continue
        mbti_type = runScorer(filename)
        writer.writerow({"filename":filename,"prompt":"","Scorer result":mbti_type})
        
