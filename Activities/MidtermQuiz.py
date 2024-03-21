
# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error

# a : Piece of string being incorrect that makes your command fail.
# type error

# a : When you use something that isn't supposed to be used in that way.

# name error

# a : Trying to use a variable that isn't defined by a value.

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?

# a : str() function

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?

# a : int() function

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 

# a : Variables cannot start with a number, variables should have names that're apart of a value,
# and you can only start a variable with a letter, a dollar sign, and a underscore.

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = - The equal sign is what you'd use to assign operators.
# == - The double equal sign operator is used to make things equal.
# =! - unlike the double equal sign the equal explanation mark shows how things aren't equal.

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# a : Keywords - alert, function, and change



def car_detection_System():
    speed = input('How fast would you like the gear to be?')
    if speed >= 20:
        print('Shift to gear 1')
    elif speed >= 30:
        print('Shift to gear 2')
    elif speed >= 40:
        print('Shift to gear 3')
    else:
        print('Revert back to gear 1')




# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach
        
# a : Keywords - two, either, change
Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
day_of_the_week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
def Breakfast(days_of_the_week):
    if Breakfast(0):
        print("Todays Monday, in the morning you'll have 2 eggs and an apple and in the afternoon bbq grilled chicken and broccoli")
    elif Breakfast(1):
        print("Todays Tuesday, in the morning you'll have oatmeal with strawberries and blueberries, and in the afternoon baked chicken with kale")
    elif Breakfast(2):
        print("Todays Wednesday, in the morning you'll have a fruit salad, curry goat with rice and cabbage")
    elif Breakfast(3):
        print("Todays Thursday, in the morning you'll have pancakes and turkey sausage, and in the afternoon eggplant pasta")
    elif Breakfast(4):
        print("Todays Friday, in the morning you'll have steak and eggs and in the afternoon cheeseburger and fries")
    elif Breakfast(5):
        print("Todays Saturday, in the morning you'll have oatmeal, and in the afternoon it'll be baked chicken and string beans")
    elif Breakfast(6):
        print("Todays Sunday, starting the weak off with oatmeal and then in the afternon steak and spinich")






# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# a: arguments, inform, above
        
def SAT_scores():
    if 0 > 85:
        print('You didnt make the academic honors list')
    if 0 < 85:
        print('You made it on the academic honors list')


# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
        
def temperture():
    if 50 < 60:
        print('Its hot outside')
    if 50 > 60:
        print('Its cold outside')