def some(*args):
    # print(args)

    # print( len(args) )

    if len(args) == 1:
        first = args[0]
        print(first)

some()
some(1)
some(1, 2)
some(1, 2, 3)

