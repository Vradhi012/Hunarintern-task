import random

def quiz():
    """
    Conducts a quiz and provides feedback, score, and final result"""

    questions = [
        ("What is the capital of japan?", "tokyo"),
        ("Which programming language is used for this quiz?", "Python"),
        ("write the sum of 13+56?", "69"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("Which animal is known as the king of the jungle?", "Lion")
    ]

    score = 0
    for question, answer in questions:
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)

    print("\nQuiz Results:")
    print(f"You scored {score} out of {len(questions)}.")

    if score >= 3:
        print("Congratulations! You passed the quiz.")
    else:
        print("Better luck next time.")


    quiz()