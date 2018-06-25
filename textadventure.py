start = '''
After spending what seems like an eternity looking for the perfect chair in ikea,
you realize you are lost. You look around and see you are in a strange room with
a door on you left and your right.
'''
print(start)

print("Type 'left' to go left or 'right' to go right.")

user_input = input()
if(user_input == "left"):
    print('''
    You decide to go left and you meet brad. He's been stuck in ikea
    for a while too. Do you want to follow him?
    ''')
    followBrad = input("Type 'yes' to follow Brad and 'no' to go another way.")
    if followBrad == "yes":
        print('''
        Brad takes you to his friends. They want you to stay in Ikea forever.
        Do you run or accept your fate?
        ''')
        runOrStay == input("Type 'run' to escape or 'stay' to accept it.")
        if runOrStay == "stay":
            print("You're stuck in Ikea forever :(.")
            print("YOU LOSE")
        elif followBrad == "no":
            print('''
            You decide not to follow brad and walk into the next room. You
            meet Pico. He asks if you need directions.
            ''')
            askPico = input("Type 'yes' to ask or 'no' to decline.")
            if askPico == "yes":
                print("Pico tells you that the kitchen is straight ahead.")
            elif askPico == "no":
                print("Pico tells you that the kitchen is straight ahead anyway.")
elif(user_input == "right"):
    print("You decide to go right and...")
