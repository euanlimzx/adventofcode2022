with open("day1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

data.append("")
currsum=0
li=[]


for i in data:
    if i == "":
        if len(li)<3:
            li.append(currsum)
        else:
            if currsum > min(li):
                li.append(currsum)
                li.remove(min(li))
        print(li)
        currsum=0
    else:
        i=int(i)
        currsum+=i

answer=0
for i in li:
    answer+=i
print(answer)