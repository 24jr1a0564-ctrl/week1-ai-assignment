from datetime import datetime

name = input("Enter your name: ")

print("Hello", name)

while True:

    print("\n1. Study Tip")
    print("2. Motivation Quote")
    print("3. Date and Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = "Practice coding every day."
        print(tip)

        file = open("output.txt", "a")
        file.write(tip + "\n")
        file.close()

    elif choice == "2":
        quote = "Never give up."
        print(quote)

        file = open("output.txt", "a")
        file.write(quote + "\n")
        file.close()

    elif choice == "3":
        time = str(datetime.now())
        print(time)

        file = open("output.txt", "a")
        file.write(time + "\n")
        file.close()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Wrong choice")