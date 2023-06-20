user_input = input()
started = False

while True:
    if user_input.upper() == 'START':
        if not started:
            print('Car started! Ready to go!')
            started = True
        else:
            print('Car already started!')
        
    elif user_input.upper() == 'STOP':
        if started:
            print('Car stopped! You reached!')
            started = False
        else:
            print('Car already stopped!')

    elif user_input.upper() == 'HELP':
        print('''
Start -> To start the car
Stop -> To stop the car
Quit -> To quit the game''')

    elif user_input.upper() == 'QUIT':
        print('You exit!')
        break

    else: 
        print("I don't understand that")
    
    user_input = input()
