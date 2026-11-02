import re
import sys

def main():
    print(convert(input("Hours: ")))
def convert(s):
    matches = re.search(r"^(\d+)(:[0-5]\d)? (AM|PM) to (\d+)(:[0-5]\d)? (AM|PM)$", s)
    if matches:
        first_hour = int(matches.group(1))
        if first_hour > 12 or first_hour <= 0:
            raise ValueError
        first_minute = matches.group(2)
        if first_minute is None:
            first_minute = ":00"
        new_first_minute = int(first_minute[1:])
        first_time = matches.group(3)
        second_hour = int(matches.group(4))
        if second_hour > 12 or second_hour <= 0:
            raise ValueError
        second_minute = matches.group(5)
        if second_minute is None:
            second_minute = ":00"
        new_second_minute = int(second_minute[1:])
        second_time = matches.group(6)
        
        if first_hour == 12 and (first_time == "AM"):
            first_hour = 00
        if first_hour != 12 and first_time == "PM":
            first_hour = first_hour + 12
        if second_hour == 12 and (second_time == "AM"):
            second_hour = 00
        if second_hour != 12 and second_time == "PM":
            second_hour = second_hour + 12
        return f"{first_hour:02}:{new_first_minute:02} to {second_hour:02}:{new_second_minute:02}"
    else:
        raise ValueError
if __name__ == "__main__":
    main()