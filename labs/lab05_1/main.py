# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
J Williams CS 31 Oct 28 2026

import nameformat
nameformat.hello_world()

def main():
  #program Title 
  print("Welcome to My Name Format Module")
  print()
  # ask for first/last name
firstName = input("What is your first name?")
lastName = input("What is your last name?")

# Menu System
while True:
  print("1 - Say Hello")
  print("2 - Output Full Name ")
  print("3 - Output Last name,First Name")
  print ("4 - Read Module Documentation")
  print("5 - Exit Program")
  choice = input("What would you like to do? ")

# if else block baseed on choice input 
if choice == "1" :
  # call sayHello
  name.format.sayHello(firstName)
elif choice == "2":
  name.format.fullName(firstName, lastName)
elif choice == "3":
  name.format.lastNameFirst(firstName, lastName)
elif choice == 4:
  print("Documentaion Placeholder")
elif choice == 5:
  print("Thank you for using our program.")
  break
else:
  print("Sorry thats not Quite what I asked for lets try again")


if __name__ == "__main__":
  main()
  

  




