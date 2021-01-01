from course import Course
import json

def read_json(filename):
    with open(filename) as src:
        bigDict = json.load(src)

    courses = bigDict['courses']
    return courses


if __name__ == '__main__':
    courses = read_json('./courses.json')