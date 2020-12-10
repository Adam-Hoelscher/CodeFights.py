CANCEL = 0
MANUAL = 1


def backupHistory(creationTimes, backupRequests, k, t):

    files = [{'created': c, 'last': t, 'manual': set()} for c in creationTimes]

    for req, idx, time in backupRequests:
        f = files[idx]
        if req == CANCEL:
            f['last'] = min(f['last'], time - 1)
        elif req == MANUAL:
            f['manual'].add(time)


    def single(f):

        auto_count = max(0, (f['last'] - f['created']) // k)

        first_auto = f['created'] + k
        last_auto = f['last'] + 1
        auto_times = range(first_auto, last_auto , k)

        man_count = sum(m <= t and m not in auto_times for m in f['manual'])

        return auto_count + man_count

    return [single(f) for f in files]
