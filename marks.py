# Student Marks Calculator
# This file calculates the average marks of a student.

# Store marks in a list
marks = [85, 78, 92, 88, 76]

# Calculate the total marks
total_marks = sum(marks)

# Calculate the average marks
average_marks = total_marks / len(marks)

# Display the marks
print("Student Marks:", marks)

# Display the total marks
print("Total Marks:", total_marks)

# Display the average marks
print("Average Marks:", average_marks)

# Check whether the student passed
if average_marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
