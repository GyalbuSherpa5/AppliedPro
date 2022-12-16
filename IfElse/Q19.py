#19. Check whether a character is an alphabet or not
ch=input("Enter the character to check")
if( (ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(f"The given character,{ch} is an alphabet")
else:
   print(f"The given character,{ch} is not an alphabet")