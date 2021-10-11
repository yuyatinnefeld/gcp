import json
import sys

if len(sys.argv) < 2:
    print("Input File Missing")
    sys.exit()

with open(sys.argv[1]) as json_data:
    data = json.load(json_data)
print(data)