with open("day8.in") as file:
    data = [i for i in file.read().strip().split("\n")]
# 30373
# 25512
# 65332
# 33549
# 35390

sum = 0
di={}
for i in range(len(data)):
    for j in range(len(data[i])):
        tree=data[i][j]
        # left = data[i][j-1]
        # right = data[i][j+1]
        # up = data[i-1][j]
        # down = data[i+1][j]

        