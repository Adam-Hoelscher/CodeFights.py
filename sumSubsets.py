def sumSubsets(arr, num):

    answers = set()
    
    def search(arr, num, curr=[]):

        if not num:
            answers.add(tuple(curr))

        elif 0 < num <= sum(arr):
            for idx, val in enumerate(arr):
                search(arr[idx+1:], num - val, curr + [val])

    search(arr, num)

    return sorted(answers)
