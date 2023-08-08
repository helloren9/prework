# Question 1

def hello_name(user_name):
    return "hello_" + user_name.upper() + "!"

print(hello_name("python"))

# Question 2

def first_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)

print(first_odds())

# Question 3

def max_num_in_list(a_list):
    m = max(a_list)
    return m

print(max_num_in_list([10, 20, 30, 40, 50]))

# Question 4

def is_leap_year(a_year):
    if a_year % 400 == 0 and a_year % 100 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

print(is_leap_year(2020))

# Question 5

def is_consecutive(nums):
    return sorted(nums) == list(range(min(nums), max(nums) + 1))

print(is_consecutive([4, 5, 6, 7, 8]))

