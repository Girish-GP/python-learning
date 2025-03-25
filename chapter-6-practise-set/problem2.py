# Write a program to check whether a student is passed or failed if it requires a total of 40% and at least 33% in each subject to pass . Assume three subjects and take marks from the user as an input

studentObj = {
    'english':0,
    'maths': 0,
    'science': 0
}
totalMarksForEachSubject = int(input("enter the total marks for each subject:"))
for i in studentObj.keys():
    marks = int(input(f"Enter marks for {i}:"))
    studentObj[i]=marks
totalPercent = (sum(studentObj.values())/3*totalMarksForEachSubject)*100
subjectInwhichPercentisLessThan33 = False
for i in studentObj.values():
    temp = (i/totalMarksForEachSubject)*100
    if(temp < 33):
        subjectInwhichPercentisLessThan33 = True
    
if(totalPercent >= 40 and (not subjectInwhichPercentisLessThan33)):
    print("student passed")
else:
    print("student failed")


# check for optimized code
# # Function to get marks from the user
# def get_marks(subjects):
#     marks = []
#     total_marks_per_subject = int(input("Enter the total marks for each subject: "))
    
#     for subject in subjects:
#         while True:
#             try:
#                 mark = int(input(f"Enter marks for {subject}: "))
#                 # Input validation
#                 if 0 <= mark <= total_marks_per_subject:
#                     marks.append(mark)
#                     break
#                 else:
#                     print(f"Invalid marks! Marks should be between 0 and {total_marks_per_subject}. Try again.")
#             except ValueError:
#                 print("Please enter a valid integer.")
#     return marks, total_marks_per_subject

# # Function to calculate total percentage
# def calculate_total_percentage(marks, total_marks_per_subject, num_subjects):
#     total_marks_obtained = sum(marks)
#     total_possible_marks = total_marks_per_subject * num_subjects
#     return (total_marks_obtained / total_possible_marks) * 100

# # Function to check if the student passed in each subject
# def check_subject_pass(marks, total_marks_per_subject):
#     for mark in marks:
#         if (mark / total_marks_per_subject) * 100 < 33:
#             return False
#     return True

# # Main function to determine if the student passed or failed
# def main():
#     subjects = ['English', 'Maths', 'Science']
    
#     # Step 1: Get marks from the user
#     marks, total_marks_per_subject = get_marks(subjects)
    
#     # Step 2: Calculate total percentage
#     total_percentage = calculate_total_percentage(marks, total_marks_per_subject, len(subjects))
    
#     # Step 3: Check subject-wise pass condition
#     if total_percentage >= 40 and check_subject_pass(marks, total_marks_per_subject):
#         print("Student passed")
#     else:
#         print("Student failed")

# # Call the main function to run the program
# main()
