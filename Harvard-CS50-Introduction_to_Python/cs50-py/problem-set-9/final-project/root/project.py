
#libraries

import re
import sys
import matplotlib.pyplot as plt
import csv

#-----------------------------------------------------------------

#classes

class Expense:
    def __init__(self, amount, category, description, regularity):
        self.amount = amount
        self.category = category
        self.description = description
        self.regularity = regularity

    def __str__(self):
        return f"Expense with amount={self.amount}, category={self.category}, description={self.description}, regularity={self.regularity} created.\n"

    def __repr__(self):     #python by default calls __repr__ not __str__ for printing objects out of a list
        return self.__str__()

#-------------------------------------------------------------------

def main():
    name = input('Please provide your first name and last name seperated by an "/": ' )

    firstname, lastname = name_check(name)

    while True: #to always start out at menu after triggering and transversing an option
        print("----------------------------------")
        print("----------------------------------")
        option = menu(firstname,lastname)
        option_verified = pick_option(option)
        trigger_option(option_verified)




#-------------------------------------------------------------------------
#further functions

def name_check(s):
    #check name
    if len(s) > 100:
        sys.exit("name too long")

    if not re.search(r"^[A-Za-z ]+/[A-Za-z ]+$",s):
        raise ValueError ("invalid name")

    else:
        firstname, lastname = s.split("/")
        firstname = firstname.strip()
        lastname = lastname.strip()
        return firstname, lastname

#----------------------------------------

def menu(firstname, lastname):
    #greet user, show possible option and let them pick one

    print (f"Hello {firstname} {lastname}")
    print()
    print("Please pick an option from the menu")
    print("-----------------------------------")
    print("create expense - type 1")
    print("remove expense - type 2")
    print("list and sort expenses - type 3")
    print("summed expenses for daily, weekly, monthly, yearly - type 4")
    print("create visualization of all expenses - type 5")
    print("export stats to csv - type 6")
    print("end application - type 9")

    option = (input("option: "))
    return option


def pick_option(option):
    #only let user continue if valid option choosen
    options = [1, 2, 3, 4, 5, 6, 9]

    while True:
        try:    #allow only valid options
            option = int(option)
            if option in options:
                return option
            else:
                raise ValueError
        except ValueError:
            option = (input("please provide a valid option: "))

#--------------------

expenses = []

def add_expense(expense):
    expenses.append(expense)
    print(f"\n{expense}")

#------------------

#trigger options

def trigger_option(option):
    #trigger specific function from menu
    if option == 1:
        new_expense()

    if option == 2:
        rm_expense(expenses)

    if option == 3:
        def_lists(expenses)

    if option == 4:
        prototype_expenses(expenses)

    if option == 5:
        visualize_expenses(expenses)

    if option == 6:
        export_csv(expenses)

    if option == 9:
        end_program()

#------------------------------------------------------
#functions for triggered options above

#add expense and constraint valid inputs (length and input types)
def new_expense():
    print("\nFor every parameter please use uniform values so they can be sorted accordingly afterwards.")

    while True:
        amount = input("\nWhich amount?(only whole numbers): ")
        if len(amount) > 20:
            print("number too long")
            continue

        try:
            amount = int(amount)
            break
        except ValueError:
            print("please provide valid amount")

    while True:
        category = input("\nWhich category?(e.g. hair dresser, bar, fitness studio): ")
        if len(category) > 100:
            print("please use smaller category")
        else:
            break

    while True:
        description = input("\nWhich description? ")
        if len(description) > 200:
            print("please use smaller description")
        else:
            break

    regularities = ["daily", "weekly", "monthly", "yearly"]

    while True:
        regularity = input("\nWhich regularity of payment?(daily, weekly, monthly, yearly): ")
        if regularity in regularities:
            break
        else:
            print("please provide valid regularity")


    new_expense = Expense(amount, category, description, regularity)    #can be used, cause all instances are appended to the list immediately after (gets overwritten everytime)
    add_expense(new_expense)


#remove expense

 # list all expenses with values and index with loop
def rm_expense(expenses):

    print(f"\nexpenses total: {len(expenses)}\n")

    for i, expense in enumerate(expenses):
        print(f"\n{i+1}, {expense}")

    while True:
        #pick expense
        if len(expenses) == 0:
            print("no expenses")
            break

        try:
            choice = input("Select number of expense that should be deleted or type 'menu' to go back to menu: " )

            if choice == "menu":
                break

            choice = int(choice)

            #delete expense
            if 1 <= choice <= len(expenses):
                choice -= 1
                expenses.remove(expenses[choice])
                print("expense removed")
                break

        except ValueError:
            print("invalid choice, returning back to menu")
            break


#list and sort expenses

