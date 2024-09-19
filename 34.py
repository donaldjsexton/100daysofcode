import os, time
listOfEmails = [] 

def prettyPrint():
    os.system("clear")
    print("listOfEmails")
    print()
    for index in range(len(listOfEmails)):
        print(f"{index}. {listOfEmails[index]}")
        time.sleep(1)

def spam(max):
    for i in range(0,max):
        print(f"""
          Email {i+1}

Dear {listOfEmails[i]},

It has come to our attention that you're missing out on the
amazing replit 100 days of code. We insist you do it right away.
If you don't we will pass on your email to every spammer we've
ever enountered and also sugn you up to the My Little Pony newsletter,
because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
    time.sleep(1)
    os.system("clear")
    
while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2. Delete email\n3. View emails\n4. Get SPAMMING\n ")
    if menu == "1":
        email = input("Enter email: ")
        listOfEmails.append(email)
    elif menu == "2":
        email = input("Enter email: ")
        if email in listOfEmails:
            listOfEmails.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        spam(4)
    time.sleep(1)
    os.system("clear")


               
