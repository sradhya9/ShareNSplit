#Total amount spent for the whole trip by the members
def total(name_dict):
    d=name_dict.values()
    t=sum(d)
    return t

def share():
    name_list=[]
    num_name=int(input("Enter the total number of people :"))
    for i in range(num_name):
        nme=input("Enter the name: ")
        name_list.append(nme)
    print()
    total_spent={}
    for i in range(len(name_list)):
        total_spent[name_list[i]]=0.0
    balance={}
    for i in range(len(name_list)):
        balance[name_list[i]]=0.0
    #print(balance)
    stops(name_list,total_spent,balance)
    

def stops(name_list,total_spent,balance):
    #Total no of
    stop_dict={}
    num_stop=int(input("Enter the total number of stops :"))
    print()
    for i in range(num_stop):
        tot=float(input(f"Enter the amount spent at stop {i+1} : "))
        stop_dict[i]=tot
    #print(stop_dict)
    stp(num_stop,name_list,total_spent,stop_dict,balance)

def stp(num_stop, name_list, total_spent,stop_dict,balance):
    for k in range(num_stop):
        stop_list = []
        print()
        n = int(input(f"Enter the number of people at stop {k + 1}: "))
        if n > len(name_list) or n < 1:
            print("Invalid Entry")
            continue
        else:
            print()
            print("Choose the applicable ones:")
            for person in name_list:
                print(f"{name_list.index(person) + 1}. {person} ")
            print()
            for i in range(n):
                x = int(input(f"Enter choice {i + 1}: "))
                stop_list.append(name_list[x - 1])
            amt = {}
            chg = {}
            print()
            for i in range(n):
                a1 = float(input(f"Enter the amount paid by {stop_list[i]}: "))
                amt[stop_list[i]] = a1
            #print(amt)
            print()
            for i in range(n):
                c1 = float(input(f"Enter the amount received by {stop_list[i]}: "))
                chg[stop_list[i]] = c1
            #print(chg)
            for j in total_spent.keys():
                if j in stop_list:
                    paid_amount = amt.get(j, 0)  # Default to 0 if not found
                    received_amount = chg.get(j, 0)  # Default to 0 if not found
                    total_spent[j] += float(paid_amount) - float(received_amount)
            #print(total_spent)
            stop_spent={}
            for i in range(len(name_list)):
                stop_spent[name_list[i]]=0.0
                
            for j in name_list:
                if j in stop_list:
                    paid_amount = amt.get(j, 0)  # Default to 0 if not found
                    received_amount = chg.get(j, 0)  # Default to 0 if not found
                    stop_spent[j] = float(paid_amount) - float(received_amount)
            #print(total_spent)
            stop_split=stop_dict[k]/n
            for j in balance.keys():
                if j in stop_list:
                    paid_amount = stop_spent.get(j, 0)  # Default to 0 if not found
                    balance[j] += float(paid_amount)-float(stop_split)
            #print(balance)
    calculate_settlements(balance)        
            
def calculate_settlements(balance):
    '''print("\nFinal Balances: ")
    for person, bal in balance.items():
        print(f"{person}: {bal:.2f}")'''
    
    # Calculate the total amount spent
    total_spent = sum(balance.values())
    avg_spent = total_spent / len(balance)
    
    # Calculate who needs to pay or receive how much
    payees = []
    payers = []
    for person, bal in balance.items():
        if bal > avg_spent:
            payees.append((person, bal - avg_spent))
        elif bal < avg_spent:
            payers.append((person, avg_spent - bal))
    
    # Sort payees and payers
    payees.sort(key=lambda x: x[1], reverse=True)
    payers.sort(key=lambda x: x[1], reverse=True)
    
    # Display settlements
    print("\nFinal settlements to be made:")
    print()
    i, j = 0, 0
    while i < len(payers) and j < len(payees):
        payer, payer_amount = payers[i]
        payee, payee_amount = payees[j]
        
        amount = min(payer_amount, payee_amount)
        print(f"{payer} pays {payee} {amount:.2f}")
        
        if payer_amount > payee_amount:
            payers[i] = (payer, payer_amount - amount)
            j += 1
        elif payer_amount < payee_amount:
            payees[j] = (payee, payee_amount - amount)
            i += 1
        else:
            i += 1
            j += 1


#Login-System
def start():
    users = {'Niranj':'1703','Sradhya':'1803','test':'0','0':'0'}  # Dictionary to store username-password pairs
    while True:
        print()
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        print()
        choice = input("Enter your choice: ")
        if choice == '1':
            sign_up(users)
        elif choice == '2':
            log_in(users)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#Function to Sign up
def sign_up(users):
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Sign up successful!")
    print()
    print("Login to Continue:")
    print()
    log_in(users)

# Function to log in
def log_in(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print()
    if username in users and users[username] == password:
        print("Login successful!")
        print()
        share()
    else:
        print("Incorrect username or password.")
        print()

start()