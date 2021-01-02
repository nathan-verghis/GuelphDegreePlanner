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

    # for priority access course
    try:
        temp = rest.split("This")
    except Exception:
        temp = rest

    # for Instructor consent 
    try:
        tempSplit = temp[0].split("Instructor")
        tempSplit2 = tempSplit[0]
        tempSplit2.strip()
        temp = tempSplit2.split(", ")
    except Exception:
        pass

        

    # for general case 

    try:
        # GETTING RID OF UNNECESSARY ENTRIES
        
        temp1 = temp.split("Restricted")
        temp = temp1[0]

        #Restricted

        # Breaking up the actual course codes
        temp.strip()
        temp.split(", ")
        
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