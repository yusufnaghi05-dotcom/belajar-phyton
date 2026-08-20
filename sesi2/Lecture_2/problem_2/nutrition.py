def main():
    fruit = input("Item: ").lower()
    if calories(fruit):
        print(f"Calories: {calories(fruit)}")
    else:
        pass
        
def calories(x):
    data = {
        "apple": 130,
        "banana": 110,
        "avocado": 50,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        
    }
    
    
    
main()