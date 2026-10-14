def main():
    fraction = input()
    percentage = convert(fraction)
    print(gauge(percentage))
def convert(fraction):
    fraction_parts = fraction.split("/")
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    if denominator == 0:
            raise ZeroDivisionError
    if numerator < 0 or denominator < 0 or numerator > denominator:
        raise ValueError
    percentage = numerator / denominator * 100
    rounded_percentage = round(percentage)
    return rounded_percentage
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
if __name__ == "__main__":
    main()