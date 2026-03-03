#usage: python word_count.py <filename>
import argparse

#Open the file and read its content
parser = argparse.ArgumentParser(description="Count the number of lines, words, and characters in a file.")
parser.add_argument("filename", help="The name of the file to count")
args = parser.parse_args()

try:
    with open(args.filename, "r") as f:
        content = f.read() #Read the entire file content as a string
        lines = content.splitlines() #Split the content into lines
        words = content.split() #Split the content into words
        characters = len(content) #Count the number of characters in the content
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")
except FileNotFoundError:
    print(f"File {args.filename} not found!")

if __name__ == "__main__":
    pass
