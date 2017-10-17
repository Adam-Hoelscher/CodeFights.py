def minimumOnStack(operations):

    depth = 0
    stack = []
    min_count = [None]
    min_value = [float('Inf')]
    ans = []

    for op in operations:
        op = op.split(' ')

        if op[0] == 'min':
            ans.append(min_value[-1])
            continue

        if op[0] == 'push':
            val = int(op[1])
            stack.append(val)
            depth += 1
            if val < min_value[-1]:
                min_count.append(1)
                min_value.append(val)
            elif val == min_value:
                min_count[-1] += 1
            continue

        if op[0] == 'pop':
            val = stack.pop()
            depth -= 1
            if val == min_value[-1]:
                min_count[-1] -= 1
                if not min_count[-1]:
                    min_value.pop()
                    min_count.pop()
            continue

    return(ans)

if __name__ == '__main__':
    operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop",
                  "min", "pop", "min"]
    print(minimumOnStack(operations))
