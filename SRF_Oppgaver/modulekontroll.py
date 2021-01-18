class kontroll:
  def __init__(self, fornavn, etternavn):
    self.name = fornavn
    self.namesur = etternavn

  def ask_fornavn(self):
      while True:
          brukerinput = input("Whats your name?")
          if brukerinput.isalpha():
              return brukerinput
          else:
              print("Prøv igjen")

  def ask_etterfornavn(self):
      while True:
          brukerinput = input("Whats your name?")
          if brukerinput.isalpha():
              return brukerinput
          else:
              print("Prøv igjen")

