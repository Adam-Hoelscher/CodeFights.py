def composeRanges(nums):
    
    output = []
    nums.reverse()
    
    while nums:
        range_beg = range_end = nums.pop()
        while nums and nums[-1] == range_end + 1:
            range_end = nums.pop()
        
        if range_beg == range_end:
            range_str = f'{range_end}'
        else:
            range_str = f'{range_beg}->{range_end}'
            
        output.append(range_str)
    
    return output