#list all expenses and make it able to sort them by amount, category or regularity (if list is empty and you sort by parameter, just returns to the menu)
def def_lists(expenses):
    for i, expense in enumerate(expenses):
        print("")
        print(i+1, expense)

    while True:
        #pick and process parameter
        parameter = input("\nSelect a parameter (amount, category, regularity) to group by or type menu to return to the menu: ")

        if parameter == "menu":
                break

        #sort by parameters (A-Z or small-big)
        elif parameter == "amount":
            amount_sorted = sorted(expenses, key=lambda expense : int(expense.amount))  #sort list by specific key inside every expense instance (here: expense.amount)
            for amount in amount_sorted:    #instead of just printing to line list them up line by line
                print(amount)
            break

        elif parameter == "category":
            category_sorted = sorted(expenses, key=lambda expense : expense.category)
            for category in category_sorted:
                print(category)
            break

        elif parameter == "regularity":
            regularity_sorted = sorted(expenses, key=lambda expense : expense.regularity)
            for regular in regularity_sorted:
                print(regular)
            break

        else:
            print("invalid input")


#create a spending prototype amount of daily/weekly/monthly/yearly expenses based on given expenses
def prototype_expenses(expenses):

    while True:
        period = input("\nFor which period of time you want to get an approximate value based on your current expenses? (daily, weekly, monthly, yearly).\nType menu to return to the menu: ")

        if period == "menu":
            break

        #build parts for equations
        daily = sum(int(expense.amount) for expense in expenses if expense.regularity == "daily")
        weekly = sum(int(expense.amount) for expense in expenses if expense.regularity == "weekly")
        monthly = sum(int(expense.amount) for expense in expenses if expense.regularity == "monthly")
        yearly = sum(int(expense.amount) for expense in expenses if expense.regularity == "yearly")

        #compute use cases
        if period == "daily":
            daily_amount = round(daily + (weekly / 7) + (monthly / 30) + (yearly / 365))
            print(f"\nYour daily expenses are approximately: {daily_amount}")
            break

        elif period == "weekly":
            weekly_amount = round((daily * 7) + weekly + (monthly / 4) + (yearly / 52))
            print(f"\nYour weekly expenses are approximately: {weekly_amount}")
            break

        elif period == "monthly":
            monthly_amount = round((daily * 31) + (weekly * 4) + monthly + (yearly / 12))
            print(f"\nYour monthly expenses are approximately: {monthly_amount}")
            break

        elif period == "yearly":
            yearly_amount = round((daily * 365) + (weekly * 52) + (monthly * 12) + yearly)
            print(f"\nYour yearly expenses are approximately: {yearly_amount}")
            break

        else:
            print("invalid time period")



#create visualization of your current expenses (empty chart if there are no expenses)
def visualize_expenses(expenses):

    ##-->sample: expense(amount, category, description, regularity)

    ###amount (show summed amounts for each specific category)
    category_totals = {}

    for expense in expenses:
        amount = int(expense.amount)

        #if category already exists --> sum up
        if expense.category in category_totals:
            category_totals[expense.category] += amount
        #if category doesn't exist --> create new entry in dict
        else:
            category_totals[expense.category] = amount

    #extract values to use them for plot
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    #plot values
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="skyblue")
    plt.title("Summed Amounts by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # save the plot as a png-file
    plt.savefig("amount-by-category.png")
    plt.close()


    ###category (bar chart --> how many expenses for each category)
    category_counts = {}

    for expense in expenses:

        #add 1 to existing entry (value)
        if expense.category in category_counts:
            category_counts[expense.category] += 1

        #create new entry and set value to 1
        else:
            category_counts[expense.category] = 1

    #extract values to use for axes in plot
    categories = list(category_counts.keys())
    amounts = list(category_counts.values())

    #plot values
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="skyblue")
    plt.title("Number of Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Number")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # save the plot as a png-file
    plt.savefig("number-by-category.png")
    plt.close()


    ###regularity (pie chart --> show regularities of expenses in pie chart)
    regularity_counts = {}

    for expense in expenses:

        #add 1 to existing entry (value)
        if expense.regularity in regularity_counts:
            regularity_counts[expense.regularity] += 1

        #create new entry and set value to 1
        else:
            regularity_counts[expense.regularity] = 1

    #extract values to use for axes in plot
    regularities = list(regularity_counts.keys())
    counts = list(regularity_counts.values())

    plt.figure(figsize=(6, 6))
    #autopct = accuracy of values displayed (e.g. %1.1f%% --> one digit at least before and one at most after decimal point), startangle= start of pie-chart, colors=color map
    plt.pie(counts, labels=regularities, autopct="%1.1f%%", startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Occurrences of Expenses by Regularity")
    plt.tight_layout()

    #save plot as png-file
    plt.savefig("regularity-of-expenses.png")
    plt.close()


#export csv
def export_csv(expenses, filename = "expenses.csv"):

    #set headers
    fieldnames = ["amount", "category", "description", "regularity"]

    #create file and append to it
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for expense in expenses:
            writer.writerow({
                "amount": expense.amount,
                "category": expense.category,
                "description": expense.description,
                "regularity": expense.regularity
            })


#end program
def end_program():

    while True:
        choice = input("\nAre you sure you want to exit the program? Have you exported or visualized your files?(yes, no): ")
        if choice == "no":
            break
        elif choice == "yes":
            sys.exit("\nProgram successfully terminated.\n")

        else:
            print("invalid input")






if __name__ == "__main__":
    main()
