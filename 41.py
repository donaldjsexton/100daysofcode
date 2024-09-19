website = {"name": None, "url": None, "description": None, "rating": None}

website["name"] = input("Enter the name of the website: ")
website["url"] = input("Enter the url of the website: ")
website["description"] = input("Enter the description of the website: ")
website["rating"] = input("Enter the rating of the website: ")

print()
for name, value in website.items():
    print(f"{name}: {value}")