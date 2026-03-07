# Metodo de retiro
# Metodo de chequeo
# Agregar efectivo
# Bool de checking account
# Num entrada != negativo


class User:
    def __init__(self, name, balance = 0, checking_account = True, id = '0000001' ):
        self.name = name
        self.id = id
        self.balance = balance
        self.account = checking_account
        pass

    def check_balance(self):
        print(f"{self.name}: {self.balance}")

    def withdraw(self, extraction):
        if self.account == False:
            raise Exception("Account not activated")
        elif extraction < 0:
            raise Exception("That's ilegal!")
        else:
            if extraction > self.balance:
                raise Exception("Insufficient funds")
            else:
                self.balance -= extraction
                print(f"{self.name}, you have {self.balance} ")


    def check(self, receiver, amount):
        if self.account == False:
            raise Exception("Account not activated")
        elif amount < 0:
            raise Exception("That's ilegal!")
        else:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            else:
                self.balance -= amount
                receiver.add_cash(amount)
                print(f"{self.name}, you've sent {amount} to {receiver.name}")
                print(f"{self.name}, you still have {self.balance} ")
                print(f"{receiver.name}, you now have {receiver.balance} ")


    def add_cash(self, income):
        if self.account == False:
            raise Exception("Account not activated")
        else:
            self.balance += income
            print(f"{self.name}, you now have {self.balance}")



Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

Jeff.check_balance()
Joe.check_balance()

Jeff.withdraw(12) # Devuelve 'Jeff tiene 68.'

# Joe.check(Jeff, 50) # Devuelve 'Joe tiene 120 y Jeff tiene 18.'

# Jeff.check(Joe, 80) # Lanza un ValueError

# Joe.checking_account = True # Habilita la cuenta corriente para Joe

# Jeff.check(Joe, 80) # Devuelve 'Jeff tiene 98 y Joe tiene 40'

# Joe.check(Jeff, 100) # Lanza un ValueError

# Jeff.add_cash(20.00) # Devuelve 'Jeff tiene 118.'