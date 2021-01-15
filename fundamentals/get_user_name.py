# program says gets users' name and says hello


def say_hello():
    get_name = input('What is your name?: ')
    birth_year = input('What year were you born in?: ')
    length_of_name = len(get_name)
    print(f'Hello, {get_name}! Your name is {length_of_name} characters long.')
    print(f'You are {2021 - int(birth_year)} years old')


say_hello()