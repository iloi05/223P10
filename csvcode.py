import csv

counters = {"freshman": 0, "sophomore": 0, "junior": 0, "senior": 0}

students = {}

with open('Students.csv', mode='r') as file1, \
     open('course enrollment.csv', mode = 'r') as file2, \
     open('outputfile.csv', mode='w', newline='') as file3:
    s = csv.DictReader(file1)
    for row in s:
        level = row["Level"].strip()
        sid = row["ID"]

        if level == "FRESH":
            counters["freshman"] += 1
        elif level == "SOPH":
            counters["sophomore"] += 1
        elif level == "JR":
            counters["junior"] += 1
        elif level == "SR":
            counters["senior"] += 1

        students[sid] = {"Total_Units": 0, "CPSC_Units": 0}

    print(f'{counters["freshman"]} freshmen')
    print(f'{counters["sophomore"]} sophomores')
    print(f'{counters["junior"]} juniors')
    print(f'{counters["senior"]} seniors')

    e = csv.DictReader(file2)
    for row in e:
        e_id = row["ID"]
        course = row["Course"]
        units = int(row["Units"])
    
        if e_id in students:
            students[e_id]["Total_Units"] += units
            if course.startswith("CPSC"):
                students[e_id]["CPSC_Units"] += units
        else:
            students[e_id] = {
                "Total_Units": units,
                "CPSC_Units": units if course.startswith("CPSC") else 0
            }

    writer = csv.writer(file3)
    writer.writerow(["ID", "Total Units", "CPSC Units"])

    for sid, data in students.items():
        writer.writerow([sid, data["Total_Units"], data["CPSC_Units"]])