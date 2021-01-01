from course import Course
import json

def read_json(filename):
    with open(filename) as src:
        bigDict = json.load(src)

    courses = bigDict['courses']
    return courses




def format_strings(course):
    # Formatting name
    name = " "
    name = course['name']
    name.strip()
    
    # formatting description
    desc = " "
    desc = course['description']
    # only one \ character in all json file, and is 'u'
    desc.replace(r"\u", " ")
    
    # Formatting restrictions
    temp = " "
    tempSplit = " "
    tempSplit2 = " "
    rest = " "
    rest = course['restrictions']

    # for priority access course
    temp = rest.split("This")
    
    # for Instructor consent 
    tempSplit = temp[0].split("Instructor")
    tempSplit2 = tempSplit[0]
    tempSplit2.strip()
    tempSplit2.split(", ")

    #tempSplit2 as final list of courses required? still need to solve priority 
    #access and instructor access issues ... possible as booleans?





if __name__ == '__main__':
    courses = read_json('./courses.json')
    for course in courses:
        format_strings(course)