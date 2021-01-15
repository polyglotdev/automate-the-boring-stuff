# program says gets users' name and says hello


def say_hello():
    get_name = input('What is your name?: ')
    length_of_name = len(get_name)
    print(f'Hello, {get_name}! Your name is {length_of_name} characters long.')


say_hello()