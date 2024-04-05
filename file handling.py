#heilliesantana
import os

# Creating file1.txt and writing content into it
with open('file1.txt', 'w') as file:
    file.write("File handling is an important part of any web application.")

# Reading content from file1.txt
with open('file1.txt', 'r') as file:
    content = file.read()
    print("Content from file1.txt:", content)

# Creating file2.txt
with open('file2.txt', 'w') as file:
    pass  # Creating an empty file

# Deleting file2.txt if it exists
if os.path.exists('file2.txt'):
    os.remove('file2.txt')
    print("file2.txt has been deleted.")
else:
    print("file2.txt does not exist.")

# Checking existence of both files
file1_exists = os.path.exists('file1.txt')
file2_exists = os.path.exists('file2.txt')

print("Does file1.txt exist?", file1_exists)
print("Does file2.txt exist?", file2_exists)
