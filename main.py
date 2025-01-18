def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount(file_contents)

def wordCount(file):
    words = file.split()
    print(len(words))

def characterCount(file):
    words = file.split()
    """Add a new function to your script that takes the text from the book as a string, 
    and returns the number of times each character appears in the string. 
    Convert any character to lowercase, we don't want duplicates."""

main()