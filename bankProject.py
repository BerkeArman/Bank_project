personInfo = {
"name":  ["Berke","Nesil","Rıfkı","Kylo"],
"surName": ["Arman", "Uludağ","Kuş","Arman"],
"id": [2334,2335,2336,2337],
"Balance": [2000200,30000000,3000,45000],
"Password": [1234,1235,1236,1237]
}
Id = personInfo["id"]
name = personInfo["name"]
print("###########BANK###########")


 

def Id_check(Id):
 
 
 if Id in personInfo["id"]:
     i = personInfo["id"].index(Id)
     password = int(input("Enter your password: "))
     if password == personInfo["Password"][i]:
      print("Welcome" + " " +personInfo["name"][i]+ " " + personInfo["surName"][i])
      print("Account balance:"+ " "+str(personInfo["Balance"][i]))
      print("                        ")
      print("Enter 1 to Whitdraw money")
      print("                       ")
      print("Enter 2 to Deposit money")
      print("                        ")
      print("Enter 3 to send money")
      print("")
      print("Enter 4 to exit")
      return True
 
     else:
       print("Password is wrong try again")  
       return False

 else:
    print("Wrong id")
    return False
    


def whitdraw(Id):  
  i = personInfo["id"].index(Id) 
  ammount = int(input( "Enter the amount you want to withdraw: "))
  if ammount < personInfo["Balance"][i]:
   personInfo["Balance"][i] = personInfo["Balance"][i]-ammount
   print("Your new balance is "+ " "+str(personInfo["Balance"][i]))
  else:
    print("Insufficient balance")


def deposit(Id):
  i = personInfo["id"].index(Id) 
  ammount = int(input( "Enter the amount you want to : "))
  personInfo["Balance"][i] = personInfo["Balance"][i] + ammount
  print("Your new balance is "+ " "+str(personInfo["Balance"][i]))


def transfer(id,Id2):
  i = personInfo["id"].index(id)
  
  reciever = personInfo["id"].index(Id2)
  
  if Id2 in personInfo["id"]:
    if i != reciever:
      user_name = input("Enter name of the reciever: " )
    
      if user_name in personInfo["name"]:
       y = personInfo["name"].index(user_name) 
       if y ==  reciever:
         if y != i:
     
           amount = int(input("Enter the amount you want to send: "))
           if amount < personInfo["Balance"][i]:
       
            personInfo["Balance"][i] = personInfo["Balance"][i] - int(amount)
            personInfo["Balance"][reciever] = personInfo["Balance"][reciever]+int(amount)
            print("Your new balance is "+ " "+ str(personInfo["Balance"][i]))
           else:  
            print("Insufficent funds")
         else:
           print("You cannot send money to yourself")
       else:
         print("Users name does not match") 
      else:
        print("Users name does not match") 
    else:     
      print("You cannot send money to yourself")
  else:
    print("Wrong id")
   





user_id = int(input("Enter your Id: "))

i =3 
if Id_check(user_id)== True : 
 operation = int(input("Select your operation: "))
 while(operation != 1 or operation != 2 or operation != 3 or operation !=4):
  
     if operation == 1:
      whitdraw(user_id)
      break
     elif operation == 2:
      deposit(user_id)
      break
  
     elif operation == 3:  
      user_id2 = int(input("Enter the id of the reciever: "))
      transfer(user_id,user_id2)
      break
     
     elif operation == 4:
       print("You have exited from your account")
       break
       
     
     elif i == 0:
      break
    
     else:  
      print("Tries left"+ " "+str(i))
      input("You entered the wrong operator enter again: ")
       
      i-=1

  
   




 

    


   
  

 

