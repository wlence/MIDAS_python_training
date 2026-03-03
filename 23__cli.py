# Command line interface (CLI) investigation
import sys

print(sys.argv)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        content = f.readlines()
        print(f"There are {len(content)} lines in the file {filename}")
except FileNotFoundError:
    print(f"File {filename} not found!")
#except Exception as e:
#    print(f"An error occurred: {e}")



