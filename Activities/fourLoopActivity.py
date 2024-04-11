# While Loop - repeats a block of code instructions , so long as conditon is true.

i = 0 # i stands for iterator. Its the starting point for a while loop

while i == 0
    print(i)

# The result here is that i (or 0) will continue to print forever because the while condition is true.

# For Loops - repeats a block of code instructions, upto a number of items in a group.

def ddg_game():
    groupOfKids = ['duck','duck','duck','goose','duck','duck']
# list of items
    for kid in groupOfKids:
# for every item in this list; kid is the item groupOfKids is the list.
        print(kid)
#print each item; print each kid.
    if kid == 'goose':
        print('found the goose!')
        continue
    print(kid)

def rpggame():
    inventory = ['sword','gun','shield','potion','grenade']
    print(inventory)
    for item in inventory:
        if item == userweapon:
            print(f'you have equipped the {userweapon} to your fighter')

def gtaCheatCodes():
    usercode= input('PLease type in a cheat code.')
    cheatcodelist = [1,2,3,4]
    for code in cheatcodelist:
        if usercode == 0:
          print('unlimited money')
              

infiniteMoney = 0


def twittertext():
    tweets = ['hello world going on a trip']
    userpost = input('upload ur post :')

    for entry in posts:
        posts.insert(0,userpost)
    print(entry)
    