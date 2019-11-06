age_of_GY = 56
count = 0
while count < 3:
    age = int(input("please input the age:"))
    if age < age_of_GY:
        print("think bigger..")
    elif age > age_of_GY:
        print("think smaller..")
    else:
        print("you get it..")
        break
    count += 1
    if count == 3:
        continue_confirm = input("do you want to keep guessing:")
        if continue_confirm != 'n':
            count = 0
