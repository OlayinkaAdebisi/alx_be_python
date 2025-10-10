# 🧾 Python OOP Practice Test — Interactive Version

def oop_test():
    questions = [
        {
            "question": "What is the purpose of the __init__ method in Python?",
            "options": [
                "A. To delete an object",
                "B. To define a static method",
                "C. To initialize an object’s attributes",
                "D. To initialize a class attribute"
            ],
            "answer": "C"
        },
        {
            "question": "What is Method Resolution Order (MRO) in Python?",
            "options": [
                "A. The order in which variables are initialized",
                "B. The order in which base classes are searched when executing a method",
                "C. The order in which methods are called within a function",
                "D. The order in which methods are defined in a class"
            ],
            "answer": "B"
        },
        {
            "question": "What is a static method in Python?",
            "options": [
                "A. A method that initializes an object’s attributes",
                "B. A method that can modify instance-specific data",
                "C. A method that is bound to the class and not the object of the class",
                "D. A method that can access or modify the class state"
            ],
            "answer": "C"
        },
        {
            "question": "Which concept allows different classes to be treated as instances of the same class through a common interface?",
            "options": [
                "A. Abstraction",
                "B. Encapsulation",
                "C. Polymorphism",
                "D. Inheritance"
            ],
            "answer": "C"
        },
        {
            "question": "Which type of inheritance allows a class to inherit from multiple base classes?",
            "options": [
                "A. Hierarchical inheritance",
                "B. Multiple inheritance",
                "C. Multilevel inheritance",
                "D. Single inheritance"
            ],
            "answer": "B"
        },
        {
            "question": "What is the difference between __str__ and __repr__?",
            "options": [
                "A. Neither are used for string representation",
                "B. __str__ is used for informal string representation, and __repr__ is used for official string representation",
                "C. Both are used for the same purpose",
                "D. __str__ is used for official string representation, and __repr__ is used for informal string representation"
            ],
            "answer": "B"
        },
        {
            "question": "Which decorator is used to define a class method in Python?",
            "options": [
                "A. @classmethod",
                "B. @method",
                "C. @property",
                "D. @staticmethod"
            ],
            "answer": "A"
        },
        {
            "question": "What is duck typing in Python?",
            "options": [
                "A. A syntax error related to type casting",
                "B. A type of polymorphism where the class type is less important than the methods it defines",
                "C. A method to create new classes",
                "D. Ensuring type safety by explicitly declaring variable types"
            ],
            "answer": "B"
        },
        {
            "question": "Which magic method is used to represent an object as a string in Python?",
            "options": [
                "A. __del__",
                "B. __repr__",
                "C. __init__",
                "D. __str__"
            ],
            "answer": "D"
        },
        {
            "question": "What is the purpose of the __del__ method in Python?",
            "options": [
                "A. To override methods",
                "B. To handle the deletion of an object",
                "C. To initialize an object’s attributes",
                "D. To define class attributes"
            ],
            "answer": "B"
        }
    ]

    score = 0

    print("\n🧠 Welcome to the Python OOP Test!\n")
    for i, q in enumerate(questions):
        print(f"Question {i}: {q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {q['answer']}\n")

    print(f"🏁 Test complete! You scored {score}/{len(questions)} ({(score/len(questions))*100:.1f}%).")

# Run the test
oop_test()
