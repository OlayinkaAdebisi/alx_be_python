"""Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

Takes a dictionary (data) and a filename (filename) as input.
Serializes the dictionary to a JSON file with the given filename.
Deserializes the JSON file back into a dictionary.
Returns the deserialized dictionary.
"""
import json
def process_json(data: dict, filename: str) -> dict:
    data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}
    serialized =json.dumps(data)
    with open('data.JSON','w') as file:
        json.dump(data,file)
    #Deserialize the json file
    data = json.loads(serialized)
    return data
    #print(serialized)
data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}


process_json(data,"gg.py")