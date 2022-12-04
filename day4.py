with open("day4.in") as file:
    data = [i for i in file.read().strip().split("\n")]

#['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

for i in range(len(data)):
    data[i] = data[i].split(",")
    for j in range(len(data)[i]):

        #[['2-4', '6-8'], ['2-3', '4-5'], ['5-7', '7-9'], ['2-8', '3-7'], ['6-6', '4-6'], ['2-6', '4-8']]


def check(li):
