def greatRenaming(roadRegister):
    ans = roadRegister[-1:] + roadRegister[:-1]
    for p, r in enumerate(ans):
        ans[p] = r[-1:] + r[:-1]
    return ans
