def main():
    get_date()
def get_date():
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                new_data1 = date.split("/")
                if len(new_data1) != 3 :
                    continue
                x_month = new_data1[0]
                x_day = new_data1[1]
                x_year = int(new_data1[2])
                new_month = int(x_month)
                new_day = int(x_day)
                if not 1000 <= x_year <= 9999:
                    continue
                if not (1 <= new_month <= 12 and 1 <= new_day <= 31):
                        continue
                print(f"{x_year}-{new_month:02d}-{new_day:02d}")
                break
            
            else:
                new_data2 = date.split()
                if len(new_data2) != 3 :
                    continue
                y_month = new_data2[0]
                y_day = new_data2[1]
                y_year = int(new_data2[2])
                if not y_day.endswith(","):
                    continue
                yz_day = y_day.rstrip(",")
                new_day = int(yz_day)
                if y_month not in month:
                    continue
                if not 1000 <= y_year <= 9999:
                    continue
                if not (1 <= new_day <= 31):
                    continue
                print(f"{y_year}-{month[y_month]:02d}-{new_day:02d}")
                break
        except IndexError:
            continue
        except ValueError:
            continue
        
main()