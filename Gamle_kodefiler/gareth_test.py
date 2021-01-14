def __main__():


    fornavn = ask_navn("Whats your name?")
    etternavn = ask_navn("Whats your surname?")
    print(f"Hei" + ' ' + fornavn + ' ' + etternavn)


def ask_navn (message):
    while True:
        navn = input(message)
        if check_navn(navn):
            return navn
        else:
            print("Prøv igjen")


def check_navn(name):
    if name.isalpha():
        return True
    return False

