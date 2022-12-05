with open("day2.in") as file:
    data = [i for i in file.read().strip().split("\n")]

#to achieve a certain outcome, when opponent plays key, we play value
win = {"A":"B","B":"C","C":"A"}
draw = {"A":"A","B":"B","C":"C"}
lose = {"A":"C","B":"A","C":"B"}

point={"A":1,"B":2,"C":3}

det = {"X":"lose","Y":"draw","Z":"win"}

#first, we see whether we need to win lose or draw
#then, we determine what we play
# then, we calculate what we play + result

def strat(str):
    d=det[str[2]]
    if d=="draw":
        sum=point[draw[str[0]]]
        return sum + 3
    if d=="win":
        sum=point[win[str[0]]]
        return sum + 6
    if d=="lose":
        sum=point[lose[str[0]]]
        return sum 

total=0
for i in data:
    total+=strat(i)

print(total)
