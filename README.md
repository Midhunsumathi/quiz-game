def play_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        ans = input("Your answer (1-4): ")
        if q["options"][int(ans)-1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"\nFinal score: {score}/{len(questions)}")

questions = [
    {"question": "Capital of France?", "options": ["Paris","London","Berlin","Rome"], "answer": "Paris"},
    {"question": "Red Planet?", "options": ["Mars","Jupiter","Venus","Saturn"], "answer": "Mars"},
    {"question": "Largest organ?", "options": ["Heart","Liver","Lungs","Skin"], "answer": "Skin"}
]

if _name_ == "_main_":
    play_quiz(questions)
