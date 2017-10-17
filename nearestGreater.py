def nearestGreater(a):

    ans = []
    length = len(a)

    right = []
    for a_pos, num in enumerate(reversed(a)):
        if not right:
            right.append(None)
            continue
        look_at = length - a_pos
        while a[look_at] <= num:
            look_at = right[length - look_at - 1]
            if look_at is None: break
        right.append(look_at)

    left = []

    for a_pos, (num, r_pos) in enumerate(zip(a,reversed(right))):

        if not left:
            l_pos = None
        else:
            l_pos = a_pos - 1
            while a[l_pos] <= num:
                l_pos = left[l_pos]
                if l_pos is None: break
        left.append(l_pos)

        if l_pos is None and r_pos is None:
            ans.append(-1)
            continue
        if l_pos is None:
            ans.append(r_pos)
            continue
        if r_pos is None:
            ans.append(l_pos)
            continue
        near = sorted([l_pos, r_pos], key = lambda x: abs(x - a_pos))[0]
        ans.append(near)

    return(ans)


if __name__ == '__main__':
    a= [1, 4, 2, 1, 7, 6]
    print(a)
    print(nearestGreater(a))
