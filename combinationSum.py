def combinationSum(a, sum):

    def rf(a, sum):

        if sum == 0:
            return []

        elif a:

            stuff = []
            val = a[0]

            next_sum = sum
            prefix = []

            while next_sum > 0:
                suffixes = rf(a[1:], next_sum)
                for s in suffixes or []:
                    stuff.append(prefix + s)
                prefix += [val]
                next_sum -= val
            
            if next_sum == 0:
                stuff.append(prefix)

            return stuff

    answers = rf(sorted(set(a)), sum)

    output = [str(tuple(t)).replace(',','') for t in answers]
    output.sort()
    output = ''.join(output)

    return output or 'Empty' 
