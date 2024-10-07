persons = [
    ('Shakib', 15), # 0 -> (0,1) -> sort key = 1
    ('Maruf', 25), # 1 -> (0,1) -> sort key = 1
    ('Asif', 7) # 2 -> (0,1) -> sort key = 1
]

SORT_KEY = 1
def get_index(item):
    print("full item ", item)
    print("sort index ", SORT_KEY)

    x = item[SORT_KEY]
    print("value ", x)

    print("---------------------------")
    return x

for i in persons:
    print(get_index(i))