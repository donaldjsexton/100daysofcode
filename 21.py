score = 0
num_questions = 10

while True:
    quiz_number = int(input("Enter the number you want to be quizzed on: "))
    
    for num in range(1, 11):
        correct_answer = quiz_number * num
        user_answer = int(input(f"What is {quiz_number} times {num}? "))
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    print(f"Quiz completed! Your score is {score}/{num_questions}.")
    print("🎉🎉🎉🎉")
    
    restart = input("Would you like to restart the quiz? (yes/no): ").lower()
    if restart != "yes":
        break
    else:
        score = 0
