import json
import statistics as stat
from typing import Dict, List


# Parsing json for values by key/target

def find_values(data: Dict[str, str], target: str, res: List = []) -> List[str]:
    """ Finding values by target-key inside nested json data recursively """    
    if type(data) is dict:
        for key,value in data.items():
            if key == target:
                res.append(value)
            find_values(value,target,res)
    
    elif type(data) is list:
        for item in data:
            find_values(item,target,res)
    
    return res

# Apply

json_file = open('teszt-json.json')
data = json.load(json_file) # type -> dictionary
json_file.close()

vals = find_values(data,'value')
print(vals)
# Printing the mean of the founded values
vals = map(lambda x: float(x), vals) # convert elements to float
print(f"Mean: {round(stat.mean(vals),2)}")



