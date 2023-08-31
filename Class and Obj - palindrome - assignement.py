class check_palindrome:         # Define a class
  string=input(("Enter a string:"))     # Assigning an attribute


  def palindrome(self):           # Check Palindrome
    if(self.string == self.string[::-1]):
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
  check = check_palindrome()      # Create Object for Check_palindrome Class

check.palindrome()                # Accessing the logic of Palindrome using object.method()