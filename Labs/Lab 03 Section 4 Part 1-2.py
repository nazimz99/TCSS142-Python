#Nazim Zerrouki
n = int(input("Enter your eye score. "))
print("Your eye score is", n)
if n in range (9, 50):
    if n <= 30:
        print("You see well.")
    elif n > 30 and n < 50:
        print("You don't see very well.")
        if n <= 40:
            print("You can get a driver's license!")
        if n >= 45:
            print("You need glasses.")
elif n in range (0, 8):
    print("You are not human!")
elif n >= 200:
    print("You are legally blind!")
else:
        print("invalid eye score was entered")

