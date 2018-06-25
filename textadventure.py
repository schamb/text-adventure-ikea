start = '''
After spending what seems like an eternity looking for the perfect chair in ikea,
you realize you are lost. You look around and see you are in a strange room with
a door on you left and your right.
'''
print(start)

print("Type 'left' to go left or 'right' to go right.")

user_input = input()
if(user_input == "left"):
    print("You decide to go left and...")
elif(user_input == "right"):
    print("You decide to go right and...")
