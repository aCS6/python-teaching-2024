
# Dummy sorting function
persons = [
    ('Shakib', 15), # 0 -> (0,1) -> sort key = 1
    ('Maruf', 25), # 1 -> (0,1) -> sort key = 1
    ('Asif', 7) # 2 -> (0,1) -> sort key = 1
]
ls = [
    ['a' , 'b' , 50 , 'w'],
    ['c' , 'd' , 45 , 'x'],
    ['e' , 'f' , 70, 'z'],
]

def get_index(item):
    print("from get_index" , item)

# for i in persons:
#     get_index(i)


def my_sorting_function(a_list , key):

    for i in a_list:
        key(i)

# my_sorting_function(persons, key=get_index)
my_sorting_function(ls, key=get_index)

