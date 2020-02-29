# Written By Kody Carling
#
#

def intro():
# This function gives instuction to the User
    print()
    print("1. Please enter either Utah, Arizona, Texas, or Nevada for 'State'\n")
    print()
    print("2. Please enter your gross income")
    print()
    print("This program will calculate your net income.")
    print()
    print("*"*50)
    print()
    print()


def calculate(income, tax):
    fed_tax = income * .10
    tax_income = income * tax
    net_income = income - (tax_income + fed_tax)
    return net_income


def main():
    intro()

    states_tax = {"Utah": .06, "Arizona": .07, "Texas": .08, "Nevada": .03}

    income = float(input("Enter your goss income and please press enter :$ "))
    print()

    st = ''
    while not st:
        state = input("Enter your state, please press enter:  ")
        if state not in states_tax:
            print("Please enter a valid state")
        else:
            tax = states_tax[state]
            st = "a"
    print()
    net_income = calculate(income, tax)
    print("Your net income is $" + str(net_income))
    print()
    print()


if __name__ == '__main__':
    main()
