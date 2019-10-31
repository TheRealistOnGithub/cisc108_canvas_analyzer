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
import matplotlib.pyplot as plt
import datetime

__version__ = 7


# 1) main
def main(user):
    '''
    Consumes a string representing the user token (e.g., 'hermione') and calls all the other functions as shown in the diagram.
    :param user:
    :return:
    '''
    print_user_info(canvas_requests.get_user(user))
    courses = filter_available_courses(canvas_requests.get_courses(user))
    print_courses(courses)
    selected = choose_course(get_course_ids(courses))
    summarize_points(canvas_requests.get_submissions(user, selected))
    summarize_groups(canvas_requests.get_submissions(user, selected))
    plot_scores(canvas_requests.get_submissions(user, selected))
    plot_grade_trends(canvas_requests.get_submissions(user, selected))


# 2) print_user_info
def print_user_info(dicty: dict):
    '''
    Consumes a User dictionary and prints out the user's name, title, primary email, and bio. It does not return anything.
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
    Consumes a list of Course dictionaries and returns a list of Course dictionaries where the workflow_state key's value is 'available' (as opposed to 'completed' or something else).
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
    Consumes a list of Course dictionaries and prints out the ID and name of each course on separate lines.
    :param courses:
    :return:
    '''
    for info in courses:
        print("ID: " + info["course_id"])
        print("Name " + info["name"])


# 5) get_course_ids
def get_course_ids(courses: list) -> [int]:
    '''
    Consumes a list of Course dictionaries and returns a list of integers representing course IDs.
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
    Consumes a list of integers representing course IDs and prompts the user to enter a valid ID, and then returns an integer representing the user's chosen course ID.
    If the user does not enter a valid ID, the function repeatedly loops until they type in a valid ID.
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
    Consumes a list of Submission dictionaries and prints out three summary statistics about the submissions where there is a score (i.e. the submissions score is not None
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
def summarize_groups(submissions: [dict]):
    '''
    Consumes a list of Submission dictionaries and prints out the group name and unweighted grade for each group.
    :param submissions:
    :return:
    '''
    groups = {}
    points_possible = {}
    for sub in submissions:
        if submissions != None:
            name = submissions["assignment"]["group"]["name"]
            if name not in groups:
                groups[name] = 0
                points_possible[name] = 0
            groups[name] = groups[name] + sub["score"]
            points_possible[name] = sub["assignment"]["points_possible"] + points_possible[name]
    for name in groups:
        key, value = groups[name], points_possible[name]
        print("*", name, ":", round(100 * (key / value)))


# 9) plot_scores
def plot_scores(submissions: [dict]):
    '''
    Consumes a list of Submission dictionaries and plots each submissions' grade as a histogram.
    :param submissions:
    :return:
    '''
    x = []
    for sub in submissions:
        if sub["score"] != None and sub["assignment"]["points_possible"] > 0:
            grade = (100 * sub["score"]) / (sub["assignment"]["points_possible"])
            x.append(grade)
        plt.hist(x)
        plt.title("Distribution of Grades")
        plt.xlabel("Grades")
        plt.ylabel("# of Assignments")
        plt.show()


# 10) plot_grade_trends
def plot_grade_trends(submissions: [dict]):
    '''
    Consumes a list of Submission dictionaries and plots the grade trend of the submissions as a line plot.
    :return:
    '''
    running_high_sum = 0
    running_high_sums = []
    running_low_sum = 0
    running_low_sums = []
    maximum = 0
    maximums = []
    dates = []
    total_points = 0
    for sub in submissions:
        total_points = sub["assignment"]["points_possible"] * sub["assignment"]["group"][
            "group_weight"] + total_points
        a_string_date = sub["assignment"]["due_at"]
        dates.append(datetime.datetime.strptime(a_string_date, "%Y-%m-%dT%H:%M:%SZ"))
        maximum = 100 * sub["assignment"]["points_possible"] * sub["assignment"]["group"][
            "group_weight"] + maximum
        maximums.append(maximum)
        if sub["score"] is None:
            running_high_sum = 100 * sub["assignment"]["points_possible"] * sub["assignment"]["group"][
                "group_weight"] + running_high_sum
            running_high_sums.append(running_high_sum)
            running_low_sum = running_low_sum + 0
            running_low_sums.append(running_low_sum)
        else:
            running_high_sum = 100 * sub["score"] * sub["assignment"]["group"][
                "group_weight"] + running_high_sum
            running_high_sums.append(running_high_sum)
            running_low_sum = 100 * sub["score"] * sub["assignment"]["group"][
                "group_weight"] + running_low_sum
            running_low_sums.append(running_low_sum)
    final_high_sums = []
    for hnum in running_high_sums:
        finalh = hnum / total_points
        final_high_sums.append(finalh)
    final_low_sums = []
    for lnum in running_low_sums:
        finall = lnum / total_points
        final_low_sums.append(finall)
    final_max = []
    for mnum in maximums:
        finalm = mnum / total_points
        final_max.append(finalm)
    plt.plot(dates, final_high_sums, label="Highest")
    plt.plot(dates, final_low_sums, label="Lowest")
    plt.plot(dates, final_max, label="Maximum")
    plt.legend()
    plt.title("Grade Trend")
    plt.ylabel("Grade")
    plt.show()


# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')

    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')
