from bankProjectFunctions import Id_check
from bankProjectFunctions import transfer
from bankProjectFunctions import whitdraw
from bankProjectFunctions import deposit
from bankProjectFunctions import createUser
from bankProjectFunctions import changePass


user_id = "0"
password = 0
i =3 

print("###########BANK###########")
print("Press 1 to log in")
print("Press 2 sign in")   
opp = int(input())
if opp == 1:
  user_id = input("Enter your Id: ")
  password = int(input("Enter your password: "))
if opp ==2:
  createUser()
  user_id = input("Enter your Id: ")
  password = int(input("Enter your password: "))
if Id_check(user_id,password) == True:
 while True : 
  print("                        ")
  print("Enter 1 to Whitdraw money")
  print("                       ")
  print("Enter 2 to Deposit money")
  print("                        ")
  print("Enter 3 to send money")
  print("")
  print("Enter 4 to change your password")
  print()
  print("Enter 5 to exit")
  operation = (input("Select your operation: "))
  if operation == "1":
   whitdraw(user_id)
  elif operation == "2":
   deposit(user_id)
  elif operation == "3":  
   user_id2 = input("Enter the id of the reciever: ")
   transfer(user_id,user_id2)  
  elif operation == "4":
    changePass(user_id)
  elif operation == "5":
   print("You have exited from your account")
   break 
  elif i == 0:
   break
  else:  
   print("Tries left"+ " "+str(i))
   operation = input("You entered the wrong operator enter again: ")
   if operation == "5":
     print("You have exited from your account")
     break
  i-=1