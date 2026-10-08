Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Category:
    def  __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit (self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description  

        })
    def withdraw (self, amount, description= ''):
        if self.check_funds(amount):
           self.ledger.append({
            'amount': -amount,
            'description': description

           })
           return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True 
    
    def transfer(self, amount, other_category):
        if  self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__ (self):
        title = self.name.center(30,'*')
        result = title+'\n'

        for item in self.ledger:
            description = item[ 'description'] [:23]
            amount = f"{item['amount']:.2f}".rjust(7)
            result += description.ljust(23) + amount + '\n'

        result += f"Total: {self.get_balance():.2f}"
        return result



def create_spend_chart(categories):
    total_spend = 0
    spending = []

    for category in categories:
        category_spend = 0
        for item in category.ledger:
            if item['amount'] < 0:
                category_spend += -item['amount']
... 
...         spending.append(category_spend)
...         total_spend += category_spend
... 
...     percentages = []
... 
...     for amount in spending:
...         percentage = int((amount/total_spend) * 100 )
...         percentage = percentage // 10 * 10
...         percentages.append (percentage)
... 
...     chart = 'Percentage spent by category\n'
... 
...     for level in range (100,-1,-10):
...         chart += f"{level:>3}|"
... 
...         for percentage in percentages:
...             if percentage >= level:
...                 chart += " o "
...             else:
...                 chart += "   "
... 
...         chart += " \n"
... 
...     chart += "    " + "-" * (len(categories) * 3+1) + "\n"
...     max_length = max(len(category.name) for category in categories)
...     for i in range(max_length):
...         chart += "     "
... 
...         for category in categories:
...             if i < len(category.name):
...                 chart += category.name[i] + "  "
...             else:
...                 chart += "   "
...         
...         if i < max_length -1:
...             chart += "\n"
... 
...     return chart
