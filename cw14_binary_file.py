import pickle
import string
import os

numbers = [1,2,3,4,5]
serialized_data = pickle.dumps(numbers)
print(serialized_data)

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(script_dir)
    return os.path.join(script_dir, file_name)

print(create_path('contacts.txt'))

def serialize(file_name, data):
    with open(create_path(file_name), 'wb') as file:
        pickle.dump(data, file)

def deserialize(file_name):
    with open(create_path(file_name), 'rb') as file:
        data=pickle.load(file)
    return data


try:
    letters=[symbol for symbol in string.ascii_letters]
    file_name='letters.data'
    print(letters)
    serialize(file_name, letters)
    letters_restored = deserialize(file_name)
    print(letters_restored)
except Exception as e:
    print(e)

import json

capitals={
    'Italy': "Rome",
    'Spain': "Madrid",
'Germany': "Berlin"
}
print(capitals)

s_capitals=json.dumps(capitals)
print(s_capitals)

print(json.loads(s_capitals))





def json_serialize(file_name, data):
    with open(create_path(file_name), 'w') as file:
        json.dump(data, file, indent=4)

def json_deserialize(file_name):
    with open(create_path(file_name), 'r') as file:
        data=json.load(file)
    return data


try:
    file_name='employee.data'

    employee_dict= {
        'company':'apple',
        'employees':[
            {
                'name':'tim cook',
                'age':55,
                'skills':['python','comm'],
            },
            {'name':'tim cook',
                'age':55,
                'skills':['python','comm'],
            }
        ],
    }
    json_serialize(file_name, employee_dict)
    des_dict = json_deserialize(file_name)
    print(f'before{employee_dict}')
    print(f'after{des_dict}')
except Exception as e:
    print(e)

