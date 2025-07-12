class Bank_account:
  def __init__(self,balance):
    self.__balance = balance
  
  def deposit(self,amount):
    if amount > 0:
      self.__balance += amount

  def withdraw(self,amount):
    if amount > 0:
      self.__balance -= amount
  
  def get_balance(self):
    return self.__balance

details = Bank_account(1000)
print(details.get_balance())
details.deposit(500)
print(details.get_balance())
details.withdraw(250)
print(details.get_balance())