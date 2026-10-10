class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
    def get_balance(self):
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        return False
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
    def check_funds(self,amount):
        if amount <=self.get_balance():
            return True
        return False
    def __str__(self):
        title=f"{self.name:*^30}\n"
        output=title + "\n"
        for item in self.ledger:
            description=item["description"][:23]
            amount=f"{item['amount']:.2f}"
            output+=f"{description:<23}{amount:>7}\n"
        output+=f"Total: {self.get_balance()}"
        return output
def create_spend_chart(categories):
    spent=[]
    for category in categories:
        total=0
        for item in category.ledger:
            if item["amount"]<0:
                total+=-item["amount"]
        spent.append(total)
    total_spent=sum(spent)
    percentages=[]
    for amount in spent:
        percentage = amount/total_spent * 100
        percentages.append(percentage)
    levels=list(range(100,-1,-10))
    chart=""
    for level in levels:
        chart+=f"{level:>3}|"
        for percentage in percentages:
            if percentage>=level:
                chart+=" o "
            else:
                chart+="    "
        chart+=" \n"
    max_length=max(len(category.name) for category in categories)
    for i in range(max_length):
        chart+="    "
        for category in categories:
            if i < len(category.name):
                chart+=category.name[i]+"    "
            else:
                chart+= "    "
        chart +="\n"
    chart+="    "+"-" * (len(categories)* 3+1) + "\n"

    return chart

food=Category("Food")
entertainment=Category("Entertainment")
clothing=Category("Clothing")
food.deposit(1000,"initial deposit")
food.withdraw(500,"groceries")
clothing.deposit(1000,"initial deposit")
clothing.withdraw(200,"clothes")
entertainment.deposit(1000,"initial deposit")
entertainment.withdraw(400,"movies")
print(create_spend_chart([food,entertainment,clothing]))