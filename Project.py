print("Wellcome treasue island, Your mission is to find the treasure.")
path = input("Which parth you want to take? 'left or 'right'?")

if path == 'right':
    print("Game over!")
else:
    ask = input("Do you want to 'wait' or 'swim'?")
    if ask == 'swim':
        print('GameOver!!')
    else:
        door = input("Which door you wanna get in thru? 'yellow' or 'red'")
        if door == 'yellow':
            print("You won the game!!!")
        else:
            print("GameOver!!!")






















# if path == 'right':
#     ask = input("Do you want to 'wait' or 'swim'? ")
#     if ask == 'wait':
#     else:
#        print("Fked")   
#     askdoor = input("Which door you wanna get in thru? 'Red' 'Yellow' or 'Blue'")
#     if askdoor == 'Yellow':
#      print("You won the game!!")
#     else: 
#      print("fked")
# else:
#     print("Game over")
