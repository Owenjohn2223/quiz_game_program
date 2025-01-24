
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
    },
    {
        "question": "[4. Which company created the Windows operating system?]",
        "options": ["A.) Apple","B.) Microsoft", "C.) Google", "D.) IBM"],
        "answer": "B"
    },
    {
        "question": "[5. Which device is used to input text into a computer?]",
        "options": ["A.) Monitor","B.) Keyboard", "C.) Printer", "D.) Scanner"],
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
    },
    {
        "question": '[4. Which island did Ferdinand Magellan first land on in the Philippines?]',
        "options": ["A.) Cebu","B.) Leyte", "C.) Samar", "D.) Bohol"],
        "answer": "C"
    },
    {
        "question": "[5. When is Philippine Independence Day celebrated?]",
        "options": ["A.) May 1","B.) June 12", "C.) July 4", "D.) August 26"],
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
    },
    {
        "question": '[4. What is the literary form of "Florante at Laura"?]',
        "options": ["A.) Novel","B.) Epic", "C.) Awit", "D.) Short Story"],
        "answer": "C"
    },
    {
        "question": '[5. What does "awit" mean in Filipino literature?]',
        "options": ["A.) Song","B.) Epic", "C.) Story", "D.) Legend"],
        "answer": "A"
    }
]

quiz4 = [
    {
        "question": '[1. What is the largest planet in our solar system?]',
        "options": ["A.) Earth", "B.) Jupiter", "C.) Saturn", "D.) Mars"],
        "answer": "B"
    },
    {
        "question": '[2.Which animal is known as the "King of the Jungle"?]',
        "options": ["A.) Tiger","B.) Lion", "C.) Elephant", "D.) Leopard"],
        "answer": "B"
    },
    {
        "question": '[3. What is the national sport of the Philippines?]',
        "options": ["A.) Basketball","B.) Boxing", "C.) Arnis", "D.) Volleyball"],
        "answer": "C"
    },
    {
        "question": '[4. What does the "E" in email stand for?]',
        "options": ["A.) Electronic","B.) Express", "C.) Efficient", "D.) Easy"],
        "answer": "A"
    },
    {
        "question": '[5. Which continent is known as the "Land Down Under"?]',
        "options": ["A.) South America","B.) Africa", "C.) Asia", "D.) Australia"],
        "answer": "D"
    }
]

player_name = input("What's your name? ")
player_age = input("How old? ")

with open('players_scores.txt', 'a') as f:
    f.write(f"\n- {player_name}, {player_age}\t")

def technology(quiz1):
    points = 0
    for quizzes in quiz1:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            points += 100
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {points} points, Good Job!")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/quiz_game_program/players_scores.txt', 'a') as f:
        f.write(f"\tTechnology - {points}\n")


def history(quiz2):
    points = 0
    for quizzes in quiz2:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            points += 100
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {points} points, Good Job!")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/quiz_game_program/players_scores.txt', 'a') as f:
        f.write(f"\tHistory - {points}\n")

def literature(quiz3):
    points = 0
    for quizzes in quiz3:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            points += 100
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {points} points, Good Job!")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/quiz_game_program/players_scores.txt', 'a') as f:
        f.write(f"\tLiterature - {points}\n")

def random(quiz4):
    points = 0
    for quizzes in quiz4:
        print(quizzes["question"])
        for option in quizzes["options"]:
            print(option)
        answer = input("Input answer: ").capitalize()
        if answer == quizzes["answer"]:
            print("Tumpak, good job!\n")
            points += 100
        else:
            print("Engk! Ligwak. The right answer was", quizzes["answer"], '\n')
    
    print(f"You got {points} points, Good Job!")

    with open('C:/Users/Owen John/OneDrive/Desktop/PLD Programs folder/quiz_game_program/players_scores.txt', 'a') as f:
        f.write(f"\tRandom - {points}\n")

while True:
    try:
        pick_category = int(input("\t- Categories -\n1. Technology\n2. History\n3. Literature\n4. Random Topic\n\nChoose a number: "))

        if pick_category in [1, 2, 3, 4]:
            if pick_category == 1:
                technology(quiz1)
                break
            elif pick_category == 2:
                history(quiz2)
                break
            elif pick_category == 3:
                literature(quiz3)
                break
            elif pick_category == 4:
                random(quiz4)
                break
    except:
        print("////Choose a valid number////\n")
        continue
            


