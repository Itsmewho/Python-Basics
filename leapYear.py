year = int(input("Give A year as a input and ill check if its a leapyear or not!\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leapyear!")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
