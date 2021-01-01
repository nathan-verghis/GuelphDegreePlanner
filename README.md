Modifier program:
 - open JSON
 - open dictionary 'courses'
 - iterate through list of courses
 - at each iteration do the following
    - remove trailing space from name
    - go through description, replace '\' (and following character) with ' '
    - turn restrictions into a dictionary containing a list of courses restricted, and the restriction message
    - format prereqs
    -