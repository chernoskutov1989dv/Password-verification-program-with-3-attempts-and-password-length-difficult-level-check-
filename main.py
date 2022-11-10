import re
def validate():
    while True:
        password = input ("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at least 8 letters. Please, restart program")
            break

        elif re.search ("[0-9]", password) is None:
            print ("Make sure your password has a number in it")
        elif re.search("[A-Z]", password) is None:
            print ("Make sure your password has a capital letter in it")
        elif password != "Asdf123456":
            print('Wrong password!')
            password = input('Try again: ')

        attemptsCount = 3
        for attempt in range(1, 2):

            password2 = input('Repeat password: ')
            if password == "Asdf123456" and password == password2:
                print('Password is ok!!! Welcome to system! ')
            if password2 == "Asdf123456" and password != password2:
                print('Password2 is ok!  But password1 is not equal password2! Passwords should be equal! Restart program ')
            if password == "Asdf123456" and password2 != password:
                print('Password1 is ok!  But password2 is not equal password! Passwords should be equal! Restart program')
            if password != "Asdf123456" and password2 != "Asdf123456":
                print(' Wrong passwords! Restart program')
            break

            attemptsCount -= 1
            print('Wrong password! You have attempts: ', 1 - attempt)
        if attemptsCount == 2:
            print('')
            break

        else:
            print ("")
            break
validate()

