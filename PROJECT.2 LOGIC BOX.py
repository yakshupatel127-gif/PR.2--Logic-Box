print("hello how are you , welcome ")

while True:
    print("\nselect an option:")
    print("1. generate a pattern")
    print("2. analyze a range of numbers")
    print("3. exite")

    choice = input("enter your choice: ")

    if choice == "1":
        rows = int(input("enter number of rows: "))

        if rows <=0:
            print("invalid number")
        else:
            print("\npattern")
            for i in range(1 , rows + 1):
                print("*" * i)

    elif choice == "2":
        start = int(input("enter start number: "))
        end  = int(input("enter end number: "))

        Total = 0
        print()

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, "is even")
            else:
                print(num, "is odd")
            Total = Total + num

            print("\nsum of all numbers:", Total)
    elif choice == "3":
        print("\nexiting the program, have a good day")

        break
    else:
        print("invalid choice , plzz try one more time")
