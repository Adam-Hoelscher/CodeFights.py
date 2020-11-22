def mapDecoding(message):
    '''
    Count the number of possible decodings of the message. Each valid message
    will be made of an ordered set of substrings ("runs"). Each run will have 
    some number of ways it can be interpretted. The number of ways a run can
    be interpretted is a function of its length; in specific, the number of
    possible ways to interpret a run of length N is equal to the Nth Fibonacci
    number. e.g.
    "1"    has 1 interpretation
    "12"   has 2 interpretations
    "123"  has 3
    "1234" has 5
    Runs are broken either when either a single digit or a pair of digits falls
    outside the range [1, 26]. For a single digit this is only when that digit
    is 0. For a pair it is when that pair is more than 26. A 0 at the end of a
    run effectively shortens the run by 1, because 0 can only be valid as the
    units value of 10 or 20. In the case that the digit before a 0 is not 1 or
    2, the pair will be invalid also. An invalid pair ending with 0 means that
    there is no way that the run can be interpretted, which makes the entire
    message uninterprettable.
    '''

    ways = 1
    a, b = 0, 1

    for char, prior in zip(message, ' ' + message):

        # an invalid pair will stop the current run at this character
        if not 0 < int(prior + char) < 27:
            ways *= b
            a, b = 0, 1

        # a zero will stop the run AND has to be treated as part of the
        # preceding character note that if the pair was also invalid, then a
        # was just reset to 0, so this block will set ways = 0
        if char == '0':
            ways *= a
            a, b = 0, 1
            
        # if the character is not zero, advance the run
        if char != '0':
            a, b = b, a + b

    # we reached the end of the message so we need to end the last run
    ways *= b

    return ways % (10 ** 9 + 7)
