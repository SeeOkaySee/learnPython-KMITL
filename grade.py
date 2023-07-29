g = eval(input("Enter score: "))

if 80 <= g <= 100: 
    print("your grade : A")
elif 70 <= g < 80: 
    print("your grade : B")
elif 60 <= g < 70: 
    print("your grade : C")
elif 50 <= g < 60: 
    print("your grade : D")
elif 0 <= g < 50 :
    print("your grade : F")
else:
    print("err")
