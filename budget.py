# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

# For public execution and test
# https://replit.com/@ToniG4/boilerplate-budget-app


class Category :

    def __init__(self, name) :

        self.name = name
        self.ledger = list()
        self._balance = 0
    

    def __str__(self) :

        header = self.name.center(30, "*") + "\n"

        body = ""
        for entry in self.ledger :
            
            # 30 characters per line: 23 for the description, 7 for the amount (including 2 decimals)
            description = "{:<23}".format( entry["description"] )
            amount = "{:>7.2f}".format( entry["amount"] )
            
            body += "{}{}\n".format( description[:23], amount[:7] )

        footer = "Total: {:.2f}".format(self._balance)

        return header + body + footer


    def deposit(self, amount, description = "") :

        self.ledger.append( {"amount" : amount, "description" : description} )
        self._balance += amount
    

    def withdraw(self, amount, description = "") :
        
        if self.check_funds(amount) :
            
            self.ledger.append( {"amount" : -1 * amount, "description" : description} )
            self._balance -= amount

            return True

        else :
            return False
    

    def get_balance(self) :

        return self._balance
    

    def transfer(self, amount, destination) :

        if self.check_funds(amount) :
            
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        
        else :
            return False
    

    def check_funds(self, amount) :
        
        if amount > self._balance : return False
        else : return True


def create_spend_chart(categories) :

    category_names = []
    spend_by_category = []
    pct_by_category = []

    # Get each category name and its spend
    for category in categories :

        category_names.append(category.name)

        category_spend = 0
        for entry in category.ledger :
            if entry["amount"] < 0 : category_spend += abs(entry["amount"])
        
        spend_by_category.append(round(category_spend, 2))

    # Get the % spend for each category (rounded down to the nearest 10)
    total_spend = sum(spend_by_category)

    for spend in spend_by_category :
        pct_by_category.append( ( ( (spend/total_spend) * 10 ) // 1 ) * 10 )

    #
    n_categories = len(categories)
    max_len_category = max( [ len(x) for x in category_names ] )

    #
    y_axis = list( reversed( list( range(0, 101, 10) ) ) )

    # Print chart title
    output = "Percentage spent by category\n"

    # Print the y axis with values from 100 to 0
    for y_value in y_axis :

        output = output + "{:>3}".format( str(y_value) ) + "|"

        # Print "o" to fill the bar of the chart
        for pct in pct_by_category :
            if pct >= y_value : output += "o".center(3, " ")
            else : output += "   "

        output += " \n"

    # Print the x axis (dashes and category names)
    output = output + "    "  + ( "-" * (3 * n_categories + 1) ) + "\n"
    
    i = 0
    while i < max_len_category :

        output = output + "    "
        
        # Get the character at the i position for each category
        for category in category_names :
            try : output += category[i].center(3, " ")
            except : output += "   "
        
        # Check whether the last character has been printed
        if i + 1 == max_len_category : output += " "
        else : output += " \n"
        
        i += 1


    return output



# Example execution and tests

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

#food.deposit(900, "deposit")
#print(food.ledger[0])
#food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#print(food.ledger[1])
#print(food.check_funds(1000))
#print(food.get_balance())



#print(food.ledger)
#print(repr(food))
#print(str(food))


#food.deposit(45.56)
#print(food.ledger[0])


#food.deposit(900, "deposit")
#food.withdraw(45.67)
#print(food.ledger[1])


#food.deposit(900, "deposit")
#food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#transfer_amount = 20
#foodbalance_before = food.get_balance()
#entertainmentbalance_before = entertainment.get_balance()
#print('Food balance before:' + str(foodbalance_before), 'Entertainment balance before:', str(entertainmentbalance_before))
#good_transfer = food.transfer(transfer_amount, entertainment)
#print(good_transfer)
#foodbalance_after = food.get_balance()
#entertainmentbalance_after = entertainment.get_balance()
#print('Food balance after:' + str(foodbalance_after), 'Entertainment balance after:', str(entertainmentbalance_after))
#print('----')
#print(food.ledger)
#print(entertainment.ledger)


#food.deposit(100, "deposit")
#foodbalance_before = food.get_balance()
#entertainmentbalance_before = entertainment.get_balance()
#print('Food balance before:' + str(foodbalance_before), 'Entertainment balance before:', str(entertainmentbalance_before))
#food.transfer(200, entertainment)
#foodbalance_after = food.get_balance()
#entertainmentbalance_after = entertainment.get_balance()
#print('Food balance after:' + str(foodbalance_after), 'Entertainment balance after:', str(entertainmentbalance_after))


#food.deposit(900, "deposit")
#food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#food.transfer(20, entertainment)
#print(food.ledger)
#print(food.get_balance())


#food.deposit(900, "deposit")
#food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#food.transfer(20, entertainment)
#print(str(food))


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(str(food), '\n')

output = create_spend_chart([business, food, entertainment])
print( output )
