def main():
    word = input('Input: ')
    print(f'Output: {shorten(word)}')
def shorten(word):
    result = ''
    for x in word:
        if x.lower() not in 'aiueo':
            result = result + x 
    return result


if __name__ == "__main__":
    main()