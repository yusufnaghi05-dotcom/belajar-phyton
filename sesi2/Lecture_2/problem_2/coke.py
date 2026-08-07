total = 0

while total < 50:
    print(f"Amount Due: {50-total}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total = total + coin 
    
change_owed = total - 50
print(f"Change Owed: {change_owed}")