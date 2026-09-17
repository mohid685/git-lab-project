# Store updated marks after adding a new result
marks = [85, 78, 92, 88, 76, 90]

# Calculate the total marks
total_marks = sum(marks)

# Calculate the average marks
average_marks = total_marks / len(marks)

# Display the updated marks
print("Updated Marks:", marks)

# Display the total marks
print("Total Marks:", total_marks)

# Display the average marks
print("Average Marks:", average_marks)

# Check whether the student passed
if average_marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
