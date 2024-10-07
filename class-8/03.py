ls = [
    [1,2,3],
    [10,20,30],
    [100,200,300],
]

# print(ls[0][0], ls[0][1], ls[0][2])
# print(ls[1][0], ls[1][1], ls[1][2])
# print(ls[2][0], ls[2][1], ls[2][2])

for i in ls:
    for j in i:
        print(j , end=',')
    
    print()

# Home work: Remove trailing comma from each line
'''
1,2,3,
10,20,30,
100,200,300,
'''