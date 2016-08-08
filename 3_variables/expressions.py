import random

print("This game will test how well you know Boolean Expressions with numbers!\n")
while True:
    rand_1 = random.randint(0, 100)
    rand_2 = random.randint(0, 100)
    rand_b = bool(random.getrandbits(1))
    user_input = input("A: %s  B: %s  Quit with 'Q'; What is the right operator to make this %s (<, >, ==)? " % (rand_1, rand_2, rand_b))

    if str(user_input).lower() == "q":
        exit()

    if str(user_input) not in ['<', '>', '==']:
        print("Not a valid choice")
    elif rand_1 > rand_2 and str(user_input) == ">" and rand_b:
        print("Correct!")
    elif rand_1 > rand_2 and str(user_input) != ">" and not rand_b:
        print("Correct!")
    elif rand_1 < rand_2 and str(user_input) == "<" and rand_b:
        print("Correct!")
    elif rand_1 < rand_2 and str(user_input) != "<" and not rand_b:
        print("Correct!")
    elif rand_1 == rand_2 and str(user_input) == "==" and rand_b:
        print("Correct!")
    elif rand_1 == rand_2 and str(user_input) != "==" and not rand_b:
        print("Correct!")
    else:
        print("Sorry that isn't right :(")
    print()
