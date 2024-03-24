
import random
import string

def password():
    global length
    length=int(input("Enter the length of the password : "))
    if length<8:
        print("Password length should contain atleast 8 characters")
        password()

def inputs():
      print("Please choose either 'YES' or 'NO'.")
      lower=input("Do you need lowercase leters in your password? :").lower()=='yes'
      upper=input("Do you need uppercase leters in your password? :").lower()=='yes'
      special=input("Do you need special characters in your password? :").lower()=='yes'
      digits=input("Do you need digits in your password? :").lower()=='yes'
      if not(lower or upper or special or digits):
        print("Please select atleast one option as 'yes' to generate your password.")
        inputs()


      char=""

      if lower:
       char+=string.ascii_lowercase
      if upper:
       char+=string.ascii_uppercase
      if special:
       char+=string.punctuation
      if digits:
       char+=string.digits
      password1="".join(random.choice(char) for i in range(length))
      print("Password generated is : ",password1)


#driver code
password()
inputs()
