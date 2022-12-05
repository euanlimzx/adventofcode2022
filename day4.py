with open("day4.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

big = []
for i in range(len(data)):
    data[i] = data[i].split(",")
    coom = []
    for j in range(len(data[i])):
        var = []
        for k in range(len(data[i][j])):
            if data[i][j][k].isalnum():
                var.append(data[i][j][k])
            else:
                coom.append(int("".join(var)))
                var = []
        coom.append(int("".join(var)))
    big.append(coom)
#big = [['23', '42', '65', '86'], ['2', '3', '4', '5'], ['5', '7', '7', '9'], ['2', '8', '3', '7'], ['6', '6', '4', '6'], ['2', '6', '4', '8']]

# bu = big upper, bl = biglower , su, sl

sum = 0


def check(li):
    if li[1]-li[0] >= li[3]-li[2]:
        bl = li[0]
        bu = li[1]
        sl = li[2]
        su = li[3]
    else:
        bl = li[2]
        bu = li[3]
        sl = li[0]
        su = li[1]
    if bl <= sl and bu >= su:
        return 1
    else:
        return 0


for j in big:
    sum += check(j)

print(sum)

# part 2 is just checking whether li[0] or li[2] is higher, and doing accordingly
