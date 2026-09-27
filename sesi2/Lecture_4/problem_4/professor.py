import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        benar = False
        for _ in range(3):
            try:
                user_answer = int(input(f'{x} + {y} = '))
                if user_answer == x + y:
                    score = score + 1
                    benar = True
                    break
                else:
                    print('EEE')
                    continue
            except ValueError:
                print('EEE')
                continue
        if not benar:
            print(f"{x} + {y} = {x + y}")
    print(f'Score: {score}')
    
def get_level():
    while True:
        try:
            x = int(input('Level: '))
            if x == 1 or x == 2 or x == 3:
                return x
            else:
                raise ValueError
        except ValueError:
            continue
def generate_integer(tingkat):
    if tingkat == 1:
        rentang_angka = random.randint(0, 9)
    if tingkat == 2:
        rentang_angka = random.randint(10, 99)
    if tingkat == 3:
        rentang_angka = random.randint(100, 999)
    
    return rentang_angka

if __name__ == "__main__":
    main()