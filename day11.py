import math
with open("day11.in") as file:
    data = [i for i in file.read().strip().split("\n")]

monkeys = []


class Monkey():
    def __init__(self, index, items, ops, test, truetest, falsetest):
        self.index = index
        self.items = items
        self.ops = ops
        self.test = test
        self.truetest = truetest
        self.falsetest = falsetest
        self.times = 0


for i in range(0, len(data), 7):
    index = int(data[i][-2])
    items = data[i+1][18:]
    items = [int(item) for item in items.split(',') if item]
    ops = data[i+2][19:]
    test = int(data[i+3][21:])
    truetest = int(data[i+4][-1])
    falsetest = int(data[i+5][-1])
    monkey = Monkey(index, items, ops, test, truetest, falsetest)
    monkeys.append(monkey)
    # print(index)
    # print(items)
    # print(ops[4])
    # print(test)
    # print(truetest)
    # print(falsetest)

# for each monkey in monkeys
    # for each item in monkey
    # conduct ops and append to relevant monkey
gcd = 1
for monkey in monkeys:
    gcd *= monkey.test

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.times += 1
            #print("for monkey ", monkey.index, "checking", item)
            operator = monkey.ops[4]
            #print("operator is ", operator)
            if monkey.ops[6].isdigit():
                value = int(monkey.ops[6:])
            else:
                value = item
            #print("value is ", value)
            worry = 0
            if operator == "*":
                worry = value * item
            elif operator == "+":
                worry = value + item
            #print("new worry level after operation is", worry)
            if worry % monkey.test == 0:
                monkeys[monkey.truetest].items.append(worry % gcd)
                #print("item sent to", monkeys[monkey.truetest].index)
            else:
                monkeys[monkey.falsetest].items.append(worry % gcd)
                #print("item sent to", monkeys[monkey.falsetest].index)
            # print()
        monkey.items.clear()

business = []
for monkey in monkeys:
    business.append(monkey.times)

maxone = max(business)
business.remove(maxone)
maxtwo = max(business)

print(maxone*maxtwo)
