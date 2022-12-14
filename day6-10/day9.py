import math
with open("day9.in") as file:
    data = [i for i in file.read().strip().split("\n")]

#data ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']

# might wanna make this per grid


def newheadpos(pos, str):
    x = pos[0]
    y = pos[1]
    if str[0] == "R":
        x += 1
    elif str[0] == "L":
        x -= 1
    elif str[0] == "U":
        y += 1
    elif str[0] == "D":
        y -= 1
    position = (x, y)
    return position


# position = (0, 0)
# for i in data:
#     position = move(position, i)
#     print(position)

def newtailpos(tail, head):
    tailx = tail[0]
    taily = tail[1]
    headx = head[0]
    heady = head[1]
    if abs(tailx-headx) <= 1 and abs(taily - heady) <= 1:
        return tail
    elif tailx == headx and taily != heady:
        taily = (heady+taily)//2
    elif taily == heady and headx != tailx:
        tailx = (headx+tailx)//2
    else:
        if tailx < headx:
            tailx = tailx+1
        else:
            tailx = tailx-1
        if taily < heady:
            taily = taily+1
        else:
            taily = taily-1
    tail = (tailx, taily)
    return tail


positions = []


def eachmove(headposition, tailpos1, tailpos2, tailpos3, tailpos4, tailpos5, tailpos6, tailpos7, tailpos8, tailpos9, instructions):
    for onemove in instructions:
        times = int("".join(onemove[2:]))
        for i in range(times):
            headposition = newheadpos(headposition, onemove)
            # update position of head
            tailpos1 = newtailpos(tailpos1, headposition)
            tailpos2 = newtailpos(tailpos2, tailpos1)
            tailpos3 = newtailpos(tailpos3, tailpos2)
            tailpos4 = newtailpos(tailpos4, tailpos3)
            tailpos5 = newtailpos(tailpos5, tailpos4)
            tailpos6 = newtailpos(tailpos6, tailpos5)
            tailpos7 = newtailpos(tailpos7, tailpos6)
            tailpos8 = newtailpos(tailpos8, tailpos7)
            tailpos9 = newtailpos(tailpos9, tailpos8)
            positions.append(tailpos9)


eachmove((0, -5),  (0, -5), (0, -5), (0, -5), (0, -5),
         (0, -5), (0, -5), (0, -5), (0, -5), (0, -5), data)

print(len(set(positions)))
