with open("day10.in") as file:
    data = [i for i in file.read().strip().split("\n")]

sprite = []
for i in range(40):
    sprite.append(".")

x = 1
cycle = 0
xpositions = [1]
for i in range(len(data)):
    if data[i][0] == "n":
        cycle += 1
        xpositions.append(x)
        # print("At the end of cycle ", cycle, ": X is ", x)
    elif data[i][0] == "a":
        cycle += 1
        xpositions.append(x)
        # print("At the end of cycle ", cycle, ": X is ", x)
        cycle += 1
        x += int(data[i][5:])
        xpositions.append(x)
        # print("At the end of cycle ", cycle, ": X is ", x)

# print(len(xpositions))

for i in range(6):
    sprite = []
    for x in range(40):
        sprite.append(".")
    for j in range(40):
        val = abs(j-xpositions[j + 40*i])
        # print("end of cycle:", j+1+40*i,
        #       "CRT is drawing at:", j,
        #       "position of x is:", xpositions[j+40*i])
        if val <= 1:
            sprite[j] = "#"
    print(sprite)
# part ONE answer
# with open("day10.in") as file:
#     data = [i for i in file.read().strip().split("\n")]

# stack = [20, 60, 100, 140, 180, 220]
# x = 1
# cycle = 0
# ans = []
# for i in range(len(data)):
#     if data[i][0] == "n":
#         cycle += 1
#         if cycle == stack[0]:
#             signal = cycle * x
#             stack.pop(0)
#             ans.append(signal)
#             if len(stack) == 0:
#                 break
#     elif data[i][0] == "a":
#         # add
#         cycle += 1
#         if cycle == stack[0]:
#             signal = cycle * x
#             stack.pop(0)
#             ans.append(signal)
#             if len(stack) == 0:
#                 break
#         cycle += 1
#         if cycle == stack[0]:
#             signal = cycle * x
#             stack.pop(0)
#             ans.append(signal)
#             if len(stack) == 0:
#                 break
#         x += int(data[i][5:])

# sum = 0
# for i in ans:
#     sum += i
# print(sum)
