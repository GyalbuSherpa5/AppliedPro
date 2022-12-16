#5. Uppercase, Lowercase, Special Character, or Digit
ch=input("Enter a character.")
if(ch>='0'and ch<='9'):
    print("Digit")
elif ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Special Character")