
print("Writing data to file...")
file = open("student.txt", "w")     #  w  mode - creates or overwrites a file
file.write("Name: Siddhi\n")
file.write("Course: Python Programming\n")
file.write("Marks: 85\n")
file.close()
print("Data written successfully!\n")

# Step 2: Read and display data from file
print("Reading data from file...")
file = open("student.txt", "r")     # 'r' mode - reads data from the file
content = file.read()
print("File Content:\n----------------")
print(content)
file.close()

# Step 3: Append new data to the existing file
print("\nAppending more data to the same file...")
file = open("student.txt", "a")     # 'a' mode - appends data at the end of file
file.write("Result: Passed\n")
file.write("Grade: A\n")
file.close()
print("Data appended successfully!\n")

# Step 4: Read again to show final content
print("Reading final content of the file...")
file = open("student.txt", "r")
final_content = file.read()
print("Final File Content:\n---------------------")
print(final_content)
file.close()

print("\nProgram completed successfully!")
