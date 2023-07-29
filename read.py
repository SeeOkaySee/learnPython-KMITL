num = eval(input("enter number: "))
if type(num) == float:
    a = str(input("float or scientific: "))
    if a == "float":
        print(format(num,"5.4f"))
    elif a == "scientific":
        print(format(num,"5.4e"))
    else:
        print("err")
elif type(num) == int:
    b = str(input("binary,octal,hexadecimal,or decimal: "))
    if b == "binary":
        print(format(num,"b"))
    elif b == "octal":
        print(format(num,"o"))
    elif b == "hexadecimal":
        print(format(num,"x"))
    elif b == "decimal":
        print(format(num,"3d"))
    else:
        print("err")
else:
    print("err")