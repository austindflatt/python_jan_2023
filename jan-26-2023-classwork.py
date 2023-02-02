"""
1.
Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.
Input : {'a': 100, 'b':200, 'c':300}
Output : 600

Input : {'x': 25, 'y':18, 'z':45}
Output : 88
"""


def sum_dict_items(d):
    return sum(d.values())


# test the function
input1 = {'a': 100, 'b': 200, 'c': 300}
print(sum_dict_items(input1))

input2 = {'x': 25, 'y': 18, 'z': 45}
print(sum_dict_items(input2))

"""
2.
Given a dictionary, find the largest item in a dictionary, the max() function
"""


def find_largest_item(d):
    return max(d, key=d.get)


# test the function
input1 = {'a': 100, 'b': 200, 'c': 300}
print(find_largest_item(input1))

input2 = {'x': 25, 'y': 18, 'z': 45}
print(find_largest_item(input2))


"""
3.
Given different scored marks of students. We need to find grades. 
The test score is an average of the respective marks scored in assignments, tests and lab-works. 
The final test score is assigned using below formula.

(use a dictionary to keep track of values)

10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works
  Grade will be calculated according to :

1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
Also, calculate the total class average and letter grade of class.
"""

students = [
    {"name": "Jack Frost",
     "assignment": [80, 50, 40, 20],
     "test": [75, 75],
     "lab": [78.20, 77.20]
     },

    {"name": "James Potter",
     "assignment": [82, 56, 44, 30],
     "test": [80, 80],
     "lab": [67.90, 78.72]
     },

    {"name": "Dylan Rhodes",
     "assignment": [77, 82, 23, 39],
     "test": [78, 77],
     "lab": [80, 80]
     },

    {"name": "Jessica Stone",
     "assignment": [67, 55, 77, 21],
     "test": [40, 50],
     "lab": [69, 44.56]
     },

    {"name": "Tom Hanks",
     "assignment": [29, 89, 60, 56],
     "test": [65, 56],
     "lab": [50, 40.6]
     },
    ]


def calc_avg(list_):
    return round(sum(list_) / len(list_), 2)


def calc_weighted_grade(avg_score, weight):
    return avg_score * weight


def calc_final_grade(assignment_weighted, test_weighted, lab_weighted):
    score = assignment_weighted + test_weighted + lab_weighted
    if score >= 90:
        return ("A", score)
    elif score >= 80:
        return ("B", score)
    elif score >= 70:
        return ("C", score)
    elif score >= 60:
        return ("D", score)
    else:
        return ("F", score)


def assign_final_grade(student):
    # get the avg for assignments, tests, and labs
    assignment_avg = calc_avg(student["assignment"])
    test_avg = calc_avg(student["test"])
    lab_avg = calc_avg(student["lab"])

    # get the weighted avg for each
    assignment_weighted = calc_weighted_grade(assignment_avg, .1)
    test_weighted = calc_weighted_grade(test_avg, .7)
    lab_weighted = calc_weighted_grade(lab_avg, .2)

    # get final grade
    final_grade = calc_final_grade(assignment_weighted, test_weighted, lab_weighted)

    # update student record
    student["grade"] = final_grade

    return student


all_grades = []
for student in students:
    all_grades.append(assign_final_grade(student)['grade'][1])
print(f"average class grade is: {calc_avg(all_grades)}")