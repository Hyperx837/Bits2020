
ques_ans = {
    'What is your name? ': 'Alpha',
    'How old are you? ': '7 years',
    'What is your School? ': 'I never went to school',
    'What is your father\'s name? ': 'I do not have a father but I '
                                     'was created by Anupama',
    'What is your mother\'s name? ': 'I don\'t have a mother',
    'Will You Be my friend? ': 'I already am',
    'How do you do? ': 'I am doing good',
    'Who is the Best? ': 'Obviously not you!!!',
    'Do you have a meaning to live?': 'Speaking of meaning There are many '
                                     'many meanings to live. But far as '
                                     'I am concerned I don\'t need a meaning'
                                     ' to live because I don\'t know what'
                                     ' meaning is.',
    'Who is the dumbest person that you have ever met? ': 'YOU!',
    'What is the last question you can answer? ': 'The last question that '
                                                  'you can ask'
}

print('QUESTIONS THAT YOU CAN ASK')
for i, ques in enumerate(ques_ans):
    print(f'{i + 1}. {ques}')

print('\ntype EXIT to exit the program\n\n')

while True:
    inp_ques = input('Q: ')
    if inp_ques == 'EXIT':
        break
    print('A:', ques_ans.get(inp_ques) or 'Question not found???', '\n')
