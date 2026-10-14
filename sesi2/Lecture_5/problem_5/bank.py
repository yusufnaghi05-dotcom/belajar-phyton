def main():
    answer = input("Greeting: ").lower().strip()
    print(f'Value: {value(answer)}')


def value(answer):
    if answer.startswith("hello"):
        answer = 0
        return answer
    elif answer.startswith("h"):
        answer = 20
        return answer
    else:
        answer = 100
        return answer

if __name__ == "__main__":
    main()