import math


def calculate_vector_from_points(a, b):
    return b[0] - a[0], b[1] - a[1], b[2] - a[2]

def scalar_multiply_vectors(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vector_multiply_vectors(a, b):
    return a[1] * b[2] - a[2] * b[1], -1 * (a[0] * b[2] - a[2] * b[0]), a[0] * b[1] - a[1] * b[0]

def vector_module(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])

def calculate_angle_between_vectors(a, b):
    cos = scalar_multiply_vectors(a, b) / (vector_module(a) * vector_module(b))
    return math.degrees(math.acos(cos))

def calculate_cos_between_vectors(a, b):
    return scalar_multiply_vectors(a, b) / (vector_module(a) * vector_module(b))


fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

v = tuple(map(float, fin.readline().split(' ')))
v = v + (0,)
a = tuple(map(float, fin.readline().split(' ')))
a = a + (0,)
m = tuple(map(float, fin.readline().split(' ')))
m = m + (1,)
w = tuple(map(float, fin.readline().split(' ')))
w = w + (0,)

cannon_left = vector_multiply_vectors((0, 0, 1), a)
cannon_right = vector_multiply_vectors(a, (0, 0, 1))

mast_angle = calculate_angle_between_vectors(m, (0, 0, 1))

last_word = "Laby ot MA kryto!"

enemy_vector = calculate_vector_from_points(v, w)

cannon_angle_left = calculate_angle_between_vectors(cannon_left, enemy_vector)
cannon_angle_right = calculate_angle_between_vectors(cannon_right, enemy_vector)
cannon_cos_left = calculate_cos_between_vectors(cannon_left, enemy_vector)
cannon_cos_right = calculate_cos_between_vectors(cannon_right, enemy_vector)

result = ""
side = 0
cannon_angle = 0.0;

mast_angle_to_enemy = 0

if calculate_angle_between_vectors(enemy_vector, a) > 90:
    cannon_angle_left *= -1
    cannon_angle_right *= -1

if -60 < cannon_angle_right < 60:
    # cannon_angle = round(cannon_angle_right, 2)
    # side = -1
    result += "-1\n" + str(round(cannon_angle_right, 2)) + '\n'
    mast_angle_to_enemy = calculate_angle_between_vectors(m, (cannon_right[0], cannon_right[1], 0))
    # print(round(cannon_angle_right, 2))
elif -60 < cannon_angle_left < 60:
    # cannon_angle = round(cannon_angle_left, 2)
    # side = 1
    result += "1\n" + str(round(cannon_angle_left, 2)) + '\n'
    mast_angle_to_enemy = calculate_angle_between_vectors(m, (cannon_left[0], cannon_left[1], 0))
    # print(round(cannon_angle_left, 2))
else:
    # side = 0
    result += "0\n"
    # print(0)

if mast_angle_to_enemy < 90:
    mast_angle *= -1

result = result + str(round(mast_angle, 2)) + '\n'
# print(round(mast_angle, 2))

result = result + last_word
# print(last_word)
fout.write(result)
