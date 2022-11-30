_ = input()
no_of_students = int(_.split()[0])
total_subjects = int(_.split()[1])

marks_to_zip = []

# adding marks of all students of a particular subject
for i in range(total_subjects):
    temp_list = []
    temp_list.append(input().split())
    marks_to_zip += temp_list

# calculating total marks of each student and averaging them
for student_marks in zip(*marks_to_zip):
    total = 0
    for marks in student_marks:
        total += float(marks)
    print(total/total_subjects)
