def ask_name(message):
    while True:
        name = input(message)
        if check_name(name):
            return name
        else:
            print("Try again please...")
def check_name(name):
    if name.isalpha():
        return True
    return False
firstname = ask_name("Whats your name? ")
surname = ask_name("Whats your surname? ")

