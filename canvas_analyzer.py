"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Nitin Armstrong
"""
__version__ = 7


# 1) main
def main(user: str):


# 2) print_user_info
def print_user_info(dicty: dict):
    for str in dicty:
        print(str)


# 3) filter_available_courses
def filter_available_courses(courses: list) -> list:
    coursey = []
    for available in courses:
        if available["workflow_state"] == 'available':
            coursey.append(dict(available))
        else:
            pass
    return coursey


# 4) print_courses
def print_courses(courses:list):
    for info in courses:
        print(info["course_id"])
        print(info[""]) #yo chief find out the key


# 5) get_course_ids
def get_course_ids(courses:list)->[int]:
    id=[]
    for info in courses:
        id.append(info["course_id"])
    return id
# 6) choose_course
def choose_course(listy:[int])->int
# 7) summarize_points
# 8) summarize_groups
# 9) plot_scores
# 10) plot_grade_trends

# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')
