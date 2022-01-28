from functools import reduce


# 31.
# N = 5
# user_set = set()
# mult = 1
# for i in range(N):
#     user_set.add(mult)
#     mult *= (-3)
# print(user_set)

# N = 10
# user_set = set((-3) ** i for i in range(N))
# print(user_set)


# 32
# N = 5
# user_dict = {k: 3*k +1 for k in range(1, N+1)}
# print(user_dict)

# 33
# str_1 = "к"
# str_2 = "крокодил кушает курицу"
# print(str_2.count(str_1))

# 34
# float_number = 3.145
# sum_result = reduce(lambda a, b: a + b, [int(i) if i.isdigit() else 0 for i in str(float_number)])
# print(sum_result)

# 35
# N = 5
# lst = []
# mult = 1
# for i in range(1, N + 1):
#     lst += [i * mult]
#     mult = i * mult
# print(lst)

