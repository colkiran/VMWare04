
def bank_flow(fnc):         #HOF

    def helper(amt):
        print("-" * 40)
        print("Logging into the system........")
        print(fnc(amt))                   # callback
        print("Logging out of the system.......")
        print("-" * 40)

    return helper

@bank_flow
def deposit(amt):
    return f"{amt} credited into the account successfully....."

@bank_flow
def withdraw(amt):
    return f"{amt} debited from the account....."

@bank_flow
def trasfer(amt):
    return f"{amt} transfered from the account......."

deposit(45000)
withdraw(5000)
trasfer(15000)