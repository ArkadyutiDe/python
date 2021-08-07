import countriesAndCapitalsList
import random

def rules():
    print("\nRules:-")
    print("In this game, we will be asking you some countries or capitals name and you have to give the capitals or countries name..")
    print("If you give the correct answer, you will be awarded with 10 points(+)...")
    print("If you press Enter, then you will be skipping the question and 2.5 points(-) will be deducted..")
    print("If you answer wrong, 10 points will be deducted and then the game will end and your points will be shown....")
    print("\nGive your best try")
    print("If ready, press Enter or see the Atlas again...")
    input()

helloCapitals = countriesAndCapitalsList.countryCapitals()
answer, points, correct, skip, qNo = 'correct', 0, 0, 0, 1
correctMarks = 10
wrongMarks = -10
skipMarks = -5
qCountries = []

rules()

while (answer != 'wrong'):
    qType = random.randint(0, 1)
    i = random.randint(0, len(helloCapitals) - 1)

    if (qNo == 202):
        points = points + wrongMarks
        print("\nYou gave {0} correct answers and skipped {1} questions\nSo your total Points are = {2}".format(correct, skip, points))
        break

    if i not in qCountries:
        qCountries.append(i)
        print("\nQuestion Number {0} :- ".format(qNo))
        qNo = qNo + 1

        if (qType == 0):
            question = list(helloCapitals)[i]
            correctAnswer = helloCapitals[list(helloCapitals)[i]]

            givenAnswer = input("Enter the capital of the country {0} :- ".format(question))

        elif (qType == 1):
            correctAnswer = list(helloCapitals)[i]
            question = helloCapitals[correctAnswer]

            givenAnswer = input("Enter the country of the capital {0} :- ".format(question))

        if (givenAnswer == correctAnswer):
            points = points + correctMarks
            correct = correct + 1
            print("\nCorrect Answer !!!")
            print("Points :- {0}\n".format(points))

        elif(givenAnswer == ''):
            points = points + skipMarks
            skip = skip + 1
            print("The answer is {0}..\nWe are skiping this question..\nPoints :- {1}".format(correctAnswer, points))

        else:
            points = points + wrongMarks
            print("\nYour answer is wrong..\nThe answer is {0}..".format(correctAnswer))
            print("\nYou gave {0} correct answers and skipped {1} questions\nSo your total Points are = {2}".format(correct, skip, points))
            print("\nWe are ending... Better choice next time..\n\n")
            answer = 'wrong'