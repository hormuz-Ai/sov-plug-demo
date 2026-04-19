import sys, json
inp = json.load(sys.stdin)
dest = inp.get("destination_country", "")
if dest != "ZA":
    print('["BLOCKED"]')
else:
    print('[]')
