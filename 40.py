name = input("Enter your name: ").strip().capitalize()
age = input("Enter your age: ").strip()
tel = input("Enter your telephone number: ").strip()
email = input("Enter your email: ").strip()
address = input("Enter your address: ").strip()
contact = {"name:": name, "age:": age, "tel:": tel, "email:": email, "address:": address}
print()
print(f"Name: {contact['name:']}\nAge: {contact['age:']}\nTelephone: {contact['tel:']}\nEmail: {contact['email:']}\nAddress: {contact['address:']}") 
