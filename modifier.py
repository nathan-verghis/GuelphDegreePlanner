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
    temp1 = " "
    tempSplit = " "
    tempSplit2 = " "
    rest = " "
    rest = course['restrictions']

    #TODO: STORE RESULTS 
    prio = False
    cons = False
    restric = False

    # for priority access course
    try:
        temp = rest.split("This")
        temp = temp[0]
        prio = True
    except Exception:
        temp = rest

    # for Instructor consent 
    try:
        tempSplit = temp.split("Instructor")
        tempSplit2 = tempSplit[0]
        temp = tempSplit2
        cons = True
    except Exception:
        pass

    # for Restricted    
    try:
        temp1 = temp.split("Restricted")
        temp = temp1[0]
        restric = True
    except Exception:
        pass


    # for general case 

    try:
        # Breaking up the actual course codes
        temp = temp.strip()
        temp = temp.split(", ")
        
    except Exception:
        pass

    
    #tempSplit2 as final list of courses required? still need to solve priority 
    #access and instructor access issues ... possible as booleans?
    print(name)
    print(temp)
    print(" ")





if __name__ == '__main__':
    courses = read_json('./courses.json')
    for course in courses:
        format_strings(course)