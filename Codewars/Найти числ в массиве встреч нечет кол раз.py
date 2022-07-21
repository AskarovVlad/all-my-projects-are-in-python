def find_it(seq):
    for i in range(len(seq)):
        count = 0
        for j in range(len(seq)):
            if seq[i] == seq[j]:
                count += 1
        if count % 2 != 0:
            print(seq[i])
    return -1


seq = [10, 20, 20, 30, 30, 30, 40, 30, 30, 30, 20, 20, 10, 40, 50, 50, 50, 50, 50]
find_it(seq)
