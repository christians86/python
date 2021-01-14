########Test av funksjonaliten:###############
# printf("hello, world\n");
# string
# name = get_string("What is your name?\n");
# printf("hello, %s\n", name);
# while True:
# navn = input("Whats your n
# if navn.isalpha():
# return navn
# else:
# print("Vennligst skrivnavn = input("Whats your name?")
# print(f"Hello {navn}")
###########################Gammel kode
# def ask_fornavn():
#    while True:
#        fornavnnavn = input("Whats your name?")
#        if fornavnnavn.isalpha():
#            return fornavnnavn
#        else:
#            print("Prøv igjen")

# def ask_etternavn():
#    while True:
#        etternavn = input("Whats your sur name?")
#        if etternavn.isalpha():
#            return etternavn
#        else:
#            print("Prøv igjen")


###########################Gammel kode

def ask_fornavn(message):
    fornavnnavn = input("Whats your name?")



def ask_etternavn():
    etternavn = input("Whats your sur name?")


class sjekk:
    def __init__(self,navn,etternavn):
        self.navn = ask_fornavn()
        self.etternavn = ask_etternavn()

    def check_value(self):
        while True:
            self = input()
        if var_car.isalpha():
            return var_car
        else:
            print("Try again")


print(f"Hei" + ' ' + ask_fornavn() + ' ' + ask_etternavn())
