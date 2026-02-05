def random_user_id():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

print(random_user_id())

def user_id_gen_by_user():
    import random
    import string
    characters = int(input("Enter the number of characters: "))
    ids = int(input("Enter the number of ids: "))
    for i in range(ids):
        return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(characters)))

print(user_id_gen_by_user()) # user_id_gen_by_user()

def  rgb_color_gen():
    import random
    return 'rgb({},{},{})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print(rgb_color_gen())

def list_of_hexa_colors():
    import random
    import string
    return ['#' + ''.join(random.choice(string.hexdigits) for _ in range(6)) for _ in range(6)]

print(list_of_hexa_colors())

def list_of_rgb_colors():
    import random
    return ['rgb({},{},{})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(6)]

print(list_of_rgb_colors())

def generate_colors(color_type, count):
    import random
    import string
    if color_type == 'hexa':
        return ['#' + ''.join(random.choice(string.hexdigits) for _ in range(6)) for _ in range(count)]
    elif color_type == 'rgb':
        return ['rgb({},{},{})'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(count)]
    else:
        return 'Invalid string'

print(generate_colors('hexa', 6))
print(generate_colors('rgb', 6))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 1))


def suggle_list(list):
    import random
    random.shuffle(list)
    return list

def array_of_seven_unique_random_numbers():
    import random
    return random.sample(range(10), 7)

print(array_of_seven_unique_random_numbers())



