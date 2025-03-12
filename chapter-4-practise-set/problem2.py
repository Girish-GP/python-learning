# write a program to accept marks of 6 students and display them in sorted order
marks = []
for i in range(6):
    student_mark = int(input(f"Enter marks for student {i+1}:"))
    marks.append(student_mark)
marks.sort()
print(f"Marks list in sorted order: {marks}")