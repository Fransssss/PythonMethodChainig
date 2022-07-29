# author: Fransiskus Agapa
from computer import Computer

print("\n== Basic Use of Computer ==")
print("1. Press power button ")
print("2. Refresh computer")
print("3. Open a file")
print("4. Work on a file")
print("5. Close file")
print("6. Turn off computer")
print("E. Exit")
choice = input("choice: ")

#----
basic_computer = Computer()
comp_is_on = False             # condition to state that computer is on
comp_is_off = False

while choice != 'e' and choice != 'E':
    if choice == '1':
        print('\n')
        comp_is_on = True
        comp_is_off = False
        basic_computer.press_on_off().turn_on()

    elif choice == '2':
        print('\n')
        if comp_is_on:
            basic_computer.refresh()
        else:
            print("[ You have to turn on the computer first ]")

    elif choice == '3':
        print('\n')
        if comp_is_on:
            basic_computer.open_file()
        else:
            print("[ You have to turn on the computer first ]")

    elif choice == '4':
        print('\n')
        if comp_is_on:
            basic_computer.work_on_file()
        else:
            print("[ You have to turn on the computer first ]")

    elif choice == '5':
        print('\n')
        if comp_is_on:
            basic_computer.close_file()
        else:
            print("[ You have to turn on the computer first ]")

    elif choice == '6':
        print('\n')
        if not comp_is_off:
            if comp_is_on:
                refresh_comp = input("Would you like to refresh the computer first: (yes/no) ").lower()     # make user input in lower case
                if refresh_comp == "yes":
                    print('\n')
                    basic_computer.refresh().turn_off()
                    comp_is_off = True
                else:
                    print('\n')
                    basic_computer.turn_off()
                    comp_is_off = True
            else:
                print("[ The computer is off ]")
        else:
            print("[ The computer is off ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Basic Use of Computer ==")
    print("1. Press power button ")
    print("2. Refresh computer")
    print("3. Open a file")
    print("4. Work on a file")
    print("5. Close file")
    print("6. Turn off computer")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")
