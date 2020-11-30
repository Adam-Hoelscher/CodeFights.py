def taskMaker(source, challengeId):

    challenge_string = f'//DB {challengeId}//'

    out = []
    for ln in source:
        if ln.strip().startswith(challenge_string):
            out.pop()
            out.append(ln.replace(challenge_string, ''))
        elif not ln.strip().startswith('//'):
            out.append(ln)

    return out
