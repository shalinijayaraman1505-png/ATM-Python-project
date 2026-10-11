
PIN = 2315


def Check_Pin():

    ATM_PIN = int(input("Enter your ATM PIN: "))

    if PIN == ATM_PIN:
        print("You have entered the correct PIN.")
        return True
    else:
        print("Incorrect PIN, try again.")
        return False


def ATM_Menu():

    while True:
        choice = input("Enter your choice: ")

        match choice:
            case "Deposit" | "D" | "deposit":
                deposit()

            case "Check Balance" | "CB" | "checkbalance":
                Check_balance()

            case "Withdraw" | "W" | "withdraw":
                withdraw()

            case "Exit" | "E" | "exit":
                print("Thank you for using the ATM!")
                break

            case _:
                print("Invalid choice")


balance = 5000


def deposit():

    global balance

    amount = int(input("Enter the deposit amount: "))

    balance = balance + amount

    print("Amount deposited:", amount)
    print("Your current balance:", balance)


def withdraw():

    global balance

    withdraw_amount = int(input("Enter the withdraw amount: "))

    if withdraw_amount > balance:
        print("Insufficient funds!")

    else:
        balance = balance - withdraw_amount

        print("Amount withdrawn:", withdraw_amount)
        print("Your current balance:", balance)



def Check_balance():

    print("Your current balance:", balance)


if Check_Pin():
    ATM_Menu()