from heapq import heappop, heappush


def fileSyncOrder(files, storageLimit, uploadSpeed, duration):

    files = [(time, size, idx) for idx, (size, time) in enumerate(files)]
    files.sort()

    queue = []
    working_on = None
    finished = []
    
    while t <= duration:
        
        if t == busy and working_on is not None:
            finished.append(working_on)
            busy, working_on = 0, None

        while files and t >= files[-1][1]:
            size, time, idx = files.pop()
            heappush(queue, (size, idx))

        while not busy and queue:
            size, idx = heappop(queue)
            if size <= storageLimit:
                busy, working_on = t + size // uploadSpeed, idx
                storageLimit -= size

        if busy:
            t = busy
        elif files:
            t = files[-1][1]
        else:
            break
        
    return finished
