import re
import sys
def main():
    print(count(input("Text: ")))
def count(s):
    word = re.findall(r"\bum\b", s, re.IGNORECASE)
    word_count = len(word)
    if word_count == 0:
        return 0
    return word_count
if __name__ == "__main__":
    main()