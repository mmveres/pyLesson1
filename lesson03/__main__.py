def infinite_sequence():
    num = 0
    while True:
        print("before yield =",num)
        num += 1
        if(num==10): return 10
        yield num

def sequence_10():
    num = 0
    while True:
        print(num)
        num += 1
        if(num==10): return

if __name__ == '__main__':
    iy= infinite_sequence().__iter__()
    print("gen next =", iy.__next__())
    print("gen next =", iy.__next__())
    for it in infinite_sequence():
        print("gen next =", it)
    sequence_10()
