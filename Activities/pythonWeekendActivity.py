# Intro to Python
# Take home activity

# Instructions
# Create a new Python file called pythonWeekendActivity.py and answer the following questions. 
# This activity contains six (6) questions. This assignment must be completed by no later than 
# 11:59 pm on Sunday March 10th,
# 2024 to receive full credit. 
 
# Two (2) coding prompt questions. 
# You need to solve each coding prompt. To get full credit, 
# you must write down the clues and keywords you find.
# The clues and keywords should be words and phrases 
# we’ve heard in class, but they can also be things YOU 
# believe will help you solve the problem.
  
# Two (2) code deciphering questions. 
# You need to read and describe each code block 
# and explain what is happening on each line. 
# You must use complete sentences to get full credit. 

# Two(2) Open-ended Programming Questions.
# To get full credit, you must write a short
#  paragraph (3-4 sentences) responding to these
# questions. You must use complete sentences.  

# Coding Prompts
# You have been hired as an engineer to develop 
# a VIP list function. The client would like your 
# program to check the names of the people on their 
# list and confirm whether they can get into the VIP 
# section. If the person’s name is on the list, 
# they should be greeted with a message saying 
# they may enter the VIP section. If they are not 
# on the list, they must return to the general
# admission section. Your program should
# check users' names by accepting the guest's 
# name as an argument. 
# The client has provided a list of VIP
# guests that they would like to check and admit
# into the VIP room.

VIP_Guests=["Bill", "Mary", "Dante", "Stacy", "Harry", "Ashley"] 

# a :

def VIPSection(Bill, Mary, Dante, Stacy, Harry, Ashley):
    if name == Bill:
        print('ACCESS GRANTED : Welcome to the VIP Section Bill!')
    if name == Mary:
         print('ACCESS GRANTED : Welcome to the VIP Section Mary!')
         if name == Dante:
          print('ACCESS GRANTED : Welcome to the VIP Section Dante!')
    if name == Stacy:
        print('ACCESS GRANTED : Welcome to the VIP Section Stacy!')
    if name == Harry:
        print('ACCESS GRANTED : Welcome to the VIP Section Harry!')
    if name == Ashley:
        print('ACCESS GRANTED : Welcome to the VIP Section Ashley!')
    else:
         print('ACCESS DENIED : Please go back to general admission Section')

# You have been hired as an engineer to develop 
# a discount rewards program for a store. 
# The store would like your function to ask
# users to enter their name, their membership tier, 
# the item they are buying, and the item's price. 
# Depending on the customer’s membership tier, 
# they will receive one of the following discounts: 
# 25% off for the Gold tier, 15% off for the silver tier,
# and 5% off for the bronze tier. Your program 
# should calculate and return a message to the user
# by name, congratulating them and providing them 
# with the new item price (example: Congratulations, 
# Dan! Your item is now $10.00. Thank you for shopping
# with us. )
         
# a :
goldtier = 25
silvertier = 15
bronzetier = 5
none = 0
membership_tiers = [goldtier, silvertier, bronzetier, none]
def Discount(tier, membership):
     membership_tiers = ['goldtier', 'silvertier', 'bronzetier, none']
     discount = input('What membership do you have? Type in goldtier, slivertier, bronzetier, or none')
     if (membership == membership_tiers[goldtier]):
          print('25% discount has been granted')
     elif (membership == membership_tiers[slivertier]):
        print('15% discount has been granted')
     elif (membership == membership_tiers[bronzetier]):
        print('5% discount has been granted')
     elif (membership == membership_tiers[none]):
        print('No membership pay at full price')
     else:
          print('ERROR please try again')
    
     
     


# Code Deciphering 
# Breakdown and describe what happens in each line 
# of the following code blocks. Then, based on the 
# context of this problem, give each function an 
# appropriate name. 



def unknownFunction_A(data1, data2):
    newData = data2 + 10
    print(f"hello, {data1}. Welcome to Boys Latin.")
    print("by solving this, you have gotten"+ data2 "points added to your grade")

# a : solving an equation and having your grade go up.

def unknownFunction_B(data1, data2):
    if data1 == "btp@gmail.com" and data2 == "abc123":
	    print("Welcome, access granted.")
    elif data1 != "btp@gmail.com" or data2 != "abc123":
 	    print("Sorry, your information is incorrect")
    else:
        print(" Error: somthing went wrong. Try again")

# a : Putting in a password for your email and either being denied access, given access, or an error code.
        
# Programming Questions
# How do you think technology has influenced and
# shaped how you learn in school? Do you think it's
# been positive or negative? Please explain why 
# by providing examples, written in 4 to 5 complete 
# sentences. 

# a : Technology has been thrown into our school out of nowhere during covid
# due to not doing in person learning.
# I think that there are ways that you could say it
# has has some positive effects and some negative.
# a lot of classes has adapted everything onto the laptops
# and it could hurt you due to your laptop not being charged,
# not having a laptop, and other things. But at the same time
# you could say it has helped due to how portable everything is.
# You can access your work anywhere, you don't have to waste paper,
# risk losing anything or leaving anything behind, and it could help
# with writing since some people have bad handwriting.

# What are some ways you think technology can help 
# people learn? Please explain why by providing examples,
# written in 4 to 5 complete sentences. 
        
# There are a lot of ways people can learn from technology.
# Nearly everything is on the internet nowadays and just by looking
# up something you want to learn that can give you basic knowledge on
# the subject. I joined the baseball team and I didn't know anything
# about baseball but now I've watched a couple of youtubes on the games
# rules, positions, and how to play in general I have complete knowledge
# of how the game is played. I think in a couple of years everything could
# be through a screen. I've thought about the good and bad that this could have
# on everything like signing documents online and how easy it could be to get
# peoples private info, but this also shows how faster a lot of things could start
# to get done.