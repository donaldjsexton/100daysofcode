print("30 days down... so many to go...    ")
print()
for i in range(1, 31):
    thought = input(f"Day {i} of 100 days of python challenge, what did you think?: ")
    print()
    myText = f"You thought day {i} was"
    print(f"{myText:^35}")
    print(f"{thought:^35}")
    print()