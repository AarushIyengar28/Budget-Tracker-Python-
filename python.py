from datetime import datetime
import json
import matplotlib.pyplot as plt

def save_budget_details(initial_budget, expenses):
   
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"budget_data_{timestamp}.json"  # New file each time you exit with the date

    data = {
        'initial_budget': initial_budget,
        'expenses': expenses,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data saved to {filepath}")


def add_expenses(expenses, description, amount):
    expenses.append({'Description': description, 'Amount': amount})
    print(f'Description: {description}, Amount: {amount}')

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['Amount']
    #did amount without cap so it can't acsess the expenses amount because the key was wrong
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)
    

def budget_details(budget, expenses):
    print(f'Total Budget: {budget}') 
    print('Expenses:')
    for expense in expenses:
        print(f'- {expense["Description"]}: {expense["Amount"]}')
    print(f'Remaining Budget: {get_balance(budget, expenses)}')
    print(f'Total Spent: {get_total_expenses(expenses)}')
        

    debt = get_balance(budget, expenses)
    if debt < 0:
        print('You are in debt. STOP SPENDING SO MUCH!')
    
            

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']# you did initial budget instead of initial_budget so it is same key error as last time
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
    
    
def get_monthly_expenses(expenses):
    descriptions = [expense['Description'] for expense in expenses]
    amounts = [expense['Amount'] for expense in expenses]
    plt.figure(figsize=(10,6))
    plt.bar(descriptions, amounts, color = 'skyblue')

    plt.xlabel("Descriptions of expenses")
    plt.ylabel("Amount of expenses")

    plt.xticks(rotation = 45, ha = 'right')

    plt.tight_layout()
    plt.show()

    
def budgettracking():
    print('Welcome to the budgeting app!')
    initial_budget = float(input('What is your initial budget?: ')) # did this twice so that is why it ran twice
    filepath = 'budget_data.json'
    # inital_budget, expenses = load_budget_data(filepath)
    if initial_budget <= 0:
        print('Your initial budget has to be over $0')
    #     initial_budget = float(input('What is your initial budget?: '))
    budget = initial_budget
    expenses =[]
    while True:
        print('\n What would you like to do?')
        print('1. Add an expense')
        print('2. View budget details')
        print('3. Exit the Budget App')
        choice = input('What do you want to do?(1/2/3): ')
        #this takes user choice and displays their choice
        if choice == '1':
            description = input('What is the description of your expense?: ')
            amount = float(input('What is the amount of your expense?: '))
            add_expenses(expenses, description, amount)
        elif choice == '2':
            budget_details(budget, expenses)
        elif choice == '3':
            summary = input("Do you want a summary of your expenses(yes or no): ").lower()
            if summary == 'yes':
                month_or_year = input("Do you want a monthly or yearly summary?: ").lower()
                if month_or_year == 'monthly':
                    get_monthly_expenses(expenses)
                    exit = input("Do you want to exit now?: ").lower()
                    if exit == 'yes':
                        save_budget_details(initial_budget, expenses)#make sure your syntax is correct you put in a < instead of a ,
                        print('Exiting the Budget App. Goodbye.')
            #forgot to use a break. just remember to end the loop
                        break
            if summary == 'no':
                save_budget_details(initial_budget, expenses)#make sure your syntax is correct you put in a < instead of a ,
                print('Exiting the Budget App. Goodbye.')
            #forgot to use a break. just remember to end the loop
                break
            
        else:
            print('Invalid Choice. Try Again')

if __name__ == '__main__':
    budgettracking()
