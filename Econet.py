balance = 50.0
print("--- Welcome to EcoCash ---")
print("1. Buy Airtime")
print("2. Buy Data")
print("3. Check Balance")
print("4. Exit")

choice = input("Enter choice (1-4): ")

if choice == "1":
    amount = float(input("Enter airtime amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Success! You bought $" + str(amount) + " airtime.")
        print("New balance is: $" + str(balance))
    else:
        print("Insufficient funds! You only have $" + str(balance))

elif choice == "2":
    print("Select Data Bundle:")
    print("1. 100MB ($1)")
    print("2. 500MB ($3)")
    print("3. 1GB ($5)")
    
    bundle_choice = input("Enter bundle choice: ")
    
    if bundle_choice == "1":
        cost = 1
    elif bundle_choice == "2":
        cost = 3
    elif bundle_choice == "3":
        cost = 5
    else:
        cost = 0
        print("Invalid bundle selection.")

    if cost > 0:
        if balance >= cost:
            balance = balance - cost
            print("Data purchase successful!")
            print("Remaining balance: $" + str(balance))
        else:
            print("Not enough money for this bundle.")

elif choice == "3":
    print("Your current balance is: $" + str(balance))

elif choice == "4":
    print("Thank you for using EcoCash. Goodbye!")

else:
    print("Invalid option selected. Please try again.")