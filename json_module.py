import json # this module is used to work with json (javascript object notation) data

data = '{"var1": "vikash", "var2": "shubhum"}'
# print(data)
parsed = json.loads(data)
print(parsed['var1'])

data2 = {
    "channel_name": "vikashJi",
    "name": "sanu",
    "isbad": False
}

# makeing a js compactable we use json.dumps
jscomp = json.dumps(data2)
print(jscomp)