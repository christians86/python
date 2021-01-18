def ask_fornavn():
    while True:
        fornavnnavn = input("Whats your name?")
        if fornavnnavn.isalpha():
            return fornavnnavn
        else:
            print("Prøv igjen")


def ask_etternavn():
    while True:
        etternavn = input("Whats your sur name?")
        if etternavn.isalpha():
            return etternavn
        else:
            print("Prøv igjen")


print(f"Hei" + ' ' + ask_fornavn() + ' ' + ask_etternavn())