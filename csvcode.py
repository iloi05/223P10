import csv

counters = {"freshman": 0, "sophomores": 0, "juniors": 0, "seniors": 0}

students = {}

with open('Students.csv', mode = 'r') as student:
    s = csv.DictReader(student)
    for row in s:
        level = row["Level"]

        if level in counters:
            counters[level] += 1

with open('course enrollments.csv', mode = 'r') as enrollments:
    e = csv.DictReader(enrollments)
    for row in e:
        e_id = row["ID"]
        course = row["Course"]
        units = row["Units"]

        students[e_id] = {"Total_Units": 0, "CPSC_Units": 0}

        students[e_id]["Total_Units"] += units

        if course.startswith("CPSC"):
            students[e_id]["CPSC_Units"] += units