cha = input("Please enter a character: ")
if len(cha) > 1:
    print("only 1 character is allowed")
    exit(0)

a = ord(cha)

if 96 < a <= 122:
    print(cha,end=" ")
    print("is a small case letter and its capital letter is ",cha.swapcase())
elif 64 < a <= 90:
    print(cha,end=" ")
    print("is a capital letter and its small case letter is ",cha.swapcase())
elif 47 < a <= 57:
    print(cha,end=" ")
    print("is a numeric character")
else:
    print("err")
