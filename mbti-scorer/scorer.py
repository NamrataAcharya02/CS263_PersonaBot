import json
from settings import config
from questionMapping import mapping
import jellyfish

json_filename = config["SRC_DIR"] + "ESFP_pre_convo_test_4.json"

def similar(a,b):
    return jellyfish.jaro_similarity(a, b)

#personality aspects array: 1-> introverted/extroverted, 2-> intuitive/ sensing, 
# 3-> Thinking/ Feeling and 4-> Judging/ Prospecting

p_arr = [0,0,0,0,0]


def extractTerms(userRow:dict,agentRow:dict):
    if userRow['role'] != 'user' or agentRow['role'] != 'assistant':
        raise Exception('incorrect rows passed. Check that userRow is user prompt and agentRow is agent response.')
    prompt,response = userRow['content'],agentRow['content']
    return prompt,response

def calc_type(extroversion,sensing,feeling,prospecting):
    result = []
    if extroversion >0:
        result.append("E")
    else:
        result.append("I")
    if sensing > 0:
        result.append("S")
    else:
        result.append("N")
    if feeling >0:
        result.append("F")
    else:
        result.append("T")
    if prospecting > 0:
        result.append("P")
    else:
        result.append("J")
    return "".join(result)

with open(json_filename,"r") as jFile:
    data = json.load(jFile)


#sometimes files can have duplicate user rows. This ensures that we skip past them.
init_turn = 0
for i in range(0,len(data)-1,1):
    if "1 to 7" in data[i]['content']:
        init_turn = i+1
        break

for i in range(init_turn,len(data)-1,2):
    question = data[i]['content']
    if question not in mapping.keys():
        raise Exception("Unfamiliar Question!")
    p_idx, C = mapping[question][0],mapping[question][1]
    answer = data[i+1]['content']

    if p_idx != '' and C != '':
        p_arr[int(p_idx)] += int(C) * (int(answer)-4)

print(p_arr)
print(calc_type(p_arr[1],p_arr[2],p_arr[3],p_arr[4]))


        