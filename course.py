class Course:
    def __init__(self, cCode, name, description, equates, semesters, restrictions, offerings, creditWeight, department, prereqs):
        self.cCode = cCode
        self.name = name
        self.description = description
        self.equates = equates
        self.semesters = semesters
        self.restrictions = restrictions
        self.offerings = offerings
        self.creditWeight = creditWeight
        self.department = department
        self.prereqs = prereqs