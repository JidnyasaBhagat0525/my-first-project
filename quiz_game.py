print("===== QUIZ GAME =====")

score = 0

answer = input("Q1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Q2. Which language are we learning? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your Score =", score)
