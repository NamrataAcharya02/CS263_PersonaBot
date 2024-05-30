# This will parse a json into a csv.
import json
import csv
from settings import config

# FILENAMES 
json_filename = config["SRC_DIR"] + config["SRC_JSON"]
csv_filename = config["DEST_DIR"] +config["DEST_CSV"]

def extractTerms(userRow:dict,agentRow:dict):
    if userRow['role'] != 'user' or agentRow['role'] != 'assistant':
        raise Exception('incorrect rows passed. Check that userRow is user prompt and agentRow is agent response.')
    prompt,response = userRow['content'],agentRow['content']
    return prompt,response

with open(json_filename,"r") as jFile:
    data = json.load(jFile)

#sometimes files can have duplicate user rows. This ensures that we skip past them.
init_turn = 0
for i in range(0,len(data)-1,1):
    if data[i]['role'] == data[i+1]['role']:
        init_turn = i+1
        break

if init_turn == len(data)-1:
    init_turn = 0

print(f"init turn is {init_turn}")

fields = ['turn','prompt','response'] + config["ANNOTATION_COLS"]




with open(csv_filename,'w') as csvFile:
    writer = csv.DictWriter(csvFile,fieldnames=fields)
    writer.writeheader()
    for idx in range(init_turn,len(data)-1,2):
        prompt,response = extractTerms(data[idx],data[idx+1])
        turn = (idx + 1 * (init_turn % 2)) // 2

        row = {'turn':turn,'prompt':prompt,'response':response}
        for i in range(3,len(fields)):
            row[fields[i]] = ''
        writer.writerow(row)
