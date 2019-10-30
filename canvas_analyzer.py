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
import canvas_requests

__version__ = 7


# 1) main
def main(user):
    '''

    :param user:
    :return:
    '''
    print_user_info(canvas_requests.get_user(user))
    print_courses(canvas_requests.get_courses(user))
    filter_available_courses(canvas_requests.get_courses(user))
    get_course_ids(canvas_requests.get_courses(user))
    choose_course(get_course_ids(canvas_requests.get_courses(user)))


# 2) print_user_info
def print_user_info(dicty: dict):
    '''

    :param dicty:
    :return:
    '''
    print("Name: " + dicty["name"])
    print("Title: " + dicty["title"])
    print("Email: " + dicty["primary_email"])
    print("Bio: " + dicty["bio"])


# 3) filter_available_courses
def filter_available_courses(courses: [list]) -> [list]:
    '''

    :param courses:
    :return:
    '''
    coursey = []
    for available in courses:
        if available["workflow_state"] == 'available':
            coursey.append(dict(available))
        else:
            pass
    return coursey


# 4) print_courses
def print_courses(courses: list):
    '''

    :param courses:
    :return:
    '''
    for info in courses:
        print("ID: " + info["course_id"])
        print("Name " + info["name"])


# 5) get_course_ids
def get_course_ids(courses: list) -> [int]:
    '''

    :param courses:
    :return:
    '''
    id = []
    for info in courses:
        id.append(info["course_id"])
    return id


# 6) choose_course
def choose_course(listy: [int]) -> int:
    '''

    :param listy:
    :return:
    '''
    choosy = int(input("Enter a valid course ID please:"))  # gotta be nice
    while choosy not in listy:
        choosy = int(input("Enter a valid course ID please:"))
    return choosy


# 7) summarize_points
def summarize_points(submissions: [dict]):
    '''

    :param submissions:
    :return:
    '''
    points_obtained = 0
    points_possible_so_far = 0
    for sub in submissions:
        if sub["score"] != None:
            score = sub["score"] * sub["assignment"]["group"]["group_weight"]
            points_obtained = points_obtained + score
            current_grade = round((points_obtained / score) * 100)
            points = sub["assignment"]["points_possible"] * sub["assignment"]["group"]["group_weight"]
            points_possible_so_far = points + points_possible_so_far
        print("Current Grade: " + str(current_grade))
        print("Points possible so far: " + str(points_possible_so_far))
        print("Points Obtained: " + str(points_obtained))


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
