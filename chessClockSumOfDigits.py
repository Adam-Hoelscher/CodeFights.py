def chessClockSumOfDigits(initialTime, k):
    
    def int_from_str(string):
        m, ss = map(int, string.split('.'))
        return 60 * m + ss

    def str_from_int(integer):
        return '{}.{:02}'.format(*divmod(integer, 60))
        
    def dig_sum(times):
        return sum(sum(int(d) for d in t.replace('.', '')) for t in times)
       
    a_beg, b_beg = [int_from_str(s) for s in initialTime]
    k = min(k, a_beg + b_beg - 1)
    
    def combos():
        for time_taken in range(k + 1):
            for a_taken in range(time_taken + 1):
                b_taken = time_taken - a_taken
                a_end = max(0, a_beg - a_taken)
                b_end = max(0, b_beg - b_taken)
                times = [str_from_int(i) for i in [a_end, b_end]]
                yield dig_sum(times)

    return min(combos()), max(combos())
