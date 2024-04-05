def passwordCheck():
    userPassword = input('Please enter a password:')
correctPassword = 1234
attempt = 0
    while userPassword != correctPassowrd:
        print('incorrect password. Please try again')   
        attempt +=1   
    userPassword = input('Please enter a password:')
    if userPassword == userPassword:
        print("password correct.")
        if attempt == 3:
            print('Exceeded attempts. Try again in 5 minutes.')