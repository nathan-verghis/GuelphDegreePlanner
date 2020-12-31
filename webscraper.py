import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from course import Course


class CourseGetter:
    def __init__(self):
        self.bot = webdriver.Firefox()
        self.courses = []

    def start(self):
        self.bot.get("https://www.uoguelph.ca/registrar/calendars/undergraduate/current/c12/index.shtml")

    def getData(self):

        # 
        div = self.bot.find_element_by_class_name("subnav")
        ul = div.find_elements_by_css_selector("ul")[1]
        ul = ul.find_elements_by_css_selector("li")
        programs = []
        programNames = []
        for li in ul:
            programs.append(li.find_element_by_css_selector("a").get_attribute("href"))
            programNames.append(li.find_element_by_css_selector("a").text)

        # first we iterate over the ul
        for program in programs:
            self.bot.get(program)
            content = self.bot.find_element_by_id("content")
            courses = content.find_elements_by_class_name("course")
            for course in courses:
                nameSplit = course.find_element_by_css_selector("a").text.split(" ")
                cCode = nameSplit[0]
                creditWeight = nameSplit[-1]
                semesters = nameSplit[-3]
                name = ""
                offerings = None
                prereqs = None
                restrictions = None
                equates = None
                y = len(nameSplit)
                for x in range(y):
                    if x > 0 and x < y - 3:
                        name += nameSplit[x] + " "

                dTag = course.find_element_by_class_name("description")
                description = dTag.find_element_by_css_selector("td").text

                dTag = course.find_element_by_class_name("departments")
                department = dTag.find_element_by_css_selector("td").text

                try:
                    oTag = course.find_element_by_class_name("offerings")
                    offerings = oTag.find_element_by_css_selector("td").text
                except Exception:
                    pass

                try:
                    pTag = course.find_element_by_class_name("prereqs")
                    prereqs = pTag.find_element_by_class_name("text").text
                except Exception:
                    pass

                try:
                    eTag = course.find_element_by_class_name("equates")
                    equates = eTag.find_element_by_class_name("text").text
                except Exception:
                    pass

                try:
                    rTag = course.find_element_by_class_name("restrictions")
                    restrictions = rTag.find_element_by_css_selector("td").text
                except Exception:
                    pass

                self.courses.append(Course(cCode, name, description, equates, semesters, restrictions, offerings, creditWeight, department, prereqs))

x = CourseGetter()
x.start()
x.getData()