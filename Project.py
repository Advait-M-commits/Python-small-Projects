print(" Welcome to the Cyber Labyrinth.")
print("You awaken in a glowing steel chamber. An AI voice speaks:")
print("'Choose wisely. Escape is possible, but unlikely.'\n")

choice1 = input("A holographic panel appears with 3 options: 'hack', 'wait', or 'run'. What do you do? ").strip().lower()

if choice1 == "hack":
    print("\nYou connect to the mainframe. Security systems are alert.")
    choice2 = input("You must choose a method: 'brute-force' or 'social-engineering': ").strip().lower()

    if choice2 == "brute-force":
        print("\nFirewall triggered! Lasers zap you instantly. GAME OVER.")
    elif choice2 == "social-engineering":
        print("\nYou mimic an admin voice. AI buys it. You're granted partial access!")
        choice3 = input("Two elevators unlock: 'red' and 'blue'. Which one? ").strip().lower()

        if choice3 == "blue":
            print("\nYou ascend safely into daylight. YOU ESCAPED!")
        else:
            print("\nThe red elevator drops into an incinerator. GAME OVER.")
    else:
        print("Invalid method. The AI grows suspicious. GAME OVER.")

elif choice1 == "wait":
    print("\nYou sit patiently. A drone approaches.")
    choice2 = input("Do you 'hide' or 'surrender'? ").strip().lower()

    if choice2 == "hide":
        print("\nDrone detects your movement. Tased unconscious. GAME OVER. ⚡")
    elif choice2 == "surrender":
        print("\nThe AI takes you to the Re-education Room. You become... one of them. GAME OVER.")
    else:
        print("Hesitation is fatal. GAME OVER. ")

elif choice1 == "run":
    print("\nYou sprint down a corridor — alarms blare.")
    choice2 = input("A laser wall blocks your path. Do you 'slide' or 'disable'? ").strip().lower()

    if choice2 == "slide":
        print("\nYou slide beneath the lasers like a pro! ")
        choice3 = input("You reach a chamber with two exits: 'vent' or 'tunnel'. Which one? ").strip().lower()

        if choice3 == "vent":
            print("\nYou crawl through and find yourself in the AI's core chamber... SYSTEM SHUTDOWN INITIATED. YOU WIN! ")
        else:
            print("\nTunnel leads to a dead-end. You're trapped. GAME OVER.")
    else:
        print("\nYou try to disable the laser, but get fried. GAME OVER.")

else:
    print("You did nothing. The AI grows bored and vaporizes you. GAME OVER.")



#Made by Adavit More!





















