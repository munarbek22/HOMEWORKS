while True:
    colour = input('Enter the colour (red, green, yellow) or exit to exit: ').lower()
    if colour == 'red':
        print('Stop!')
    elif colour == 'green':
        print('Go!')
    elif colour == 'yellow':
        print('Wait...')
    elif colour == 'exit':
        print('exit...')
        break
    else:
        print('Mistake, please enter(red, green, yellow or exit)')


