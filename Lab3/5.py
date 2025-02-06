from itertools import permutations

def print_permutations(s):
    per_list = permutations(s)
    for perm in per_list:
        print("".join(perm))


user_input = input()
print_permutations(user_input)
