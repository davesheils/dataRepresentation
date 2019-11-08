import json

# create DICT
data = {
    'name':'joe',
    'age':21,
    "student": True
}
# print(data)
# look at the output, all categories will have single quotes

# convert to JSON

file = open("simpleJSON.json", 'w') # create/open file
# output of file will be in double quotes
# Note also, True becomes true, etc

# json.dump(data, file, indent=4) # write data to file
# indent is optional, it "prettifies" the data for readibility

jsonString = json.dumps(data)

print(jsonString)

# sending HTTP requests in python



