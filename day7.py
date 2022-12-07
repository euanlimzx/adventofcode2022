import re
with open("day7.in") as file:
    data = [i for i in file.read().strip().split("\n")]


class Node():
    def __init__(self, value, prev=None):
        self.val = value
        self.next = {}
        self.prev = prev


head = Node("head")
currnode = head
for i in data:
    if i[0] == "$":
        if i[2] == "c":
            if i[5] == "/":
                # exit all
                currnode = head
            elif i[5] == ".":
                # going out
                currnode = currnode.prev
            else:
                # entering directory
                currnode = currnode.next["".join(i[5:])]
        elif i[2] == "l":
            # list
            pass
    elif i[0] == "d":
        # directory that has been listed
        dir = Node("".join(i[4:]), currnode)
        currnode.next[dir.val] = dir
    else:
        # file that has been listed
        i = ''.join(filter(str.isdigit, i))
        currnode.next[i] = i

li = []
di = {}


def value(currnode):
    sum = 0
    currnext = currnode.next
    for key in currnext:
        try:
            var = int(key)
            #print("this is an int", key)
            sum += int(currnext[key])
        except ValueError:
            #rint("this is not an int", key)
            sum += value(currnext[key])
    li.append(sum)
    di[sum] = currnode.val

    return sum


value(head)

print(li[-1])

smallest = float("inf")
ans = None
for j in li:
    if j >= li[-1] - 40000000:
        if j < smallest:
            smallest = j
            ans = di[j]

print(ans)
print(smallest)
