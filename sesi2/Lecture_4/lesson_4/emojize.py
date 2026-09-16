from emoji import emojize

def main():
    get_emoji()
    
def get_emoji():
    text = input("Input: ")
    new_text = emojize(text, language="alias")
    print(new_text)

main()