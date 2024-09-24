import random, string

password_length = int(input("Enter length of the password:\n"))

print('''Choose character set for password from these options : 
         1. Numbers
         2. Letters
         3. Special characters
         4. Exit''')
 
character_list = ""
 
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        character_list += string.ascii_letters
    elif(choice == 2):
         
        character_list += string.digits
    elif(choice == 3):
         
        character_list += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []
 
for i in range(password_length):
   
    randomchar = random.choice(character_list)
     
    password.append(randomchar)
 
print("The random password is " + "".join(password))