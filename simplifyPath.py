def simplifyPath(path):

    stack = [x for x in reversed(path.split(sep='/'))]

    output = []
    while stack:
        k = stack.pop()
        if k in ['', '.'] : pass
        elif k == '..':
            try:
                output.pop()
                output.pop()
            except:
                pass
        else:
            output.append(k)
            output.append('/')
    try:
        output.pop()
    except:
        pass

    return(''.join(['/'] + output))
