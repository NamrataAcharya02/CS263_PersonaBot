import json
from settings import config


json_filename = config["SRC_DIR"] + "INTJ_pre_convo_test_3.json"

with open(json_filename,"r") as jFile:
    data = json.load(jFile)


#sometimes files can have duplicate user rows. This ensures that we skip past them.
init_turn = 0
for i in range(0,len(data)-1,1):
    if "1 to 7" in data[i]['content']:
        init_turn = i+1
        break



print(f"init turn is {init_turn}")
print(data[init_turn]['content'])