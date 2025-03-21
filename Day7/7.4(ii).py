"ii) Write a program to dump/write data in json file."

import json


dict1 ={
    "stud1": {
        "name": "Lisa",
        "roll.no":25,
        "age": "34",
    },
    "stud2": {
        "name": "Elis",
        "roll.no":52,
        "age": "24",
    },
}

out_file = open("studInfo.json", "w")

json.dump(dict1, out_file, indent = 6)

out_file.close()
