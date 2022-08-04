students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = [input()]
        students.insert(_, name)
        score = float(input())
        students[_].insert(1, score)

# sorting students in ascending order based on grades
sorted_list = sorted(students, key = lambda x: x[1])

#removing students with lowest grade
lowest_grade = sorted_list[0][1]
for i in range(len(sorted_list)):
    if sorted_list[0][1] == lowest_grade:
        sorted_list.pop(0)

# second lowest grade
second_lowest_grade = sorted_list[0][1]

# sorting and printing name of student(s) in alphabetical order having second lowest grade
if len(sorted_list) == 1:
    print(sorted_list[0][0])
else:
    for i in sorted(sorted_list):
        if i[1] == second_lowest_grade:
            print(i[0])
