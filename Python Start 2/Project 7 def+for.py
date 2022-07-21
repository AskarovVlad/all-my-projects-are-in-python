def building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Week %s : cans: %s ' % (week, total_cans))
building(2)
