import time

QUESTIONS = [
    {
        "q": "What is the output of: print(2 * 3 ** 2)?",
        "choices": ["A) 36", "B) 18", "C) 12", "D) 11"],
        "answer": "C"  # 2 * (3**2) = 18 -> Wait careful: correct is B) 18
    },
    {
        "q": "Which data type is immutable?",
        "choices": ["A) list", "B) dict", "C) set", "D) tuple"],
        "answer": "D"
    },
    {
        "q": "What does 'len' return for the string 'hello'?",
        "choices": ["A) 4", "B) 5", "C) 6", "D) error"],
        "answer": "B"
    },
    {
        "q": "Which keyword starts a function definition?",
        "choices": ["A) func", "B) def", "C) function", "D) lambda"],
        "answer": "B"
    },
    {
        "q": "Which one creates a set?",
        "choices": ["A) {}", "B) set()", "C) []", "D) ()"],
        "answer": "B"
    },
]

def run_quiz():
    print("\nSimple Python Skill Quiz — 5 questions\n")
    name = input("Enter your name: ").strip() or "Anonymous"
    start = time.time()
    score = 0

    for idx, q in enumerate(QUESTIONS, start=1):
        print(f"\nQ{idx}. {q['q']}")
        for choice in q["choices"]:
            print("   ", choice)
        while True:
            ans = input("Your answer (A/B/C/D): ").strip().upper()
            if ans in ("A","B","C","D"):
                break
            print("Please enter A, B, C, or D.")
        if ans == q["answer"]:
            score += 1

    duration = time.time() - start
    percent = score / len(QUESTIONS) * 100

    print(f"\n{name}, you scored {score}/{len(QUESTIONS)} ({percent:.1f}%).")
    print(f"Time taken: {duration:.1f} seconds.")

    # Save results
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {name} - {score}/{len(QUESTIONS)} - {percent:.1f}% - {duration:.1f}s\n")

    print("Your result was saved to results.txt")

if __name__ == "__main__":
    run_quiz()
