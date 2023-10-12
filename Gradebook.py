# Define last semester's gradebook as a list of tuples, where each tuple contains a subject and a score.
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# Create two lists, one for subjects and another for corresponding grades.
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Create a two-dimensional list called gradebook, where each sublist contains a subject and its corresponding grade.
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]

# Append a new subject ("Computer Science") and its grade (100) to the gradebook.
gradebook.append(["Computer Science", 100])

# Append another new subject ("Visual Arts") and its grade (93) to the gradebook.
gradebook.append(["Visual Arts", 93])

# Modify the last entry (Visual Arts) in the gradebook to change the grade from 93 to 98.
gradebook[-1][-1] = 98

# Remove the grade (85) for "Poetry" from the gradebook's sublist and replace it with "Pass".
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combine last semester's gradebook and the current gradebook to create a full gradebook.
full_gradebook = last_semester_gradebook + gradebook

# Print the full gradebook, which includes grades from last semester and the current semester.
print(full_gradebook)
