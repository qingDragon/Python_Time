

_age_of_SB = 56


while True:
    age_of_SB = int(input("age_of_SB:"))
    if age_of_SB == _age_of_SB :
        print("You get true answer...")
        break
    elif age_of_SB > _age_of_SB:
        print("think smaller...")
    else:
        print("think bigger!")