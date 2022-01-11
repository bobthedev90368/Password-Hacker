
# importing random
from random import *
import time
count = 0

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0} Hours {1} Minutes {2} Seconds.".format(int(hours),int(mins),sec))

# taking input from user
user_pass = input("Enter your password")

# storing alphabet letter to use thm to crack password
password = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', '', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3' , '4', '5', '6', '7', '8', '9', '!', '@', '#' , '$', '%', '^', '&', '*', '(', ')', '0', '-', '_', '+', '=', '{', '[', '}', ']', '|', ':', ';', '\'', '/', '<', '>', '.', ',', '\\', '\"', ' ']
animals = ['dog', 'cat']
animalskey = [['dogs', 'bark', 'big', 'bad', ],[]]

mostPopularPasswords = ['1234', 'cat', 'dog', '123456', '123456789', 'qwerty', 'password', 'qwerty123', '1q2w3e', '12345678', '111111', '1234567890', '1234567', '000000']


seed = ""
#         an empty string
guess = ""


# using while loop to generate many passwords untill one of
# them does not matches user_pa
def randomllyguesspassword():
  global guess
  global count
  start_time = time.time()
  while (guess != user_pass):
      guess = ""
      # generating random passwords using for loop
      for letter in range(len(user_pass)):
          count = count+1
          guess_letter = password[randint(0, 92)]
          guess = str(guess) + str(guess_letter) 
      # printing guessed passwords
      print(guess)
  end_time = time.time()
  # printing the matched password
  print("Your password is",guess)
  print(str(count) + " guesses.")
  time_lapsed = end_time - start_time
  time_convert(time_lapsed)

def calculateAge(dob):
  from datetime import date
  today = date.today()
  age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
  return age


def logicalydefeatpassword():
  from datetime import date
  global guess
  global count
  start_time = time.time()
  while(guess != user_pass):
    guess = ""
    for i in range(len(mostPopularPasswords)):
      if(guess != user_pass):
        count = count+1
        guess = mostPopularPasswords[i]
        print(guess)
      else:
        break
      if i == len(mostPopularPasswords):
        #Sees when the list is done as to not go forever
        break
    #This part is when the password is not in list.
    if(input("Do you wish to add logic? (Y/N)") == "Y"):
      birthday = input("Input date of birth of person being hacked.\n Please follow the following template: 01-21-2012.\n Character that seperates numbers does not matter.\n Must have a sperating character whether that is a number or letter or character.\n Enter NA if not avaiblible.\n")
      dob = [int(birthday[0:2]), int(birthday[3:5]), int(birthday[6:10])]
      dob.append(calculateAge(date(dob[2], dob[0], dob[1])))
      gender = input("Input gender of person being hacked. Enter NA if not avaiblible.")
      animal = input("Input favorite animal of person being hacked. Enter NA if not avaiblible.")
      color = input("Please input the person who is being hacked favorite color. Enter NA if not avaiblible.")
      number = input("Please enter the favorite number of the person who you are hacking. Enter NA if not avaiblible.")
      if(birthday != "NA"):
        guess = dob[0] + dob[1] + dob[2]
        if guess == user_pass:
          break
        guess = dob[3]
        
    else:
      randomllyguesspassword()
    break
  end_time = time.time()
  print("Your password is",guess)
  print(str(count) + " guesses.")
  time_lapsed = end_time - start_time
  time_convert(time_lapsed)

def getpasswordwithseed():
  break

logicalydefeatpassword()
#randomllyguesspassword()