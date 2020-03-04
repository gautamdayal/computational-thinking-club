# import math
# import random
#
#
# def get_time(x):
#     y = 2 * math.pi * math.sqrt(x/9.81)
#     return y + random.random() * y/10
#
#
# L = [0.1, 0.2, 0.3]
# T = []
# for x in L:
#     y = []
#     for i in range(4):
#         y.append(round(get_time(x), 2))
#     T.append(y)
# print(T)

pi = 3.14159
g = 9.81

raw_data = [[0.65, 0.66, 0.67, 0.64], [0.98, 0.96, 0.91, 0.94], [1.16, 1.12, 1.11, 1.19]]
X = []
for tSet in raw_data:
    S = 0
    for T in tSet:
        S += (T**2 / (4 * pi**2)) * g
    X.append(S/len(tSet))
print(X)
