class bank_account:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.amount = int(input("Enter your deposit: "))

    def display(self):
        print("Thanks for Opening Account in Our Bank", self.name)


dhanusya = bank_account()
dhanusya.display()
print(dhanusya.name)
print(dhanusya.age)


