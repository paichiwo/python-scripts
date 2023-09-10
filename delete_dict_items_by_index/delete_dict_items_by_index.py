import json
from itertools import islice
# dict = {
#     "1": "abc",
#     "2": "def"
# }
#
# with open("test.txt", "w") as db:
#     json.dump(dict, db)
#

with open("test.txt", "r") as db:
    dict1 = json.load(db)

print(dict1[next(islice(dict1, 1, None))])
