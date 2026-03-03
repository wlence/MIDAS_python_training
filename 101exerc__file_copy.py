# Exercise to copy a file from source to destination
source = "test.txt"
destination = "copy_test.txt"

with open(source, "r") as src_file:
    content = src_file.read()

with open(destination, "w") as dest_file:
    dest_file.write(content)

