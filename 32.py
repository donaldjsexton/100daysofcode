import random
def greet():
    greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
    index = random.randint(0,3)
    print(greetings[index])

while True:
    greet()
    print("Would you like to be greeted again?")
    response = input()
    if response.lower() != "yes":
        break
  
