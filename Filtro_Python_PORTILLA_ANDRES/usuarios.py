import json
filepath="file.json"
def store_json_data(data):
    with open(filepath, 'w') as outfile:
        data=filepath
        for i in data:
            filepath["ID"]="A"
    json.dump(data, outfile)
    
store_json_data()