
quiz1 = [
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
        "options": ["A.) ROM","B.) RAM", "C.) SSD", "D.) HDD"],
        "answer": "B"
    }
]

quiz2 = [
    {
        "question": "[1. Who is known as the National Hero of the Philippines?]",
        "options": ["A.) Emilio Aguinaldo", "B.) Andres Bonifacio", "C.) Jose Rizal", "D.) Apolinario Mabini"],
        "answer": "C"
    },
    {
        "question": '[2. What is the name of the first Filipino President of the Philippines?]',
        "options": ["A.) Ferdinand Marcos","B.) Emilio Aguinaldo", "C.) Manuel L. Quezon", "D.) Sergio Osmeña"],
        "answer": "B"
    },
    {
        "question": "[3. What year did the Philippines gain independence from Spain?]",
        "options": ["A.) 1896","B.) 1898", "C.) 1901", "D.) 1946"],
        "answer": "B"
    }
]

quiz3 = [
    {
        "question": '[1. Who is the author of "Noli Me Tangere"?]',
        "options": ["A.) Andres Bonifacio", "B.) Jose Rizal", "C.) Francisco Balagtas", "D.) Apolinario Mabini"],
        "answer": "B"
    },
    {
        "question": '[2. What is the title of the sequel to "Noli Me Tangere"?]',
        "options": ["A.) La Solidaridad","B.) Florante at Laura", "C.) El Filibusterismo", "D.) Dekada '70"],
        "answer": "C"
    },
    {
        "question": '[3. Who is considered the "Father of the Tagalog Poem"?]',
        "options": ["A.) Jose Garcia Villa","B.) Francisco Balagtas", "C.) Lope K. Santos", "D.) Amado V. Hernandez"],
        "answer": "B"
    }
]

player_name = input("What's your name? ")
player_age = input("How old? ")

with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/test_file.txt', 'a') as f:
    f.write(f"\n- {player_name}, {player_age}\t")

def run_quiz(quiz1):
    score = 0
    for quizzes in quiz1:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            score += 1
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {score} out of {len(quiz1)} questions correct")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/test_file.txt', 'a') as f:
        f.write(f"\t{score}/{len(quiz1)}\n")

def run_quizzing(quiz2):
    score = 0
    for quizzes in quiz2:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            score += 1
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {score} out of {len(quiz2)} questions correct")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/test_file.txt', 'a') as f:
        f.write(f"\t{score}/{len(quiz2)}\n")

def run_quizness(quiz3):
    score = 0
    for quizzes in quiz3:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            score += 1
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {score} out of {len(quiz3)} questions correct")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/test_file.txt', 'a') as f:
        f.write(f"\t{score}/{len(quiz3)}\n")

while True:
    try:
        pick_category = int(input("\t- Categories -\n1. Technology\n2. History\n3. Literature\n\nChoose a number: "))

        if pick_category in [1, 2, 3]:
            if pick_category == 1:
                run_quiz(quiz1)
                break
            elif pick_category == 2:
                run_quizzing(quiz2)
                break
            elif pick_category == 3:
                run_quizness(quiz3)
                break
    except:
        print("////Choose a valid number////")
        continue
            


