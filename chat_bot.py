def chat():
    print('How are you?')

    answer = input('\n > ').lower()

    if answer == 'good':
        print('That is good.')

        chat()

    elif answer == 'bad':
        print('That is not good.')

        chat()

    elif answer == 'fine':
        print('You could be better.')

        chat()

    elif answer == 'ok':
        print('Just okay?')

        chat()

    else:
        print('INVALID ANSWER!')

        chat()


chat()
