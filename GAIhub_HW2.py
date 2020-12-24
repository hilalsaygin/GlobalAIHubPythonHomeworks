
while True:
        choice=int(input("If you would like to enter new user information choose 1 otherwise 0  "))
        if choice==1:
                info = list()
                info.append(input("Your name:"))
                info.append(input("Your surname:"))
                info.append(int(input("Your age:")))
                info.append(input("Your birth of year:"))
                print("<<< Personal Information >>> ")
                for i in info:
                        print(i)
                if 0 < info[2] < 18:
                        print("You cannot go out because it's too dangerous")
                else:
                        print("You may go out to street")
        else:
                print("Thank you for visiting :) See you next time...")
                break
