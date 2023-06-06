"""
import json
python_data = {
        'Name': "Ram",
        'Roll': 1,
        'Class': 10
    }
json_data = json.dumps(python_data) # Converting Python Object to Json data type using jumps() method and {"name":"Sita","roll": 10,"class": 11}
print(json_data)

"""

""" Converting Json data to Python object using loads(data) => This is used to parse json string, and take a string as input and returns a dictionary as output."""

import json

json_data = """{
    "name":"Sita",
    "roll": 10,
    "class": 11
}"""
parsed_data = json.loads(json_data)
print(parsed_data)