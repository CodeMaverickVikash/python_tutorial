# json module: javascript object notation(json data)
import json

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