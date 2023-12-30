# Original data
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Changes
# 1- Change the value 10 in x to 15
x[1][0] = 15

# 2- Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# 3- In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# 4- Change the value 20 in z to 30
z[0]['y'] = 30

# Print the updated values
print("1- Updated x:", x)
print("2- Updated last_name of the first student:", students[0]['last_name'])
print("3- Updated 'Messi' to 'Andres' in sports_directory:", sports_directory['soccer'][0])
print("4- Updated value 20 to 30 in z:", z)


def iterateDictionary(some_list):
    for person in some_list:
        output = ""
        for key, value in person.items():
            output += f"{key} - {value}, "
        print(output[:-2])  # to remove the trailing comma and space

# Example usage with the provided list
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for person in some_list:
        print(person[key_name])

# Example usage with the provided list
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', students)

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('last_name', students)

def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)
        print()  # Add an empty line between sections

# Example usage with the provided dictionary
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)