
quiz = [
    {
        "question": "[1. What does CPU stand for?]",
        "options": ["A.) Central Processing Unit", "B.) Computer Power Unit", "C.) Central Peripheral Unit", "D.) Core Programming Unit"],
        "answer": "A"
    },
    {
        "question": '[2. Which component is considered the "brain" of the computer?]',
        "options": ["A.) RAM","B.) CPU", "C.) Hard Drive", "D.) Motherboard"],
        "answer": "B"
    },
    {
        "question": "[3. What type of memory is used for temporary data storage while the computer is running?]",
        "options": ["A. ROM","B.) RAM", "C.) SSD", "D.) HDD"],
        "answer": "B"
    }
]


for quizzes in quiz:
    print(quizzes["question"])
    for option in quizzes["options"]:
        print(option)
    answer = input("Input answer: ")