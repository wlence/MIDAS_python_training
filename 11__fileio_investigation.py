# File input
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

fp = open("test.txt")
lines = fp.readlines()
for line in lines:
    print(line.strip())
fp.close()

# File output
with open("output.txt", "w") as file:
    file.write("This is a test.\n")
    file.write("This is only a test.\n")



