def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        checker(file_contents)

def checker(file):
    words = file.split()
    print(len(words))
main()