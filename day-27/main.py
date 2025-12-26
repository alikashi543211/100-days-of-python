questions = [
    'What does PHP stand for?',
    'Which HTTP status code represents “Too Many Requests”?',
    'In Laravel, which command is used to clear the application cache?',
    'Which JavaScript method removes whitespace from both ends of a string?',
    'Which database is most commonly used with Laravel by default?',
]

questionOptions = [
    [
        "Personal Home Processor",
        "Private Home Page",
        "Hypertext Preprocessor", 
        "Pretext Hyper Program",
        3
    ],
    [
        "200",
        "401",
        "404",
        "429",
        4
    ],
    [
        "php artisan cache:make",
        "php artisan clear:cache",
        "php artisan cache:clear",
        "php artisan app:clear",
        3
    ],
    [
        "cut()",
        "remove()",
        "clean()",
        "trim()",
        4
    ],
    [
        "MongoDB",
        "SQLite",
        "PostgreSQL",
        "MySQL",
        4
    ]
]

print("***************** Kon Baney Ga Carore Patii Show ********************************************")

for question in questions:
    print(question)
    optionsIndex = questions.index(question)    
    options = questionOptions[optionsIndex]
    correctAnswer = options[len(options) - 1]
    for option in options:
        if(option == options[len(options) - 1]):
            continue
        print(options.index(option) + 1, option)
    answer = int(input("Please Choose Correct Option: "))
    if(answer == correctAnswer):
        print("*****************  You Have Won Amount of 1 Carore ********************************************")
    else:
        print("*** Sorry !!!! You Have Lose The Game *******")
    break

