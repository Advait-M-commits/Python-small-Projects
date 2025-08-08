import random
hand = '''        
        ___..__
__..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
'''

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 '''

scissors = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''
user_input = int(input("0 for rock, 1 for hand, 2 scissors\n"))
if user_input == 0:
    print("Your choice: ",rock)
elif user_input == 1:
    print("Your choice: ",hand)
elif user_input == 2:
    print("Your choice: ",scissors)
else:
    print("EEEE choose one of the option")

con = [hand,rock,scissors]
commputer_Choise = random.choice((con))
print("The computer choice: ",commputer_Choise)

if con[user_input] == commputer_Choise:
    print("It's a draw!")
