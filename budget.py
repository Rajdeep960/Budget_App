
class Category:

    # constructor
    def __init__(self, name ):
        # instance variable
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        headline = self.name.center(30, "*")
        outputString = headline
        total = 0
        for i in self.ledger:
            description = i["description"]
            amount = "{:0.2f}".format(i["amount"])
            newString = f"{description[0:23]:23}{amount:>7}"
            outputString = outputString + "\n" + newString
            total = total + i["amount"]
        outputString = outputString + "\n" + "Total: " + str(total)
        return outputString
    

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        funds = 0
        for i in self.ledger:
            funds = funds + i["amount"]
        return funds

    def transfer(self, amount, another_budget_category ):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + another_budget_category.name)
            another_budget_category.deposit(amount, "Transfer from " + self.name)
            return True
        else :
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else :
            return True

    def total_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        return total



def create_spend_chart(category):

  # round number to multipale of 10
  def round_down(num):
    return num - (num%10)

  withdrawals_list= [a.total_withdrawals() for a in category]
  
  # sum of all category total withdrawals  
  total_withdrawals = 0
  for item in withdrawals_list:
    total_withdrawals += item

  categoryPercentageList = []
  for value in withdrawals_list:
    percentage = (value / total_withdrawals)*100
    # round percentage multipale of 10
    roundPercentage = round_down(percentage)
    categoryPercentageList.append(roundPercentage)


  # for chart part: 
  result = "Percentage spent by category\n"
  line = "    " + "".join(["-" for i in range(len(category) * 3 + 1)])
  bar = ""
  for i in range(100, -1, -10):
    if i == 100:
      bar = "100| "
    elif i == 0:
      bar = "  0| "
    else :
      bar = " " + str(i) + "| "

    for item in categoryPercentageList:
      if i <= item:
        bar += "o  "
      else:
        bar += "   "
    result += bar + "\n"  
  result += line + "\n"

  # for name printing : 
  greatest_name_length = 0
  for i in category:
    if len(i.name) > greatest_name_length:
      greatest_name_length = len(i.name)
  for i in range(greatest_name_length):
    result += "    "
    for c in category:
      if i < len(c.name):
        result += " " + c.name[i] + " "
      else:
        result += "   "
    if i == greatest_name_length - 1:
      result += " "
    else:
      result += " \n"


  return result  