#20. Input any alphabet and check whether it is vowel or consonant.
ch = input("Enter a character \n")
ch=ch.lower()
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("It is vowel")
else:
    print("It is consonant")