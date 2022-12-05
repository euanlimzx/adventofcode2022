with open("day3.in") as file:
    data = [i for i in file.read().strip().split("\n")]

#['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
di = {}

for i in range(len(str)):
    di[str[i]] = i+1


def check(str, di):
    che = {}
    middle = len(str)//2
    for i in range(middle):
        che[str[i]] = str[i]
    for j in range(middle, len(str)):
        try:
            return di[che[str[j]]]
        except KeyError:
            continue


sum = 0
count = 0

for i in data:
    count += 1
    #print(check(i, di))
    sum += check(i, di)

# part 2


def badge(li, di):
    one = set(li[0])
    two = set(li[1])
    three = set(li[2])

    inter = one.intersection(two)
    ans = inter.intersection(three)

    return di[list(ans)[0]]


total = 0
i = 0

while i < len(data):
    total += badge(data[i:i+3], di)
    i = i+3
print(total)
