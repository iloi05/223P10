import csv

counters = {"freshman": 0, "sophomores": 0, "juniors": 0, "seniors": 0}

students = {}

with open('Students.csv', mode='r') as file1:
    s = csv.DictReader(file1)
    for row in s:
        level = row["Level"]

        if level in counters:
            counters[level] += 1
    print(f'{counters["freshman"]} freshmen')
    print(f'{counters["sophomores"]} sophomores')
    print(f'{counters["juniors"]} juniors')
    print(f'{counters["seniors"]} seniors')

with open('course enrollments.csv', mode = 'r') as file2:
    e = csv.DictReader(file2)
    for row in e:
        e_id = row["ID"]
        course = row["Course"]
        units = row["Units"]
    
    if e_id not in students:
        students[e_id] = {"Total_Units": 0, "CPSC_Units": 0}

        students[e_id]["Total_Units"] += units

        if course.startswith("CPSC"):
            students[e_id]["CPSC_Units"] += units

with open('outputfile.csv', mode='w', newline='') as file3:
   writer = csv.writer(file3, delimiter=',')
   writer.writerow(["ID", "Total Units", "CPSC Units"])

   for k, v in students.items():
        writer.writerow([k, v["Total_Units"], v["CPSC_Units"]])
