def password():
    import random

    name=input("Please enter your name and sirname without any space :").lower()
    password_name = ""
    password_length_name = 3
    for x in range(password_length_name):
        password_name += random.choice(name)

    numbers = "0123456789"
    password_num= ""
    password_length_num = 4
    for x in range(password_length_num):
        password_num += random.choice(numbers)

    password = password_name + password_num
    print(password)


password()