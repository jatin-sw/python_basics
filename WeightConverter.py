def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

weight = input("Weight: ")

if not isNumber(weight):
    print("Enter weight in numeric format!")
else:
    unit = input("(L)bs or (K)gs: ")

    if unit.upper() == 'L':
        converted_weight = float(weight) * 0.45
        print(f'You are {round(converted_weight)} Kgs!')
    elif unit.upper() == 'K':
        converted_weight = float(weight) / 0.45
        print(f'You are {round(converted_weight)} Lbs!')
    else:
        print("Enter proper unit!")