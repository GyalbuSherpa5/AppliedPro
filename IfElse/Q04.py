#4. A Character Is an Alphabet or Not
ch=input("Enter the character to check")
if( (ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(f"The given character,{ch} is an alphabet")
else:
   print(f"The given character,{ch} is not an alphabet")