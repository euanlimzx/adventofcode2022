with open("day5.in") as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

intel = []
for i in range(len(data)):
    temp = []
    for j in range(len(data[i])):
        temp.append(data[i][j])
    intel.append(temp)

bigintel = []

for i in range(len(intel)):
    temp = []
    e = intel[i].index("e")
    f = intel[i].index("f")
    r = intel[i].index("r")
    t = intel[i].index("t")
    temp.append(int("".join(intel[i][e+2:f-1])))
    temp.append(int("".join(intel[i][r+4:t-1])))
    temp.append(int("".join(intel[i][t+3:])))
    bigintel.append(temp)

for i in bigintel:
    print(i)

 #   [D]
#[N] [C]
#[Z] [M] [P]
# 1   2   3
#stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

#[M] [H]         [N]
#[S] [W]         [F]     [W] [V]
#[J] [J]         [B]     [S] [B] [F]
#[L] [F] [G]     [C]     [L] [N] [N]
#[V] [Z] [D]     [P] [W] [G] [F] [Z]
#[F] [D] [C] [S] [W] [M] [N] [H] [H]
#[N] [N] [R] [B] [Z] [R] [T] [T] [M]
#[R] [P] [W] [N] [M] [P] [R] [Q] [L]
# 1   2   3   4   5   6   7   8   9

stacks = [
    list("RNFVLJSM"),
    list("PNDZFJWH"),
    list("WRCDG"),
    list("NBS"),
    list("MZWPCBFN"),
    list("PRMW"),
    list("RTNGLSW"),
    list("QTHFNBV"),
    list("LMHZNF")
]

for ins in bigintel:
    num = ins[0]
    frm = ins[1]-1
    to = ins[2]-1
    for i in range(num):
        var = stacks[frm].pop()
        stacks[to].append(var)

#[['C'], ['M'], ['P', 'D', 'N', 'Z']]

ans = []
for j in stacks:
    var = j.pop()
    ans.append(var)

print("".join(ans))
