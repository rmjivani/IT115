#Import class library
import json


#Create the data dictionary
data = {

    'name': 'John Doe',
    'age' : 30,
    'city': 'New York, NY',
    'interests': ['golf', 'running', 'video games'],
    'is_student': False
    
}

#Create a Json file and write the python object contents to it
with open('data.json', 'w') as json_file:

    json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

