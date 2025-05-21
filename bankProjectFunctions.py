import json
import random
import os

personInfo = {}

if not os.path.exists("userInfo.json"):
    with open("userInfo.json", "w") as file:
        json.dump({}, file)
try:
    with open("userInfo.json", "r") as file:
        personInfo = json.load(file)
except json.JSONDecodeError:
    print("The file you are trying to read has faults")

def Id_check(Id,password):
  if Id in personInfo: 
    user = personInfo[Id]
    if user["password"] == password: 
     print("Welcome" + " " +user["name"]+ " " + user["surName"])
     print("Account balance:"+ " "+str(user["balance"]))
     return True
    else: 
     print("Wrong Id or password")
 
    
def whitdraw(Id):  
  user = personInfo[Id]
  ammount = int(input( "Enter the amount you want to withdraw: "))
  if ammount < user["balance"]:
   user["balance"] = user["balance"]-ammount
   print("Your new balance is "+ " "+str(user["balance"]))
   with open("userInfo.json", "w", encoding="utf-8") as file:
      json.dump(personInfo, file, indent=4,ensure_ascii=False)
   input("Press enter to return to menu")
  else:
    print("Insufficient balance")

def deposit(Id):
  user = personInfo[Id] 
  ammount = int(input( "Enter the amount you want to : "))
  user["balance"] = user["balance"] + ammount
  print("Your new balance is "+ " "+str(user["balance"]))
  with open("userInfo.json", "w", encoding="utf-8") as file:
    json.dump(personInfo, file, indent=4,ensure_ascii=False)
  input("Press enter to return to menu")

def transfer(Id,Id2):
  sender = personInfo[Id]
  if Id2 in personInfo:
    reciever = personInfo[Id2]
    if Id2 != Id:
      user_name = input("Enter name of the reciever: " )
      if user_name in reciever["name"]:
           amount = int(input("Enter the amount you want to send: "))
           if amount < sender["balance"]:
       
             sender["balance"] -= int(amount)
             reciever["balance"] += int(amount)
             print("Your new balance is "+ " "+ str(sender["balance"]))
             with open("userInfo.json", "w", encoding="utf-8") as file:
              json.dump(personInfo, file, indent=4,ensure_ascii=False)
             input("Press enter to return to menu")
           else:  
            print("Insufficent funds")
      else:
        print("Users name does not match") 
    else:     
      print("You cannot send money to yourself")
  else:
    print("Wrong id")
    return False


def createUser():   
    userName = input("Enter your name (without ı,ş,ğ,ç,ö,ü): ")
    userSurname = input("Enter your surname (without ı,ş,ğ,ç,ö,ü): ")
    
    user_id = str(random.randint(2100,2999))
    while user_id in personInfo:
        user_id = str(random.randint(2100,2999))

    password = int(input("Create your password (numbers only): "))
    initial_balance = int(input("Enter your initial deposit: "))

    personInfo[user_id] = {
      "name" : userName,
      "surName" : userSurname,
      "password": password,
      "balance": initial_balance
    }

    with open("userInfo.json", "w", encoding="utf-8") as file:
        json.dump(personInfo, file, indent=4,ensure_ascii=False)
    print("Your account has been created successfully!")
    input(f"Your id is {user_id}, press enter to continue")
    
def changePass(user_Id):
 user = personInfo[user_Id]
 ope = ""
 newPass = 0
 while True: 
  password = int(input("Enter your current password: "))  
  if password == user["password"]:
    newPass = int(input("Enter your new password(Only enter numbers): "))
    if newPass != user["password"]: 
      newPass2 = int(input("Enter it again: "))  
      if newPass == newPass2:
       user["password"] = newPass
       input("Your new password has been created press enter to return to main menu ")
       with open("userInfo.json", "w", encoding="utf-8") as file:
         json.dump(personInfo, file, indent=4,ensure_ascii=False)
       return
      else: 
       ope = input("Passwords do not match press enter to try again or press 0 to return to main menu")
      if ope == "0" :
       return
    else:
     ope = input("Your new password cannot be same as your last password")    
  else:
    ope = input("Your password is wrong press enter to try again or press 0 to return to main menu")  
    if ope == "0" :
       return
    
        
      
      
   
  
   




 

    


   
  

 

