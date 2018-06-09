#These is a program that helps in troubleshooting a computer problem
#It receives users input 'n' or 'y' to communicate

print('Help! My computer is not working')
print('Is it making any noise (fan etc)')
choice=input('Or show any lights (y/n)')

#The troubleshooting control logic

if choice == 'n': #No power
    choice = input('Is the power cable pluged in (y/n)')
    if choice == 'n': #Not pluged in Plug it in
        print('Plug the cable in if the problem persist')
        print('Please run the program in')
    else: #pluged in
        choice = input('Does the cable have any faults (y/n)')
        if choice == 'y': #The cable have faults
            print('Please replace the cable or fix it if the problem persist')
            print('Then run the program again')
        else: #The cable is ok
            choice = input('Is the switch in on position ?  (y/n)')
            if choice == 'n': #Its not in on position
                print('Put the switch on and if the problem persists')
                print('Then run the program again')
            else: #Switch is ok
                choice= input('Does the cable have a fuse?  (y/n)')
                if choice == 'n': # There is a fuse
                    print('Please insert a fuse')
                    if choice == 'y':
                        choice=input('Is the fuse okay?  (y/n)')
                        if choice == 'n': # Replace the fuse
                            print('Please replace the fuse')
                        else: #The fuse is okay
                            print("Please consult a service technician.")
else:
    print("Please consult a service technician.")