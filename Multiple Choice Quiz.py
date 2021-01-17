# This is a simple multiple choice quiz done through a Youtube tutorial.

# Introductory Statements

from time import sleep
from question import Question

# Questions before test.

print('Hello! Please answer some basic questions to begin the multiple choice test!')
sleep(3)


print('What is your first name?')
myName = input()
sleep(3)


print('Thank you, ' + myName)
sleep(3)


print('How old are you?')
myAge = input()
sleep(3)


print('Thank you, ' + myName + '. You are ' + myAge + ' years old.')
sleep(3)


print('Last question. What is the date you are taking this test?')
testDate = input()
sleep(3)


print('Thanks, ' + myName + '!' + ' You are taking this test on ' + testDate + '.')
sleep(3)

# Good Luck! How to answer.

print('Good luck with this multiple choice test ' + myName + '!')
sleep(1)
print('Please answer the following questions with one of the choices provided. Example - a, b or c')
sleep(1)

# Loading Multiple Choice Test

print('Initializing test')
sleep(1)
print('5')
sleep(1)
print('4')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')


sleep(3)
print('Test successfully loaded! Good luck, ' + myName)
sleep(3)


question_prompts = [
    'What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]




def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    sleep(5)
    print('Thank you for answering the questions')
    sleep(1)
    print('Now gathering results.')
    sleep(5)
    print('Results successfully gathered. Now tabulating your score')
    sleep(3)

    print('Congratulations, ' + myName + ', ' + myAge + ' years old!')
    sleep(1)
    print('You got ' + str(score) + '/' + str(len(questions)) + ' Correct!')
    sleep(1)
    print('This test result was generated on ' + testDate + ', and the score is valid for one week!')
    sleep(1)
    print('Thank you for taking our test.')
    sleep(1)
    print('Goodbye ' + myName + '!')


run_test(questions)
