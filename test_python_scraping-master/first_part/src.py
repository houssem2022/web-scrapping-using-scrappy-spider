def exercise_one():
    for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("ThreeFive")
    elif num % 3 == 0:
        print("Three")
    elif num % 5 == 0:
        print("Five")
    else:
        print(num)

